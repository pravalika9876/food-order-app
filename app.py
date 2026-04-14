from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from extensions import db
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_socketio import SocketIO
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# 🔐 Secret key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

# 📦 Database config (important for deployment)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///foodapp.db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

socketio = SocketIO(app)

from models import User, Restaurant, MenuItem, Order, CartItem

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ✅ IMPORTANT: Create DB tables on startup (FIXED)
with app.app_context():
    db.create_all()

# ---------------- ROUTES ---------------- #

@app.route('/')
def index():
    restaurants = Restaurant.query.all()
    return render_template('index.html', restaurants=restaurants)


@app.route('/search')
def search():
    query = request.args.get('q', '')
    res_matches = Restaurant.query.filter(
        Restaurant.name.contains(query) | Restaurant.category.contains(query)
    ).all()

    item_matches = MenuItem.query.filter(
        MenuItem.name.contains(query) | MenuItem.category.contains(query)
    ).all()

    for item in item_matches:
        if item.restaurant not in res_matches:
            res_matches.append(item.restaurant)

    return render_template('index.html', restaurants=res_matches, search_query=query)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')

        existing_user = User.query.filter(
            (User.email == email) | (User.username == username)
        ).first()

        if existing_user:
            flash('Email or Username already exists!')
            return redirect(url_for('register'))

        hashed_pw = generate_password_hash(request.form.get('password'))
        new_user = User(username=username, email=email, password=hashed_pw)

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please login.')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form.get('email')

        user = User.query.filter(
            (User.email == identifier) | (User.username == identifier)
        ).first()

        if user and check_password_hash(user.password, request.form.get('password')):
            login_user(user)
            return redirect(url_for('index'))

        flash('Invalid email/username or password')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/restaurant/<int:rid>')
def restaurant_detail(rid):
    res = Restaurant.query.get_or_404(rid)
    menu = MenuItem.query.filter_by(restaurant_id=rid).all()
    return render_template('restaurant.html', restaurant=res, menu=menu)


@app.route('/add_to_cart', methods=['POST'])
@login_required
def add_to_cart():
    data = request.json
    item_id = data.get('item_id')

    cart_item = CartItem(user_id=current_user.id, menu_item_id=item_id)
    db.session.add(cart_item)
    db.session.commit()

    return jsonify({"status": "success"})


@app.route('/remove_from_cart', methods=['POST'])
@login_required
def remove_from_cart():
    data = request.json
    cart_item_id = data.get('cart_item_id')

    cart_item = CartItem.query.get(cart_item_id)
    if cart_item and cart_item.user_id == current_user.id:
        db.session.delete(cart_item)
        db.session.commit()

    return jsonify({"status": "success"})


@app.route('/get_cart')
@login_required
def get_cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()

    items_data = []
    total = 0

    for item in cart_items:
        m = MenuItem.query.get(item.menu_item_id)
        if m:
            items_data.append({"id": item.id, "name": m.name, "price": m.price})
            total += m.price
        else:
            db.session.delete(item)

    db.session.commit()

    return jsonify({"items": items_data, "total": round(total, 2)})


@app.route('/checkout', methods=['POST'])
@login_required
def checkout():
    data = request.json or {}
    address = data.get('address', 'Current Location')

    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()

    if not cart_items:
        return jsonify({"status": "error", "message": "Cart empty"})

    total = 0
    items_list = []

    for item in cart_items:
        m = MenuItem.query.get(item.menu_item_id)
        total += m.price
        items_list.append(m.name)
        db.session.delete(item)

    new_order = Order(
        user_id=current_user.id,
        total_price=total,
        items=",".join(items_list)
    )

    current_user.address = address

    db.session.add(new_order)
    db.session.commit()

    socketio.emit('order_status', {
        'order_id': new_order.id,
        'status': 'Preparing'
    })

    return jsonify({"status": "success", "order_id": new_order.id})


@app.route('/orders')
@login_required
def orders():
    user_orders = Order.query.filter_by(
        user_id=current_user.id
    ).order_by(Order.timestamp.desc()).all()

    return render_template('orders.html', orders=user_orders)


@app.route('/track/<int:oid>')
@login_required
def track_order(oid):
    order = Order.query.get_or_404(oid)
    return render_template('track.html', order=order)


# ✅ IMPORTANT for Render (gunicorn uses this)
if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000)
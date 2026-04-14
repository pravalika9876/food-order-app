from app import app
from extensions import db
from models import CartItem, MenuItem

with app.app_context():
    items = CartItem.query.all()
    print(f"Total Cart Items: {len(items)}")
    for i in items:
        m = MenuItem.query.get(i.menu_item_id)
        print(f"User {i.user_id}: {m.name if m else 'Invalid Item'}")

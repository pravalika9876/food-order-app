from app import app
from extensions import db
from models import Restaurant, MenuItem

def seed_data():
    with app.app_context():
        db.create_all()
        # Clear existing data
        MenuItem.query.delete()
        Restaurant.query.delete()
        db.session.commit()
        
        # --- Restaurants ---
        restaurants = [
            Restaurant(name="The Burger Lab", image_url="https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=500", rating=4.5, category="Burgers", lat=12.9716, lng=77.5946),
            Restaurant(name="Sushi Zen", image_url="https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=500", rating=4.8, category="Japanese", lat=12.9726, lng=77.5936),
            Restaurant(name="Pizza Haven", image_url="https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500", rating=4.2, category="Italian", lat=12.9706, lng=77.5956),
            Restaurant(name="Himalayan Spice", image_url="https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=500", rating=4.6, category="Indian", lat=12.9736, lng=77.5966),
            Restaurant(name="Taco Fiesta", image_url="https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?w=500", rating=4.4, category="Mexican", lat=12.9696, lng=77.5926),
            Restaurant(name="Green Bowl", image_url="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=500", rating=4.7, category="Healthy", lat=12.9746, lng=77.5916),
            Restaurant(name="Sweet Retreat", image_url="https://images.unsplash.com/photo-1551024601-bec78aea704b?w=500", rating=4.9, category="Desserts", lat=12.9756, lng=77.5986),
            Restaurant(name="Caffeine Coast", image_url="https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=500", rating=4.3, category="Cafe", lat=12.9686, lng=77.5906)
        ]
        
        db.session.add_all(restaurants)
        db.session.commit()
        
        r1, r2, r3, r4, r5, r6, r7, r8 = restaurants
        
        # --- Menu Items ---
        items = [
            # Burger Lab
            MenuItem(name="Classic Cheeseburger", price=12.99, description="Juicy beef patty with cheddar", category="Main", restaurant_id=r1.id, image_url="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=300"),
            MenuItem(name="Truffle Fries", price=5.99, description="Crispy fries with truffle oil", category="Sides", restaurant_id=r1.id, image_url="https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=300"),
            MenuItem(name="Bacon King", price=14.99, description="Double patty with crispy bacon", category="Main", restaurant_id=r1.id, image_url="https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=300"),
            MenuItem(name="Onion Rings", price=4.99, description="Crunchy breaded onion rings", category="Sides", restaurant_id=r1.id, image_url="https://images.unsplash.com/photo-1639024471283-035188835118?w=300"),
            
            # Sushi Zen
            MenuItem(name="Salmon Nigiri", price=18.99, description="Fresh salmon over rice", category="Main", restaurant_id=r2.id, image_url="https://images.unsplash.com/photo-1583623025817-d180a2221d0a?w=300"),
            MenuItem(name="Dragon Roll", price=22.50, description="Eel, cucumber, topped with avocado", category="Main", restaurant_id=r2.id, image_url="https://images.unsplash.com/photo-1559700014-f7207f1c71f5?w=300"),
            MenuItem(name="Miso Soup", price=4.50, description="Traditional bean paste soup", category="Starter", restaurant_id=r2.id, image_url="https://images.unsplash.com/photo-1547592166-23ac45744acd?w=300"),
            MenuItem(name="California Roll", price=14.99, description="Crab, avocado, and cucumber", category="Main", restaurant_id=r2.id, image_url="https://images.unsplash.com/photo-1579584425555-c3ce17fd4351?w=300"),
            
            # Pizza Haven
            MenuItem(name="Pepperoni Feast", price=15.99, description="Loaded with spicy pepperoni", category="Main", restaurant_id=r3.id, image_url="https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?w=300"),
            MenuItem(name="Way of the Veggie", price=13.99, description="Bell peppers, olives, mushrooms", category="Main", restaurant_id=r3.id, image_url="https://images.unsplash.com/photo-1574071318508-1cdbad80ad50?w=300"),
            MenuItem(name="Garlic Knots", price=6.50, description="Buttery dough with parsley", category="Sides", restaurant_id=r3.id, image_url="https://images.unsplash.com/photo-1541745537411-b8046dc6d66c?w=300"),
            
            # Himalayan Spice
            MenuItem(name="Butter Chicken", price=16.99, description="Creamy tomato curry with tender chicken", category="Main", restaurant_id=r4.id, image_url="https://images.unsplash.com/photo-1603894584113-f4726cd57790?w=300"),
            MenuItem(name="Paneer Tikka Masala", price=14.99, description="Grilled cottage cheese in spicy gravy", category="Main", restaurant_id=r4.id, image_url="https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=300"),
            MenuItem(name="Garlic Naan", price=3.99, description="Clay-oven bread with garlic", category="Sides", restaurant_id=r4.id, image_url="https://images.unsplash.com/photo-1533777857889-4be7c70b33f7?w=300"),
            
            # Taco Fiesta
            MenuItem(name="Steak Tacos", price=11.50, description="Three soft tacos with carne asada", category="Main", restaurant_id=r5.id, image_url="https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?w=300"),
            MenuItem(name="Chicken Quesadilla", price=10.99, description="Melted cheese with spiced chicken", category="Main", restaurant_id=r5.id, image_url="https://images.unsplash.com/photo-1599974579688-8dbdd335c77f?w=300"),
            MenuItem(name="Guacamole & Chips", price=7.99, description="Fresh avocado dip with corn chips", category="Appetizer", restaurant_id=r5.id, image_url="https://images.unsplash.com/photo-1541532713595-dc0a4c8410c2?w=300"),
            
            # Green Bowl
            MenuItem(name="Quinoa Harvest Bowl", price=13.50, description="Roasted veggies, quinoa, and tahini", category="Main", restaurant_id=r6.id, image_url="https://images.unsplash.com/photo-1543332164-6e82f355bee1?w=300"),
            MenuItem(name="Avocado Toast", price=9.99, description="Sourdough with poached egg", category="Main", restaurant_id=r6.id, image_url="https://images.unsplash.com/photo-1525351484163-7529414344d8?w=300"),
            MenuItem(name="Açaí Smoothie", price=8.50, description="Mixed berries and almond milk", category="Drinks", restaurant_id=r6.id, image_url="https://images.unsplash.com/photo-1553530666-ba11a7da3888?w=300"),
            
            # Sweet Retreat
            MenuItem(name="Chocolate Lava Cake", price=8.99, description="Warm cake with molten center", category="Dessert", restaurant_id=r7.id, image_url="https://images.unsplash.com/photo-1624353365286-3f8d62daad51?w=300"),
            MenuItem(name="Tiramisu", price=7.50, description="Classic Italian coffee dessert", category="Dessert", restaurant_id=r7.id, image_url="https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=300"),
            MenuItem(name="Strawberry Waffle", price=10.50, description="Fresh berries and whipped cream", category="Dessert", restaurant_id=r7.id, image_url="https://images.unsplash.com/photo-1504113888839-1c8ec72927d1?w=300"),
            
            # Caffeine Coast
            MenuItem(name="Caramel Macchiato", price=5.50, description="Espresso with vanilla and caramel", category="Coffee", restaurant_id=r8.id, image_url="https://images.unsplash.com/photo-1485808191679-5f86510681a2?w=300"),
            MenuItem(name="Avocado Latte", price=6.50, description="Creamy and unique blend", category="Coffee", restaurant_id=r8.id, image_url="https://images.unsplash.com/photo-1550850395-c19a84f6df2a?w=300"),
            MenuItem(name="Blueberry Muffin", price=4.25, description="Freshly baked daily", category="Pastry", restaurant_id=r8.id, image_url="https://images.unsplash.com/photo-1607958996333-41aef7caefaa?w=300"),
        ]
        
        db.session.add_all(items)
        db.session.commit()
        print("Database re-seeded with MASSIVE variety! 🍽️")

if __name__ == "__main__":
    seed_data()

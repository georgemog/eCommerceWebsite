# populate_db.py
from app import app, db, Product

def add_product(name, description, price, image_url):
    product = Product(name=name, description=description, price=price, image_url=image_url)
    db.session.add(product)

with app.app_context():
    # Clear existing products
    Product.query.delete()

    # Add some sample products
    products = [
        ("T-Shirt", "Comfortable cotton t-shirt", 19.99, "/static/images/tshirt.jpg"),
        ("Jeans", "Classic blue jeans", 49.99, "/static/images/jeans.jpg"),
        ("Sneakers", "Stylish and comfortable sneakers", 79.99, "/static/images/sneakers.jpg")
    ]

    for name, description, price, image_url in products:
        add_product(name, description, price, image_url)

    # Commit the changes
    db.session.commit()

    print("Database populated with sample products!")
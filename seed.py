from database import SessionLocal
from models import Sweet

db = SessionLocal()

sweets = [
    Sweet(name="Gulab Jamun", category="Indian", price=10.0, quantity=20),
    Sweet(name="Rasgulla", category="Indian", price=12.0, quantity=15),
    Sweet(name="Kaju Katli", category="Indian", price=25.0, quantity=10),
    Sweet(name="Ladoo", category="Indian", price=8.0, quantity=30),
    Sweet(name="Brownie", category="Bakery", price=50.0, quantity=5),
    Sweet(name="Cupcake", category="Bakery", price=40.0, quantity=7),
    Sweet(name="Donut", category="Bakery", price=35.0, quantity=12),
    Sweet(name="Chocolate Bar", category="Chocolate", price=20.0, quantity=25),
]

db.add_all(sweets)
db.commit()
db.close()

print("✅ Multiple sweets added successfully")
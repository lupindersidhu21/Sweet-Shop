from database import SessionLocal
from models import User

db = SessionLocal()
user = db.query(User).first()

user.is_admin = True
db.commit()
db.close()

print("Admin enabled")
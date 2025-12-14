from database import SessionLocal
from models import User

db = SessionLocal()

user = db.query(User).filter(User.username == "admin").first()

if not user:
    print("User not found")
else:
    user.is_admin = True
    db.commit()
    print("Admin enabled")

db.close()
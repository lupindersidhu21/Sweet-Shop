from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import engine, get_db
from models import Base, User, Sweet
from schemas import UserCreate, Token, SweetCreate, SweetUpdate
from auth import hash_password, verify_password, create_access_token
from dependencies import get_current_user, admin_required

# ---------------- APP SETUP ----------------

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- AUTH ----------------

@app.post("/api/auth/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(
        username=user.username,
        password=hash_password(user.password),
        is_admin=False
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}


@app.get("/api/auth/me")
def get_me(user: User = Depends(get_current_user)):
    return {
        "username": user.username,
        "is_admin": user.is_admin
    }
@app.post("/api/auth/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# ---------------- SWEETS ----------------

@app.post("/api/sweets")
def add_sweet(
    sweet: SweetCreate,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_sweet = Sweet(**sweet.dict())
    db.add(db_sweet)
    db.commit()
    db.refresh(db_sweet)
    return db_sweet


@app.get("/api/sweets")
def get_sweets(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Sweet).all()


@app.get("/api/sweets/search")
def search_sweets(
    user: User = Depends(get_current_user),
    name: str | None = None,
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Sweet)

    if name:
        query = query.filter(Sweet.name.contains(name))
    if category:
        query = query.filter(Sweet.category.contains(category))
    if min_price is not None:
        query = query.filter(Sweet.price >= min_price)
    if max_price is not None:
        query = query.filter(Sweet.price <= max_price)

    return query.all()


@app.put("/api/sweets/{id}")
def update_sweet(
    id: int,
    sweet: SweetUpdate,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_sweet = db.query(Sweet).get(id)

    if not db_sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    for key, value in sweet.dict(exclude_unset=True).items():
        setattr(db_sweet, key, value)

    db.commit()
    db.refresh(db_sweet)
    return db_sweet


@app.delete("/api/sweets/{id}")
def delete_sweet(
    id: int,
    admin: User = Depends(admin_required),
    db: Session = Depends(get_db)
):
    sweet = db.query(Sweet).get(id)

    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    db.delete(sweet)
    db.commit()
    return {"message": "Sweet deleted"}

# ---------------- INVENTORY ----------------

@app.post("/api/sweets/{id}/purchase")
def purchase_sweet(
    id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    sweet = db.query(Sweet).get(id)

    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    if sweet.quantity <= 0:
        raise HTTPException(status_code=400, detail="Out of stock")

    sweet.quantity -= 1
    db.commit()
    db.refresh(sweet)
    return sweet


@app.post("/api/sweets/{id}/restock")
def restock_sweet(
    id: int,
    amount: int = 1,
    admin: User = Depends(admin_required),
    db: Session = Depends(get_db)
):
    sweet = db.query(Sweet).get(id)

    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    sweet.quantity += amount
    db.commit()
    db.refresh(sweet)
    return sweet
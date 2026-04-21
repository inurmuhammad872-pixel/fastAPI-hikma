from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import uuid

from db.database import engine, SessionLocal
from db.models import Base, TypeAUser, TypeBUser, TypeCUser
from schemas.schemas import TypeACreate, TypeBCreate, TypeCCreate, UserLogin

Base.metadata.create_all(bind=engine)

app = FastAPI()


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- REGISTER ----------------

@app.post("/register/type_a")
def register_type_a(user: TypeACreate, db: Session = Depends(get_db)):
    new_user = TypeAUser(
        id=str(uuid.uuid4()),
        first_name=user.first_name,
        last_name=user.last_name,
        father_name=user.father_name,
        phone=user.phone,
        gender=user.gender,
        birth_date=user.birth_date,
        region=user.region,
        district=user.district,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    return {"message": "Type A user created"}


@app.post("/register/type_b")
def register_type_b(user: TypeBCreate, db: Session = Depends(get_db)):
    new_user = TypeBUser(
        id=str(uuid.uuid4()),
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        relation=user.relation,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    return {"message": "Type B user created"}


@app.post("/register/type_c")
def register_type_c(user: TypeCCreate, db: Session = Depends(get_db)):
    new_user = TypeCUser(
        id=str(uuid.uuid4()),
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    return {"message": "Type C user created"}


# ---------------- LOGIN ----------------

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    # Type A
    db_user = db.query(TypeAUser).filter(TypeAUser.phone == user.phone).first()
    if db_user and db_user.password == user.password:
        return {"message": "Login successful", "type": "A"}

    # Type B
    db_user = db.query(TypeBUser).filter(TypeBUser.phone == user.phone).first()
    if db_user and db_user.password == user.password:
        return {"message": "Login successful", "type": "B"}

    # Type C
    db_user = db.query(TypeCUser).filter(TypeCUser.phone == user.phone).first()
    if db_user and db_user.password == user.password:
        return {"message": "Login successful", "type": "C"}

    return {"error": "Invalid credentials"}
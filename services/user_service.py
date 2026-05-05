from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
import uuid

from db.models.user import User, TypeAUser, TypeBUser, TypeCUser
from core.security import hash_password


# -------------------------
# Helper
# -------------------------
def normalize_phone(phone: str):
    return phone.replace(" ", "").replace("-", "").strip()


# -------------------------
# Base Create Function
# -------------------------
def _create_user(db: Session, data, role: str):
    # Normalize phone
    phone = normalize_phone(data.phone)

    # 1. Email check
    existing_email = db.query(User).filter(User.email == data.email).first()
    if existing_email:
        raise HTTPException(409, "User with this email already exists")

    # 2. Phone check (role-based table)
    if role == "type_a":
        existing_phone = db.query(TypeAUser).filter(TypeAUser.phone == phone).first()
    elif role == "type_b":
        existing_phone = db.query(TypeBUser).filter(TypeBUser.phone == phone).first()
    else:
        existing_phone = db.query(TypeCUser).filter(TypeCUser.phone == phone).first()

    if existing_phone:
        raise HTTPException(400, "Phone number already registered")

    # 3. Create User (auth table)
    user = User(
        id=str(uuid.uuid4()),
        email=data.email,
        hashed_password=hash_password(data.password),
        role=role
    )

    db.add(user)

    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(400, "User creation failed")

    # 4. Create Profile
    if role == "type_a":
        profile = TypeAUser(
            id=user.id,
            first_name=data.first_name,
            last_name=data.last_name,
            father_name=data.father_name,
            phone=phone,
            gender=data.gender,
            birth_date=data.birth_date,
            region=data.region,
            district=data.district
        )

    elif role == "type_b":
        profile = TypeBUser(
            id=user.id,
            first_name=data.first_name,
            last_name=data.last_name,
            father_name=data.father_name,
            phone=phone,
            relation=data.relation
        )

    elif role == "type_c":
        profile = TypeCUser(
            id=user.id,
            first_name=data.first_name,
            last_name=data.last_name,
            father_name=data.father_name,
            phone=phone
        )

    else:
        raise HTTPException(400, "Invalid user type")

    db.add(profile)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(400, "Phone already exists")

    return {
        "message": "User created",
        "user_id": user.id,
        "role": user.role
    }


# -------------------------
# Public Functions
# -------------------------
def create_type_a_user(db: Session, data):
    return _create_user(db, data, "type_a")


def create_type_b_user(db: Session, data):
    return _create_user(db, data, "type_b")


def create_type_c_user(db: Session, data):
    return _create_user(db, data, "type_c")
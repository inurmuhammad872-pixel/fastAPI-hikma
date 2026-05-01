from sqlalchemy.orm import Session
from fastapi import HTTPException
import uuid
from db.models.user import User, TypeAUser, TypeBUser, TypeCUser
from core.security import hash_password


def _create_user(db: Session, data, role):
    # Duplicate email check
    existing_user = db.query(User).filter(User.email == data.email).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="User with this email already exists"
        )

    # Create auth user
    user = User(
        id=str(uuid.uuid4()),
        email=data.email,
        hashed_password=hash_password(data.password),
        role=role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    # Create profile by role
    user_data = None

    if role == "type_a":
        user_data = TypeAUser(
            id=user.id,
            first_name=data.first_name,
            last_name=data.last_name,
            father_name=data.father_name,
            phone=data.phone,
            gender=data.gender,
            birth_date=data.birth_date,
            region=data.region,
            district=data.district
        )

    elif role == "type_b":
        user_data = TypeBUser(
            id=user.id,
            first_name=data.first_name,
            last_name=data.last_name,
            father_name=data.father_name,
            phone=data.phone,
            relation=data.relation
        )

    elif role == "type_c":
        user_data = TypeCUser(
            id=user.id,
            first_name=data.first_name,
            last_name=data.last_name,
            father_name=data.father_name,
            phone=data.phone
        )

    # Validate role
    if not user_data:
        raise HTTPException(
            status_code=400,
            detail="Invalid user type"
        )

    # Save profile
    db.add(user_data)
    db.commit()

    return {
        "message": "User created",
        "user_id": user.id,
        "role": user.role
    }


def create_type_a_user(db: Session, data):
    return _create_user(db, data, "type_a")


def create_type_b_user(db: Session, data):
    return _create_user(db, data, "type_b")


def create_type_c_user(db: Session, data):
    return _create_user(db, data, "type_c")
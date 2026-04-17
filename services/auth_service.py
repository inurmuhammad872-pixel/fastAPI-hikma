from sqlalchemy.orm import Session
from db.models import User
from core.security import verify_password
from core.auth import create_access_token

def login_user(db: Session, data):

    user = db.query(User).filter(User.phone == data.phone).first()

    if not user:
        raise Exception("User not found")

    if not verify_password(data.password, user.password):
        raise Exception("Wrong password")

    token = create_access_token({
        "user_id": user.id,
        "role": user.role
    })

    return {"access_token": token}
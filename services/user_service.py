import uuid
from sqlalchemy.orm import Session
from db.models import User, TypeAUser
from core.security import hash_password

def create_type_a_user(db: Session, data):

    db_user = TypeAUser(
        id=str(uuid.uuid4()),
        **data.dict(exclude={"password"})
    )
    db.add(db_user)

    auth_user = User(
        id=db_user.id,
        phone=data.phone,
        password=hash_password(data.password),
        role="type_a"
    )
    db.add(auth_user)

    db.commit()

    return {"message": "User created"}
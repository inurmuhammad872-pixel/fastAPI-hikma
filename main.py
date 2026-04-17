from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db.database import engine, SessionLocal
from db.models import Base
from schemas.schemas import TypeACreate, UserLogin
from services.user_service import create_type_a_user
from services.auth_service import login_user
from dependencies.dependencies import get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register/type_a")
def register(user: TypeACreate, db: Session = Depends(get_db)):
    return create_type_a_user(db, user)


@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, user)


@app.get("/me")
def me(user=Depends(get_current_user)):
    return user
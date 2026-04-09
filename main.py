import uuid
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from schemas import TypeACreate, TypeBCreate, TypeCCreate
from models import Base, TypeAUser, TypeBUser, TypeCUser

# Database sozlash
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Jadvallarni yaratish
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Registration API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Type A Registration
@app.post("/register/type_a")
async def register_type_a(user: TypeACreate, db: Session = Depends(get_db)):
    db_user = TypeAUser(
        id=str(uuid.uuid4()),
        first_name=user.first_name,
        last_name=user.last_name,
        father_name=user.father_name,
        phone=user.phone,
        gender=user.gender,
        birth_date=user.birth_date,
        region=user.region,
        district=user.district,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return {
        "id": db_user.id,
        "first_name": db_user.first_name,
        "last_name": db_user.last_name,
        "phone": db_user.phone,
        "message": "Muvaffaqiyatli registratsiya qilindi!"
    }

# Type B Registration
@app.post("/register/type_b")
async def register_type_b(user: TypeBCreate, db: Session = Depends(get_db)):
    db_user = TypeBUser(
        id=str(uuid.uuid4()),
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        relation=user.relation,
        reference_code=user.reference_code,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return {
        "id": db_user.id,
        "first_name": db_user.first_name,
        "last_name": db_user.last_name,
        "message": "Muvaffaqiyatli registratsiya qilindi!"
    }

# Type C Registration
@app.post("/register/type_c")
async def register_type_c(user: TypeCCreate, db: Session = Depends(get_db)):
    db_user = TypeCUser(
        id=str(uuid.uuid4()),
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        gender=user.gender,
        teacher_type=user.teacher_type,
        subject=user.subject,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return {
        "id": db_user.id,
        "first_name": db_user.first_name,
        "last_name": db_user.last_name,
        "message": "Muvaffaqiyatli registratsiya qilindi!"
    }

@app.get("/")
async def root():
    return {"message": "Xush kelibsiz! User Registration API"}
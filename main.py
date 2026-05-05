from fastapi import FastAPI
from db.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from api.routes.user import router as user_router
from api.routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://hikma.uz",
        "http://hikma.uz"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user_router)
app.include_router(auth_router)
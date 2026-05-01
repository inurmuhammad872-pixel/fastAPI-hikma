from fastapi import FastAPI
from db.database import engine, Base

from api.routes.user import router as user_router
from api.routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Include routers
app.include_router(user_router)
app.include_router(auth_router)
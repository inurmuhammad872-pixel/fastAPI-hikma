from fastapi import FastAPI
from db.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from api.routes.user import router as user_router
from api.routes.auth import router as auth_router
from api.routes import focus
from api.routes.growth import router as growth_router
from api.routes.thinking_tools import thinking_tools
from api.routes.thinking.thinking import router as thinking_router
from api.routes.personal_growth.self_awareness import (
    router as self_awareness_router
)

from api.routes.personal_growth.self_awareness import router as self_awareness_router
from api.routes.personal_growth.skill import router as skill_router
from api.routes.personal_growth.discipline import router as discipline_router
from api.routes.personal_growth.goal import router as goal_router
from api.routes.personal_growth.self_assessment import router as self_assessment_router
from api.routes.personal_growth.career import router as career_router
from api.routes.personal_growth.parent_dashboard import router as dashboard_router
from api.routes.personal_growth.parent_dashboard import router as parent_dashboard_router
from api.routes.personal_growth import (
    learning_profile
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    root_path="/api"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
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
app.include_router(focus.router)
app.include_router(growth_router)


app.include_router(
    self_awareness_router
)
app.include_router(thinking_tools.router)
app.include_router(thinking_router)


app.include_router(self_awareness_router)
app.include_router(skill_router)
app.include_router(discipline_router)
app.include_router(goal_router)
app.include_router(self_assessment_router)
app.include_router(
    learning_profile.router,
    prefix="/api"
)
app.include_router(career_router)
app.include_router(dashboard_router)
app.include_router(parent_dashboard_router)



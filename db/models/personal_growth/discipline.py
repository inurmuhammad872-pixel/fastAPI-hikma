from sqlalchemy import (
    Column,
    String,
    Boolean,
    Date,
    DateTime
)

from db.database import Base

from datetime import datetime
import uuid


class Habit(Base):
    __tablename__ = "pg_habits"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    user_id = Column(
        String,
        nullable=False
    )

    name = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class HabitLog(Base):
    __tablename__ = "pg_habit_logs"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    habit_id = Column(
        String,
        nullable=False
    )

    date = Column(
        Date,
        nullable=False
    )

    completed = Column(
        Boolean,
        default=False
    )
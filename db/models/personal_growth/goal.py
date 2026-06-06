from sqlalchemy import (
    Column,
    String,
    Boolean,
    DateTime
)

from db.database import Base

from datetime import datetime
import uuid


class Goal(Base):
    __tablename__ = "pg_goals"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    user_id = Column(
        String,
        nullable=False
    )

    title = Column(
        String,
        nullable=False
    )

    completed = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
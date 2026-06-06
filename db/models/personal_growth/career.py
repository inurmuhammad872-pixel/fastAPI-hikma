from sqlalchemy import (
    Column,
    String,
    DateTime
)

from db.database import Base

from datetime import datetime
import uuid


class CareerInterest(Base):
    __tablename__ = "pg_career_interests"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    user_id = Column(
        String,
        nullable=False
    )

    interest = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
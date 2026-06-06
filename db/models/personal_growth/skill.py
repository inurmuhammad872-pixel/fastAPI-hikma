from sqlalchemy import Column, String, Integer, DateTime
from db.database import Base
from datetime import datetime
import uuid


class Skill(Base):
    __tablename__ = "pg_skills"

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

    score = Column(
        Integer,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
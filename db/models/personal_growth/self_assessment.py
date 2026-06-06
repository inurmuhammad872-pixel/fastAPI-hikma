from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime
)

from db.database import Base

from datetime import datetime
import uuid


class SelfAssessment(Base):
    __tablename__ = "pg_self_assessments"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    user_id = Column(
        String,
        nullable=False
    )

    confidence = Column(
        Integer,
        nullable=False
    )

    motivation = Column(
        Integer,
        nullable=False
    )

    focus = Column(
        Integer,
        nullable=False
    )

    social = Column(
        Integer,
        nullable=False
    )

    stress = Column(
        Integer,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
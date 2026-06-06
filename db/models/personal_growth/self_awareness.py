from sqlalchemy import Column, String, Text, DateTime
from db.database import Base
from datetime import datetime
import uuid


class SelfAwarenessQuestion(Base):
    __tablename__ = "pg_self_awareness_questions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    question = Column(Text, nullable=False)


class SelfAwarenessAnswer(Base):
    __tablename__ = "pg_self_awareness_answers"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    user_id = Column(String, nullable=False)

    question_id = Column(String, nullable=False)

    answer = Column(Text, nullable=False)

    ai_feedback = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
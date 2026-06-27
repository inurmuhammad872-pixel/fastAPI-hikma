from sqlalchemy import Column, Integer, String, Text, ForeignKey
from db.database import Base


class GrowthAnswer(Base):
    __tablename__ = "growth_answers"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    question_id = Column(Integer, ForeignKey("growth_questions.id"))

    step = Column(Integer)

    ai_question = Column(Text)

    answer = Column(Text)

    ai_feedback = Column(Text)
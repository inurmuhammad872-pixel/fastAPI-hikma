from sqlalchemy import Column, Integer, Text, ForeignKey
from db.database import Base

class GrowthAnswer(Base):
    __tablename__ = "growth_answers"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("growth_questions.id"))
    answer = Column(Text)
from sqlalchemy import Column, Integer, String, Text
from db.database import Base


class GrowthQuestion(Base):

    __tablename__ = "growth_questions"

    id = Column(Integer, primary_key=True, index=True)

    category = Column(String, nullable=False)

    question = Column(Text, nullable=False)

    scenario = Column(Text, nullable=True)
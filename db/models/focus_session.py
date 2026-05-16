from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime
Base = declarative_base()



class FocusSession(Base): 
    __tablename__ = "focus_sessions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    duration = Column(Integer)  
    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime, nullable=True)
    status = Column(String, default="active")  # active, completed, interrupted
    note = Column(Text, nullable=True)
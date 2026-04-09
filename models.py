from datetime import date
from sqlalchemy import Column, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TypeAUser(Base):
    __tablename__ = "type_a_users"
    id = Column(String, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    father_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    region = Column(String, nullable=False)
    district = Column(String, nullable=False)
    role = Column(String, default="type_a")

class TypeBUser(Base):
    __tablename__ = "type_b_users"
    id = Column(String, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    relation = Column(String, nullable=False)
    reference_code = Column(String, nullable=True)
    role = Column(String, default="type_b")

class TypeCUser(Base):
    __tablename__ = "type_c_users"
    id = Column(String, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    teacher_type = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    role = Column(String, default="type_c")
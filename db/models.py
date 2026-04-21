from sqlalchemy import Column, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TypeAUser(Base):
    __tablename__ = "type_a_users"

    id = Column(String, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    father_name = Column(String)
    phone = Column(String, unique=True, index=True)
    gender = Column(String)
    birth_date = Column(Date)
    region = Column(String)
    district = Column(String)
    password = Column(String)


class TypeBUser(Base):
    __tablename__ = "type_b_users"

    id = Column(String, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String, unique=True, index=True)
    relation = Column(String)
    password = Column(String)


class TypeCUser(Base):
    __tablename__ = "type_c_users"

    id = Column(String, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String, unique=True, index=True)
    password = Column(String)
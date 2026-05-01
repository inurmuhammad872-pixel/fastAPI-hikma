from sqlalchemy import Column, String, Date
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)


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


class TypeBUser(Base):
    __tablename__ = "type_b_users"

    id = Column(String, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    father_name = Column(String)
    phone = Column(String, unique=True, index=True)
    relation = Column(String)

class TypeCUser(Base):
    __tablename__ = "type_c_users"

    id = Column(String, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    father_name = Column(String)
    phone = Column(String, unique=True, index=True)
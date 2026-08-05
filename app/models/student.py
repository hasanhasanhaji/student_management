from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base

class Student(Base):
    """
    Student model representing the students table in the database.
    """
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
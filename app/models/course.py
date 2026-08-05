from app.core.database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(100), nullable=False)

    unit = Column(Integer, nullable=False)

    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    student = relationship("Student", back_populates="courses")
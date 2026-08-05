from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import DateTime
from app.core.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime



class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key= True
    )

    first_name: Mapped[str] = mapped_column(
        String(50)
    )

    last_name: Mapped[str] = mapped_column(
        String(50)
    )

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    age: Mapped[int]

    major: Mapped[str]

    gpa: Mapped[float]

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    courses = relationship("Course", back_populates="student", cascade="all, delete-orphan")
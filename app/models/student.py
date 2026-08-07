from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import MappedColumn
from app.database.base import Base


# Student database model
class Student(Base):
    __tablename__ = "students"

    id : Mapped[int] = MappedColumn(
        primary_key=True,
        index = True
    )

    name : Mapped[str] = MappedColumn(
        String(100),
        nullable = False
    )

    age : Mapped[int] = MappedColumn(
            Integer,
            nullable = False
        )

    email : Mapped[str] = MappedColumn(
                String(255),
                nullable = False,
                unique = True
            )


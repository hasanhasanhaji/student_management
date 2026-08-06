from datetime import datetime
from app.database.database import Base
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
)

class User(Base):
    """
    User table.
    """

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    username = Column(
        String,
        unique=True,
        nullable=False,
        index=True,
    )

    email = Column(
        String,
        unique=True,
        nullable=False,
        index=True,
    )

    password = Column(
        String,
        nullable=False,
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
DATABASE_URL = (
    "postgresql://postgres:0173276@localhost:5432/student_management"
)

engine = create_engine(
    DATABASE_URL, 
    echo = True
)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(bind= engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
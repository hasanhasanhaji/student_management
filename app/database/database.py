from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

# PostgreSQL connection URL
DATABASE_URL = (
    "postgresql://postgres:0173276@localhost:5432/student_db"
)

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = DeclarativeBase()

def get_db():
    """
    Provide database session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings



# Create a SQLAlchemy engine
engine = create_engine(
    settings.DATABASE_URL
)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    """
    Provide database session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
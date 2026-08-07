from collections.abc import Generator
from sqlalchemy.orm import Session
from app.database.session import SessionLocal

# Database session dependency
def get_db() -> Generator[Session, None, None]:
    # create db session
    db = SessionLocal()

    try:
        # Provide session to endpoint
        yield db
    finally:
        db.close() # Close database session
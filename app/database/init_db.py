from app.database.database import engine
from app.database.database import Base
from app.models.student import Student

# Create the database tables
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
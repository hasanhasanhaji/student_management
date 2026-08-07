from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker

# DB url
DATABASE_URL = ("postgresql+psycopg2://postgres:0173276@localhost:5432/student_db")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo= True)

# Create session factory
SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind= engine)
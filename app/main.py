from fastapi import FastAPI
from app.routers import student

# temp for test
from app.database.session import engine
from app.database.base import Base
from app.models.student import Student

# Create all tables موقت()
Base.metadata.create_all(bind= engine)


# Create FastAPI application instance
app = FastAPI(
    title="Student Management API",
    description="Professional Student Management System",
    version="1.0.0"
)

# Include  routers
app.include_router(student.router)

# root EndPoint
@app.get("/")
def home():
    return{
       "message": "Student Management API is running" 
    }
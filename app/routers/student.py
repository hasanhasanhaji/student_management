from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.schemas.student import StudentCreate

# Create router instance for student endpoints
router = APIRouter(
    prefix="/students",
    tags= ["Students"] 
)

# Get all students endpoint
@router.get("/")
def get_students(db :Session = Depends(get_db)):
    return {
        "message":"Student list"
    }

# Create a new student
@router.post("/")
def create_student(student :StudentCreate, db: Session = Depends(get_db)):
    return {
        "message": "Student received",
        "database": str(db)
    }
from fastapi import APIRouter
from app.schemas.student import StudentCreate

# Create a router for student-related endpoints
router = APIRouter()

# Define a GET endpoint to retrieve a list of students
@router.get("/students")
def get_students():
    return {
        "students": [
            {
                "id": 1,
                "name": "Ali"
            },
            {
                "id": 2,
                "name": "Sara"
            }
        ]
    }

# Define a POST endpoint to create a new student
@router.post("/students")
def create_student(student: StudentCreate):
    return {
        "message": "Student created successfully",
        "student": student
    }
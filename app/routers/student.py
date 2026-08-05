from fastapi import APIRouter
from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from app.schemas.student import StudentCreate, StudentResponse
from app.database.database import get_db
from app.services.student_service import *


# Create a router for student-related endpoints
router = APIRouter()

# Define a GET endpoint to retrieve a list of students
@router.get("/students")
def get_students():
    """
    Get all students API endpoint.
    """
    return get_students_service()

@router.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    """
    Get student by ID API endpoint.
    """
    student = get_student_by_id_service(student_id)
    if student:
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")

# Define a POST endpoint to create a new student
@router.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)): 
    """
    Create student API endpoint.

    Router responsibility:
    Receive request and call service layer.
    """

    # Send request to service layer
    created_student = create_student_service(db,student)
    return created_student

@router.delete("/students/{student_id}")
def delete_student(student_id: int):

    """
    Delete student endpoint.
    """


    student = delete_student_service(student_id)


    # Student was not found.
    if student is None:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )


    return {

        "message": "Student deleted",

        "student": student
    }
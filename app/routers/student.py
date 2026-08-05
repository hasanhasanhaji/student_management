from fastapi import APIRouter
from app.schemas.student import StudentCreate, StudentResponse
from app.services.student_service import create_student_service
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
@router.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate): 
    """
    Create student API endpoint.

    Router responsibility:
    Receive request and call service layer.
    """
    
    # Call business logic from service layer.
    created_student = create_student_service(student)

    return created_student
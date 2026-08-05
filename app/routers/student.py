from fastapi import APIRouter

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
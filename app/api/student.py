from fastapi import APIRouter
from app.schemas.students import StudentCreate
from app.services.student_service import StudentService


router = APIRouter(
    prefix="/students",
     tags=["Students"]
)

service = StudentService()


@router.get("/")
def get_students():
    return {
        "id": 1,
        "name": "Ali",
    }

@router.post("/")
def create_student(student: StudentCreate):
    return service.create_student(student)
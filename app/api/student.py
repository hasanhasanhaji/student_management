from fastapi import APIRouter
from app.schemas.students import StudentCreate,StudentUpdate, StudentResponse
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

@router.get("/{student_id}")
def get_students(student_id: int):
    return {
        "id": student_id,
        "name": "Ali",
    }


@router.post("/")
def create_student(student: StudentCreate):
    return service.create_student(student)

@router.put("/{student_id}")
def update_student(student_id: int,student:StudentUpdate):
    return service.StudentUpdate(student_id,student)
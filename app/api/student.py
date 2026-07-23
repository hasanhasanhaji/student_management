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
    return  service.get_students()

@router.get("/{student_id}")
def get_students(student_id: int):
    return service.get_students(student_id)


@router.post("/")
def create_student(student: StudentCreate):
    return service.create_student(student)

@router.put("/{student_id}")
def update_student(student_id: int,student:StudentUpdate):
    return service.update_student(student_id,student)

@router.delete("/{student_id}")
def delete_student(student_id: int):
    return service.delete_student(student_id)
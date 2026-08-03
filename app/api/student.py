from fastapi import APIRouter
from app.core.database import get_db
from app.schemas.students import StudentCreate,StudentUpdate, StudentResponse
from app.services.student_service import StudentService
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

from app.repositories.student_repository import StudentRepository

router = APIRouter(
    prefix="/students",
     tags=["Students"]
)

# service = StudentService()


@router.get("/")
def get_students(db: Session = Depends(get_db)):
    service = StudentService(db)
    return service.get_students()

@router.get("/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    service = StudentService(db)
    return service.get_student(student_id)


@router.post("/")
def create_student(student: StudentCreate, db:Session = Depends(get_db)):
    service = StudentService(db)
    return service.create_student(student)
   

# @router.put("/{student_id}")
# def update_student(student_id: int,student:StudentUpdate):
#     return service.update_student(student_id,student)

# @router.delete("/{student_id}")
# def delete_student(student_id: int):
#     return service.delete_student(student_id)
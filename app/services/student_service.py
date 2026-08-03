from app.repositories.student_repository import StudentRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException

class StudentService:
    def __init__(self, db: Session):
        self.repository = StudentRepository(db)

    def get_students(self):
        return self.repository.get_all()

    def get_student(self, student_id: int):
        student = self.repository.get_by_id(student_id)
        if student is None:
             raise HTTPException(
                 status_code= 404,
                 detail= "Student not found."
             )
        return student

    def create_student(self, student):
        return self.repository.create(student)

    def update_student(self, student_id: int, student):
        updated_student = self.repository.update(
             student_id,
        student
        )
        if self.update_student is None:
            raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
        return updated_student    

    # def delete_student(self, student_id):
    #     return self.repository.delete(student_id)


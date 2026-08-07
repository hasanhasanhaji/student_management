from sqlalchemy.orm import Session
from app.repositories import student_repository
from app.schemas.student import StudentCreate

# Create student service
def create_student(
        db: Session,
    student_data: StudentCreate
):
    # Call repository layer
    return student_repository.create_student(db, student_data)
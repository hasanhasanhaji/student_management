from app.schemas.student import StudentCreate
from sqlalchemy.orm import Session
from app.repositories.student_repository import create_student

students_db= []  # Initialize an empty list to store student records

def get_students_service():
    """
    Retrieve all student records from the in-memory database.

    Returns:
        List of student objects.
    """
    return students_db

def get_student_by_id_service(student_id: int):
    """
    Find student by ID.
    """
    for student in students_db:
        if student["id"] == student_id:
            return student
    return None

def create_student_service(db: Session,student: StudentCreate):
    """
    Create a new student record and add it to the in-memory database.
    Args:
        student:
            Validated student data from Pydantic schema.

    Returns:
        Created student object.
    """
    return create_student(
        db,
        student
    )

def delete_student_service(student_id: int):
    """
    Delete student by ID.
    """
    for index, student in enumerate(students_db):


        if student["id"] == student_id:


            # Remove student from storage.
            deleted_student = students_db.pop(index)


            return deleted_student


    return None

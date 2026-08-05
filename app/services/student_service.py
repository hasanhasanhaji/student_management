from app.schemas.student import StudentCreate
from sqlalchemy.orm import Session
from app.repositories.student_repository import *


def get_students_service( db: Session):
    """
    Retrieve all student records from the in-memory database.

    Returns:
        List of student objects.
    """
    return get_students(db)

def get_student_service( db: Session,student_id: int):
    """
    Find student by ID.
    """
    return get_student_by_id(
        db,
        student_id
    )

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

def update_student_service(
    db: Session,
    student_id: int,
    student: StudentCreate
):

    """
    Update student.
    """


    return update_student(
        db,
        student_id,
        student
    )


def delete_student_service(
    db: Session,
    student_id: int
):

    """
    Delete student.
    """


    return delete_student(
        db,
        student_id
    )

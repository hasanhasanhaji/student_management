from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate

def create_student(db: Session, student: StudentCreate):
    """
    Create a new student in database.
    """

    # Convert schema object into database model
    db_student = Student(
        name=student.name,
        age=student.age,
        email=student.email
    )

    ## Add the new student to the database session and commit the transaction
    db.add(db_student)
    db.commit()
    # Refresh object to get generated fields like ID
    db.refresh(db_student)

    return db_student
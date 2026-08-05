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

def get_students(db: Session):
    """
    Retrieve all students from the database.
    """
    return db.query(Student).all()


def get_student_by_id(db: Session, student_id: int):
    """
    Retrieve a student by their ID.
    """
    return db.query(Student).filter(Student.id == student_id).first()


def update_student(db: Session, student_id: int, student_data: StudentCreate):
    """
    Update an existing student's information.
    """
    student = get_student_by_id(
        db,
        student_id
    )

    if student is None:

        return None
    
    if student:
        student.name = student_data.name
        student.age = student_data.age
        student.email = student_data.email

        db.commit()
        db.refresh(student)
    return student

def delete_student(db: Session, student_id: int):
    """
    Delete a student from the database.
    """
    student = get_student_by_id(db, student_id)
    if student is None:
        return None

    db.delete(student)
    db.commit()
    return student
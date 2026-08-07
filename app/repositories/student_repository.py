from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate

# Create a studenet in db
def create_student(db:Session, student_data:StudentCreate):
    # Create database object
    student = Student(
        name=student_data.name,
        age=student_data.age,
        email=student_data.email 
    )

    # Add object to session
    db.add(student)

    # Save changes to database
    db.commit()

    # Refresh object with database values
    db.refresh(student)

    return student


from app.schemas.student import StudentCreate

students_db= []  # Initialize an empty list to store student records

def create_student_service(student: StudentCreate):
    """
    Create a new student record and add it to the in-memory database.
    Args:
        student:
            Validated student data from Pydantic schema.

    Returns:
        Created student object.
    """
    new_student = { "id": len(students_db) + 1,

        "name": student.name,

        "age": student.age,

        "email": student.email }
    students_db.append(new_student)

    return new_student
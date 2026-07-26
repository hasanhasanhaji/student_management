from datetime import datetime
from sqlalchemy.orm import Session  
from app.models.student import Student

class StudentRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_all(self):
        return self.db.query(Student).all()

    # def get_by_id(self, student_id):
    #     for student in self.students:
    #         if student["id"] == student_id:
    #             return student
    #     return None

    def create(self, student):
        db_student = Student(
            first_name=student.first_name,
            last_name=student.last_name,
            email=student.email,
            age=student.age,
            major=student.major,
             gpa=student.gpa
        )
        self.db.add(db_student)
        self.db.commit()
        self.db.refresh(db_student)
        return db_student

    # def update(self, student_id, student):

    #     existing = self.get_by_id(student_id)

    #     if existing is None:
    #         return None

    #     data = student.model_dump(exclude_unset=True)

    #     existing.update(data)

    #     existing["updated_at"] = datetime.now()

    #     return existing

    # def delete(self, student_id):

    #     existing = self.get_by_id(student_id)

    #     if existing is None:
    #         return False

    #     self.students.remove(existing)

    #     return True
from datetime import datetime
from sqlalchemy.orm import Session  
from app.models.student import Student

class StudentRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_all(self):
        return self.db.query(Student).all()

    def get_by_id(self, student_id: int):
        return self.db.query(Student).filter(Student.id == student_id).first()

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

    def update(self, student_id: int, student_data):

        student = self.get_by_id(student_id)

        if student is None:
            return None
        student.first_name = student_data.firast_name
        student.last_name = student_data.last_name
        student.email = student_data.email
        student.age = student_data.age
        student.major = student_data.major
        student.gpa = student_data.gpa

        self.db.commit()
        self.db.refresh()

        return student

    # def delete(self, student_id):

    #     existing = self.get_by_id(student_id)

    #     if existing is None:
    #         return False

    #     self.students.remove(existing)

    #     return True
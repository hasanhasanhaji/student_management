from app.repositories.student_repository import StudentRepository

class StudentService:
    def __init__(self):
        self.repository = StudentRepository()

    def get_students(self):
        return self.repository.get_all()

    def get_students(self, student_id):
         return self.repository.get_by_id(student_id)

    def create_student(self, student):
        return self.repository.create(student)

    def update_student(self, student_id, student):
        return self.repository.update(student_id, student)

    def delete_student(self, student_id):
        return self.repository.delete(student_id)


from app.repositories import student_repository

class StudentService:
    def __init__(self):
        self.repository = student_repository
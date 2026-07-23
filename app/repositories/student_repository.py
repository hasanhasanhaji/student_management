from datetime import datetime

class StudentRepository:
    def __init__(self):
        self.students = []
        self.current_id = 1

    def get_all(self):
        return self.students

    def get_by_id(self, student_id):
        for student in self.students:
            if student["id"] == student_id:
                return student
        return None

    def create(self, student):
        new_student = student.model_dump()

        new_student["id"] = self.current_id
        new_student["created_at"] = datetime.now()
        new_student["updated_at"] = datetime.now()

        self.current_id += 1

        self.students.append(new_student)

        return new_student

    def update(self, student_id, student):

        existing = self.get_by_id(student_id)

        if existing is None:
            return None

        data = student.model_dump(exclude_unset=True)

        existing.update(data)

        existing["updated_at"] = datetime.now()

        return existing

    def delete(self, student_id):

        existing = self.get_by_id(student_id)

        if existing is None:
            return False

        self.students.remove(existing)

        return True
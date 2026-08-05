from pydantic import BaseModel


class CourseCreate(BaseModel):

    title: str

    unit: int

    student_id: int
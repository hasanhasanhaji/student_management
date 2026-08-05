from fastapi import FastAPI
from app.core.database import Base
from app.core.database import engine
from app.models.student import Student
from app.models.course import Course
from app.api.student import router as student_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(student_router)



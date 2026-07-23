from fastapi import FastAPI
from typing import Optional
from app.api.student import router as student_router


app = FastAPI()

app.include_router(student_router)


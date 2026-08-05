from fastapi import FastAPI
from app.routers import student

app = FastAPI(title="Student Management API", version="1.0.0")

# Include the student router
app.include_router(student.router)


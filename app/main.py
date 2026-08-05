from fastapi import FastAPI
from app.routers import student

app = FastAPI(title="Student Management API", version="1.0.0")

app.include_router(student.router)


@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}
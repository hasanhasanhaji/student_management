from fastapi import FastAPI
from typing import Optional
from app.schemas.students import StudentCreate
from app.schemas.books import BookCreate
app = FastAPI()

@app.post('/students')
def create_student(student:StudentCreate):
    return student

@app.post('/books')
def create_book(book:BookCreate):
    return book
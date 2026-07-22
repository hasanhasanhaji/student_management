from fastapi import FastAPI
from typing import Optional
app = FastAPI()

@app.get('/')
def root():
    return {
        "Message" : "This is the first project in FastAPI."
    }

@app.get('/about')
def about():
    return {
        "framework": "FastAPI",
    "version": "1.0"
    }

@app.get('/health')
def health():
    return {
        "status": "ok"
    }

# @app.get('/students/{student_id}')
# def get_student(student_id :int):
#     return{
#         'student_id':student_id
#     }

@app.get('/students/{student_id}/courses/{course_id}')
def get_student(student_id :int, course_id : int):
    return{
        'student_id':student_id,
        'course_id': course_id
    }

# @app.get('/students')
# def get_student(name:str):
#     return {
#         "name":name
#     }

@app.get('/students')
def students(page:int, size:int):
    return{
        "page":page,
        "size":size
    }


@app.get('/students/{student_id}')
def get_student(student_id :int, details: bool = False):
    return{
        'student_id':student_id,
        "details": details
    }

# @app.get('/books/{book_id}')
# def get_books(book_id:int):
#     return{
#         'book_id':book_id
#     }

@app.get('/books')
def get_books(page:int, size:int):
    return{
        'page':page,
        'size':size,
    }
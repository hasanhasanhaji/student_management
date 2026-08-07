from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database.dependencies import get_db
from app.schemas.student import StudentCreate, StudentResponse, StudentUpdate
from app.models.student import Student
from app.services import student_service

# Create router instance for student endpoints
router = APIRouter(
    prefix="/students",
    tags= ["Students"] 
)

# Get all students endpoint
@router.get("/", response_model=list[StudentResponse])
def get_students(db :Session = Depends(get_db)):
   # create sql statement
   statement = select(Student)

   # Execute query
   result = db.execute(statement)

    # Convert result to Student objects
   students = result.scalars().all()
   return students

# get one student
@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session= Depends(get_db)):
    statement = (
        select(Student).where(Student.id == student_id)
    )
    result = db.execute(statement)
    student = result.scalars().first()
    return student

# Create a new student
@router.post("/",response_model=StudentResponse, status_code= 201)
def create_student(student :StudentCreate, db: Session = Depends(get_db)):
    return student_service.create_student( db, student)

# Update
@router.patch("/student_id", response_model=StudentResponse)
def update_student(student_id:int, student_date:StudentUpdate, db:Session = Depends(get_db)):
    # Load student from database
    statement = (select(Student).where(Student.id == student_id))
    reslut = db.execute(statement)
    student = reslut.scalars().first()

    if student is None:
        return None

    # Convert schema to dictionary
    update_data = student_date.model_dump(
        exclude_unset= True
    )

    # Update only provided fields
    for k,v in update_data.items():
        setattr(student, k , v)

    db.commit()
    db.refresh(student)
    return student


@router.delete("/{student_id}", status_code=204)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    statement = select(Student).where(Student.id == student_id) 
    result = db.execute(statement) 
    student = result.scalars().first() 
    if student is None: return None

    db.delete(student)
    db.commit()
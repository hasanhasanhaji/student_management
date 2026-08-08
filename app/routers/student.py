from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, func
from math import ceil
from app.database.dependencies import get_db
from app.schemas.student import StudentCreate, StudentResponse, StudentUpdate, StudentListResponse
from app.models.student import Student
from app.services import student_service

# Create router instance for student endpoints
router = APIRouter(
    prefix="/students",
    tags= ["Students"] 
)


# Get all students endpoint
@router.get(
    "/",
    response_model=StudentListResponse
)
def get_students(
    page: int = Query(
        default=1,
        ge=1,
        description="Page number"
    ),
    size: int = Query(
        default=10,
        ge=1,
        le=100,
        description="Number of students per page"
    ),
    name: str | None = Query(
        default=None,
        description="Filter students by exact name"
    ),
    sort_by: str = Query(
        default="id",
        description="Field used for sorting"
    ),
    sort_order: str = Query(
        default="asc",
        description="Sort direction: asc or desc"
    ),
    db: Session = Depends(get_db)
):
    # Calculate pagination offset
    offset = (page - 1) * size

    # Define allowed sorting fields
    allowed_sort_fields = {
        "id": Student.id,
        "name": Student.name,
        "age": Student.age
    }

    # Validate sorting field
    if sort_by not in allowed_sort_fields:
        raise HTTPException(
            status_code=400,
            detail="Invalid sort field"
        )

    # Validate sorting direction
    if sort_order not in {"asc", "desc"}:
        raise HTTPException(
            status_code=400,
            detail="Invalid sort order"
        )

    # Start building the query
    statement = select(Student)

    # Apply filtering
    if name is not None:
        statement = statement.where(
            Student.name == name
        )

    # Apply sorting
    sort_column = allowed_sort_fields[sort_by]

    if sort_order == "asc":
        statement = statement.order_by(
            sort_column.asc()
        )
    else:
        statement = statement.order_by(
            sort_column.desc()
        )

    # Count filtered records
    count_statement = (
        select(func.count())
        .select_from(statement.subquery())
    )

    total = db.scalar(count_statement)

    # Apply pagination
    statement = (
        statement
        .offset(offset)
        .limit(size)
    )

    # Execute query
    result = db.execute(statement)

    # Extract Student objects
    students = result.scalars().all()

    # Calculate number of pages
    pages = ceil(total / size) if total > 0 else 0

    # Return paginated response
    return StudentListResponse(
        items=students,
        total=total,
        page=page,
        size=size,
        pages=pages
    )

# get one student
@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session= Depends(get_db)):
    statement = (
        select(Student).where(Student.id == student_id)
    )
    result = db.execute(statement)
    student = result.scalars().first()

    if student is None:
        raise HTTPException(
            status_code= 404,
            detail= "Student is not found"
        )
    return student

# Create a new student
@router.post( "/", response_model=StudentResponse, status_code=201 ) 
def create_student( student: StudentCreate, db: Session = Depends(get_db) ): 
    new_student = Student( name=student.name, age=student.age, email=student.email ) 
    db.add(new_student) 
    try: 
        db.commit() 
        db.refresh(new_student) 
    except IntegrityError: 
        db.rollback() 
        raise HTTPException( status_code=409, detail="Email already exists" ) 
    return new_student

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
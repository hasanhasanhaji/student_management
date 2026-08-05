from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException


from sqlalchemy.orm import Session


from app.database.database import get_db


from app.schemas.student import (
    StudentCreate,
    StudentResponse,
    StudentUpdate
)


from app.services.student_service import *



router = APIRouter()



@router.post(
    "/students",
    response_model=StudentResponse
)
def create_student(

    student: StudentCreate,

    db: Session = Depends(get_db)

):

    return create_student_service(
        db,
        student
    )





@router.get(
    "/students",
    response_model=list[StudentResponse]
)
def get_students(

    db: Session = Depends(get_db)

):

    return get_students_service(db)





@router.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(

    student_id: int,

    db: Session = Depends(get_db)

):

    student = get_student_service(
        db,
        student_id
    )


    if student is None:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )


    return student





@router.put(
    "/students/{student_id}",
    response_model=StudentResponse
)
def update_student(

    student_id: int,

    student: StudentUpdate,

    db: Session = Depends(get_db)

):

    updated = update_student_service(
        db,
        student_id,
        student
    )


    if updated is None:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )


    return updated





@router.delete(
    "/students/{student_id}"
)
def delete_student(

    student_id:int,

    db: Session = Depends(get_db)

):

    deleted = delete_student_service(
        db,
        student_id
    )


    if deleted is None:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )


    return {

        "message":"Student deleted"

    }
from fastapi import APIRouter

router = APIRouter()

@router.get("/students")
def get_students():
    return {
        "students": [
            {
                "id": 1,
                "name": "Ali"
            },
            {
                "id": 2,
                "name": "Sara"
            }
        ]
    }
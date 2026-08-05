from pydantic import BaseModel, Field

# Define a Pydantic model for creating a new student
class StudentCreate(BaseModel):
    name :str
    age : int
    email : str


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str
    
class StudentUpdate(BaseModel):

    name: str

    age: int

    email: str
    
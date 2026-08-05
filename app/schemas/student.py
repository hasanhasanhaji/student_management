from pydantic import BaseModel, Field

# Define a Pydantic model for creating a new student
class StudentCreate(BaseModel):
    name :str
    age : int
    email : str
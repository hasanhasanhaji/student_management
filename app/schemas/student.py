from pydantic import BaseModel, EmailStr, ConfigDict


# Schema for creating a new student
class StudentCreate(BaseModel):
    name:str
    age: int
    email: EmailStr

# Schema for updating an existing student
class StudentUpdate(BaseModel):
    # Student full name (optional)
    name: str | None = None
    age: int | None = None
    email : EmailStr | None = None


# Schema returned to the client
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr

    # Allow Pydantic to read SQLAlchemy ORM objects
    model_config = ConfigDict(
        from_attributes= True
    )
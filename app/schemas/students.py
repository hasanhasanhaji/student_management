from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    name : str
    age : int = Field(ge=18)
    email: str
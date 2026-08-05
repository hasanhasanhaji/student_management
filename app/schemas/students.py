from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional

class StudentCreate(BaseModel):
   first_name: str = Field(min_length=2, max_length=50)
   last_name: str = Field(min_length=2 , max_length=50)
   email: EmailStr
   age : int = Field(ge=18 ,le=90)
   major : str
   gpa : float = Field(ge=0.0 , le=20.0)
   
class StudentResponse(BaseModel):
   id: int
   first_name: str
   last_name: str
   email: EmailStr
   age : int
   major : str
   gpa : float
   created_at: datetime
   updated_at: datetime
   model_config = ConfigDict(from_attributes=True)

class StudentUpdate(BaseModel):
   first_name : Optional[str] = None
   last_name :  Optional[str] = None
   email :  Optional[EmailStr] = None
   age :  Optional[int] = None
   major :  Optional[str] = None
   gpa:  Optional[float] = None
from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    title:str = Field(min_length= 5)
    author:str
    pages: int = Field(ge=0)
    price : int = Field(ge=0)
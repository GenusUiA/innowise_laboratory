from typing import Optional
from pydantic import BaseModel, Field

# schema for validate books
class BookValid(BaseModel):
    title: str 
    author: str
    year: Optional[int] = Field(None, ge=1, le=9999)
    
#schema for output books
class BookOut(BaseModel):
    id: int
    title: str
    author: str
    year: int | None
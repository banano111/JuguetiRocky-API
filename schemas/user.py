from typing import Optional
from pydantic import BaseModel

class User_Auth(BaseModel):
    email: str
    password: str

class User(BaseModel):
    id: Optional[int]
    name: str
    last_name: str
    email: str
    password: str

    class Config:
        orm_mode=True
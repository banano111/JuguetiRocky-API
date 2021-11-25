from typing import Optional
from pydantic import BaseModel

class Sale(BaseModel):
    sale_id: Optional[int]
    user_id: int
    total_sale: int
    ship_status: str

    class Config:
        orm_mode=True
from pydantic import BaseModel
from typing import Optional

class Service(BaseModel):
    id: Optional[int] = None
    name: str
    unit: str
    price: float

    class Config:
        from_attributes = True
from pydantic import BaseModel
from typing import Optional, List
from core.entities.service import Service

class Work(BaseModel):
    id: Optional[int] = None
    photo_url: Optional[str] = None
    square: float
    price: float
    services: List[Service] = []

    class Config:
        from_attributes = True

class WorkCreate(BaseModel):
    photo_url: Optional[str] = None
    square: float
    price: float
    service_ids: List[int] = []
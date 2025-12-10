from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from .service import Service

class ServiceInWork(Service):
    """Услуга в составе работы с количеством"""
    quantity: float = 1.0

class Work(BaseModel):
    id: Optional[int] = None
    photo_url: Optional[str] = None
    square: float
    price: float
    description: Optional[str] = None
    services: List[ServiceInWork] = []  # список услуг из таблицы services

    model_config = ConfigDict(from_attributes=True)

class WorkCreate(BaseModel):
    photo_url: Optional[str] = None
    square: float
    price: float
    description: Optional[str] = None
    service_ids: List[int] = []  # ID услуг для добавления
    quantities: List[float] = []  # количества для каждой услуги
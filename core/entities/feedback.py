from pydantic import BaseModel
from typing import Optional
from enum import Enum

class RepairStatus(str, Enum):
    NO_REQUEST = "no_request"
    REQUESTED = "requested"
    COMPLETED = "completed"

class Feedback(BaseModel):
    id: Optional[int] = None
    phone_number: str
    had_repair_request: bool
    work_completed: bool
    description: str

    class Config:
        from_attributes = True  # Для совместимости с SQLAlchemy
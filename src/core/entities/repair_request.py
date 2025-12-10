from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class RepairRequest(BaseModel):
    id: Optional[int] = None
    name: str
    phone_number: str
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

# Дополнительная модель для создания (без id и created_at)
class RepairRequestCreate(BaseModel):
    name: str
    phone_number: str
from pydantic import BaseModel, ConfigDict
from typing import Optional

class Service(BaseModel):
    id: Optional[int] = None
    name: str
    unit: str
    price: float

    model_config = ConfigDict(from_attributes=True)
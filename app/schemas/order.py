from uuid import UUID
from typing import Optional
from pydantic import BaseModel, ConfigDict

class OrderBase(BaseModel):
    patient_id: UUID
    item_name: str
    quantity: int = 1
    price: float = 0.0

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    item_name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None

class OrderOut(OrderBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

from uuid import UUID
from typing import Optional
from pydantic import BaseModel, ConfigDict

class InventoryItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int = 0
    price: float = 0.0

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None

class InventoryItemOut(InventoryItemBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

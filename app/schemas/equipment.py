from datetime import date
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, ConfigDict

class EquipmentBase(BaseModel):
    name: str
    purchase_date: Optional[date] = None
    status: Optional[str] = None

class EquipmentCreate(EquipmentBase):
    pass

class EquipmentUpdate(BaseModel):
    name: Optional[str] = None
    purchase_date: Optional[date] = None
    status: Optional[str] = None

class EquipmentOut(EquipmentBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

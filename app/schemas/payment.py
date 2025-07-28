from datetime import date
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, ConfigDict

class PaymentBase(BaseModel):
    patient_id: UUID
    amount: float
    paid_on: Optional[date] = None
    method: Optional[str] = None

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    amount: Optional[float] = None
    paid_on: Optional[date] = None
    method: Optional[str] = None

class PaymentOut(PaymentBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

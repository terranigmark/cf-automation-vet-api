from uuid import UUID
from typing import Optional
from pydantic import BaseModel, ConfigDict

class PrescriptionBase(BaseModel):
    patient_id: UUID
    medication: str
    dosage: Optional[str] = None
    instructions: Optional[str] = None

class PrescriptionCreate(PrescriptionBase):
    pass

class PrescriptionUpdate(BaseModel):
    medication: Optional[str] = None
    dosage: Optional[str] = None
    instructions: Optional[str] = None

class PrescriptionOut(PrescriptionBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

from datetime import date
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, ConfigDict

class PatientHistoryBase(BaseModel):
    patient_id: UUID
    visit_date: Optional[date] = None
    notes: Optional[str] = None

class PatientHistoryCreate(PatientHistoryBase):
    pass

class PatientHistoryUpdate(BaseModel):
    visit_date: Optional[date] = None
    notes: Optional[str] = None

class PatientHistoryOut(PatientHistoryBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

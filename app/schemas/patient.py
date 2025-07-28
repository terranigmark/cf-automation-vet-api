
from datetime import date
from uuid import UUID
from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict


class PatientBase(BaseModel):
    name: str
    species: str
    breed: Optional[str] = None
    sex: Optional[Literal["M", "F", "N", "S"]] = None
    birth_date: Optional[date] = None
    owner_name: Optional[str] = None
    owner_phone: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    breed: Optional[str] = None
    owner_phone: Optional[str] = None

class PatientOut(PatientBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)


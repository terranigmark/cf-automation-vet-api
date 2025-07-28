from datetime import date
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, ConfigDict

class EmployeeBase(BaseModel):
    name: str
    role: str
    hire_date: Optional[date] = None

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    hire_date: Optional[date] = None

class EmployeeOut(EmployeeBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

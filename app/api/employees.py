from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.employee import EmployeeCreate, EmployeeOut, EmployeeUpdate
from app.crud import employees as crud
from app.dependencies import get_db

router = APIRouter(prefix="/employees", tags=["employees"])

@router.post("/", response_model=EmployeeOut, status_code=status.HTTP_201_CREATED)
async def create_employee(payload: EmployeeCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create(db, payload)

@router.get("/{employee_id}", response_model=EmployeeOut)
async def read_employee(employee_id: UUID, db: AsyncSession = Depends(get_db)):
    employee = await crud.get(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.patch("/{employee_id}", response_model=EmployeeOut)
async def update_employee(employee_id: UUID, patch: EmployeeUpdate, db: AsyncSession = Depends(get_db)):
    employee = await crud.update(db, employee_id, patch)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_employee(employee_id: UUID, db: AsyncSession = Depends(get_db)):
    await crud.delete(db, employee_id)

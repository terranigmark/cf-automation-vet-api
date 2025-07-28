from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.equipment import EquipmentCreate, EquipmentOut, EquipmentUpdate
from app.crud import equipment as crud
from app.dependencies import get_db

router = APIRouter(prefix="/equipment", tags=["equipment"])

@router.post("/", response_model=EquipmentOut, status_code=status.HTTP_201_CREATED)
async def create_equipment(payload: EquipmentCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create(db, payload)

@router.get("/{equipment_id}", response_model=EquipmentOut)
async def read_equipment(equipment_id: UUID, db: AsyncSession = Depends(get_db)):
    equipment = await crud.get(db, equipment_id)
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment

@router.patch("/{equipment_id}", response_model=EquipmentOut)
async def update_equipment(equipment_id: UUID, patch: EquipmentUpdate, db: AsyncSession = Depends(get_db)):
    equipment = await crud.update(db, equipment_id, patch)
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment

@router.delete("/{equipment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_equipment(equipment_id: UUID, db: AsyncSession = Depends(get_db)):
    await crud.delete(db, equipment_id)

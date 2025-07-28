from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.patient_history import PatientHistoryCreate, PatientHistoryOut, PatientHistoryUpdate
from app.crud import patient_histories as crud
from app.dependencies import get_db

router = APIRouter(prefix="/histories", tags=["histories"])

@router.post("/", response_model=PatientHistoryOut, status_code=status.HTTP_201_CREATED)
async def create_history(payload: PatientHistoryCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create(db, payload)

@router.get("/{history_id}", response_model=PatientHistoryOut)
async def read_history(history_id: UUID, db: AsyncSession = Depends(get_db)):
    history = await crud.get(db, history_id)
    if not history:
        raise HTTPException(status_code=404, detail="History not found")
    return history

@router.patch("/{history_id}", response_model=PatientHistoryOut)
async def update_history(history_id: UUID, patch: PatientHistoryUpdate, db: AsyncSession = Depends(get_db)):
    history = await crud.update(db, history_id, patch)
    if not history:
        raise HTTPException(status_code=404, detail="History not found")
    return history

@router.delete("/{history_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_history(history_id: UUID, db: AsyncSession = Depends(get_db)):
    await crud.delete(db, history_id)

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.prescription import PrescriptionCreate, PrescriptionOut, PrescriptionUpdate
from app.crud import prescriptions as crud
from app.dependencies import get_db

router = APIRouter(prefix="/prescriptions", tags=["prescriptions"])

@router.post("/", response_model=PrescriptionOut, status_code=status.HTTP_201_CREATED)
async def create_prescription(payload: PrescriptionCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create(db, payload)

@router.get("/{prescription_id}", response_model=PrescriptionOut)
async def read_prescription(prescription_id: UUID, db: AsyncSession = Depends(get_db)):
    prescription = await crud.get(db, prescription_id)
    if not prescription:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return prescription

@router.patch("/{prescription_id}", response_model=PrescriptionOut)
async def update_prescription(prescription_id: UUID, patch: PrescriptionUpdate, db: AsyncSession = Depends(get_db)):
    prescription = await crud.update(db, prescription_id, patch)
    if not prescription:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return prescription

@router.delete("/{prescription_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_prescription(prescription_id: UUID, db: AsyncSession = Depends(get_db)):
    await crud.delete(db, prescription_id)

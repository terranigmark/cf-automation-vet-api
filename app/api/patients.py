
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.patient import PatientCreate, PatientOut, PatientUpdate
from app.crud import patients as crud
from app.dependencies import get_db

router = APIRouter(prefix="/patients", tags=["patients"])

@router.post("/", response_model=PatientOut, status_code=status.HTTP_201_CREATED)
async def create_patient(payload: PatientCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create(db, payload)

@router.get("/{patient_id}", response_model=PatientOut)
async def read_patient(patient_id: UUID, db: AsyncSession = Depends(get_db)):
    patient = await crud.get(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.patch("/{patient_id}", response_model=PatientOut)
async def update_patient(
    patient_id: UUID, patch: PatientUpdate, db: AsyncSession = Depends(get_db)
):
    patient = await crud.update(db, patient_id, patch)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_patient(patient_id: UUID, db: AsyncSession = Depends(get_db)):
    await crud.delete(db, patient_id)

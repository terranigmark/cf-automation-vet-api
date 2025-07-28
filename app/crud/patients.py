
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate

async def create(db: AsyncSession, payload: PatientCreate) -> Patient:
    patient = Patient(**payload.model_dump())
    db.add(patient)
    await db.commit()
    await db.refresh(patient)
    return patient

async def get(db: AsyncSession, patient_id: UUID) -> Patient | None:
    result = await db.execute(select(Patient).where(Patient.id == patient_id))
    return result.scalar_one_or_none()

async def update(db: AsyncSession, patient_id: UUID, patch: PatientUpdate) -> Patient | None:
    patient = await get(db, patient_id)
    if not patient:
        return None
    for k, v in patch.model_dump(exclude_unset=True).items():
        setattr(patient, k, v)
    await db.commit()
    await db.refresh(patient)
    return patient

async def delete(db: AsyncSession, patient_id: UUID) -> None:
    patient = await get(db, patient_id)
    if patient:
        await db.delete(patient)
        await db.commit()

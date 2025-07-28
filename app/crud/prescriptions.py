from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.prescription import Prescription
from app.schemas.prescription import PrescriptionCreate, PrescriptionUpdate

async def create(db: AsyncSession, payload: PrescriptionCreate) -> Prescription:
    prescription = Prescription(**payload.model_dump())
    db.add(prescription)
    await db.commit()
    await db.refresh(prescription)
    return prescription

async def get(db: AsyncSession, prescription_id: UUID) -> Prescription | None:
    result = await db.execute(select(Prescription).where(Prescription.id == prescription_id))
    return result.scalar_one_or_none()

async def update(db: AsyncSession, prescription_id: UUID, patch: PrescriptionUpdate) -> Prescription | None:
    prescription = await get(db, prescription_id)
    if not prescription:
        return None
    for k, v in patch.model_dump(exclude_unset=True).items():
        setattr(prescription, k, v)
    await db.commit()
    await db.refresh(prescription)
    return prescription

async def delete(db: AsyncSession, prescription_id: UUID) -> None:
    prescription = await get(db, prescription_id)
    if prescription:
        await db.delete(prescription)
        await db.commit()

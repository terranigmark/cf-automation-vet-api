from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.patient_history import PatientHistory
from app.schemas.patient_history import PatientHistoryCreate, PatientHistoryUpdate

async def create(db: AsyncSession, payload: PatientHistoryCreate) -> PatientHistory:
    history = PatientHistory(**payload.model_dump())
    db.add(history)
    await db.commit()
    await db.refresh(history)
    return history

async def get(db: AsyncSession, history_id: UUID) -> PatientHistory | None:
    result = await db.execute(select(PatientHistory).where(PatientHistory.id == history_id))
    return result.scalar_one_or_none()

async def update(db: AsyncSession, history_id: UUID, patch: PatientHistoryUpdate) -> PatientHistory | None:
    history = await get(db, history_id)
    if not history:
        return None
    for k, v in patch.model_dump(exclude_unset=True).items():
        setattr(history, k, v)
    await db.commit()
    await db.refresh(history)
    return history

async def delete(db: AsyncSession, history_id: UUID) -> None:
    history = await get(db, history_id)
    if history:
        await db.delete(history)
        await db.commit()

from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.equipment import Equipment
from app.schemas.equipment import EquipmentCreate, EquipmentUpdate

async def create(db: AsyncSession, payload: EquipmentCreate) -> Equipment:
    equipment = Equipment(**payload.model_dump())
    db.add(equipment)
    await db.commit()
    await db.refresh(equipment)
    return equipment

async def get(db: AsyncSession, equipment_id: UUID) -> Equipment | None:
    result = await db.execute(select(Equipment).where(Equipment.id == equipment_id))
    return result.scalar_one_or_none()

async def update(db: AsyncSession, equipment_id: UUID, patch: EquipmentUpdate) -> Equipment | None:
    equipment = await get(db, equipment_id)
    if not equipment:
        return None
    for k, v in patch.model_dump(exclude_unset=True).items():
        setattr(equipment, k, v)
    await db.commit()
    await db.refresh(equipment)
    return equipment

async def delete(db: AsyncSession, equipment_id: UUID) -> None:
    equipment = await get(db, equipment_id)
    if equipment:
        await db.delete(equipment)
        await db.commit()

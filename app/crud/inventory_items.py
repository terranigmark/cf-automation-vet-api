from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.inventory_item import InventoryItem
from app.schemas.inventory_item import InventoryItemCreate, InventoryItemUpdate

async def create(db: AsyncSession, payload: InventoryItemCreate) -> InventoryItem:
    item = InventoryItem(**payload.model_dump())
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item

async def get(db: AsyncSession, item_id: UUID) -> InventoryItem | None:
    result = await db.execute(select(InventoryItem).where(InventoryItem.id == item_id))
    return result.scalar_one_or_none()

async def update(db: AsyncSession, item_id: UUID, patch: InventoryItemUpdate) -> InventoryItem | None:
    item = await get(db, item_id)
    if not item:
        return None
    for k, v in patch.model_dump(exclude_unset=True).items():
        setattr(item, k, v)
    await db.commit()
    await db.refresh(item)
    return item

async def delete(db: AsyncSession, item_id: UUID) -> None:
    item = await get(db, item_id)
    if item:
        await db.delete(item)
        await db.commit()

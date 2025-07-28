from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate

async def create(db: AsyncSession, payload: OrderCreate) -> Order:
    order = Order(**payload.model_dump())
    db.add(order)
    await db.commit()
    await db.refresh(order)
    return order

async def get(db: AsyncSession, order_id: UUID) -> Order | None:
    result = await db.execute(select(Order).where(Order.id == order_id))
    return result.scalar_one_or_none()

async def update(db: AsyncSession, order_id: UUID, patch: OrderUpdate) -> Order | None:
    order = await get(db, order_id)
    if not order:
        return None
    for k, v in patch.model_dump(exclude_unset=True).items():
        setattr(order, k, v)
    await db.commit()
    await db.refresh(order)
    return order

async def delete(db: AsyncSession, order_id: UUID) -> None:
    order = await get(db, order_id)
    if order:
        await db.delete(order)
        await db.commit()

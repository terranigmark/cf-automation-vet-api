from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.payment import Payment
from app.schemas.payment import PaymentCreate, PaymentUpdate

async def create(db: AsyncSession, payload: PaymentCreate) -> Payment:
    payment = Payment(**payload.model_dump())
    db.add(payment)
    await db.commit()
    await db.refresh(payment)
    return payment

async def get(db: AsyncSession, payment_id: UUID) -> Payment | None:
    result = await db.execute(select(Payment).where(Payment.id == payment_id))
    return result.scalar_one_or_none()

async def update(db: AsyncSession, payment_id: UUID, patch: PaymentUpdate) -> Payment | None:
    payment = await get(db, payment_id)
    if not payment:
        return None
    for k, v in patch.model_dump(exclude_unset=True).items():
        setattr(payment, k, v)
    await db.commit()
    await db.refresh(payment)
    return payment

async def delete(db: AsyncSession, payment_id: UUID) -> None:
    payment = await get(db, payment_id)
    if payment:
        await db.delete(payment)
        await db.commit()

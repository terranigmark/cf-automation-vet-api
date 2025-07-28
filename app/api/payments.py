from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.payment import PaymentCreate, PaymentOut, PaymentUpdate
from app.crud import payments as crud
from app.dependencies import get_db

router = APIRouter(prefix="/payments", tags=["payments"])

@router.post("/", response_model=PaymentOut, status_code=status.HTTP_201_CREATED)
async def create_payment(payload: PaymentCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create(db, payload)

@router.get("/{payment_id}", response_model=PaymentOut)
async def read_payment(payment_id: UUID, db: AsyncSession = Depends(get_db)):
    payment = await crud.get(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.patch("/{payment_id}", response_model=PaymentOut)
async def update_payment(payment_id: UUID, patch: PaymentUpdate, db: AsyncSession = Depends(get_db)):
    payment = await crud.update(db, payment_id, patch)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.delete("/{payment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_payment(payment_id: UUID, db: AsyncSession = Depends(get_db)):
    await crud.delete(db, payment_id)

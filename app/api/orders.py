from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.order import OrderCreate, OrderOut, OrderUpdate
from app.crud import orders as crud
from app.dependencies import get_db

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=OrderOut, status_code=status.HTTP_201_CREATED)
async def create_order(payload: OrderCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create(db, payload)

@router.get("/{order_id}", response_model=OrderOut)
async def read_order(order_id: UUID, db: AsyncSession = Depends(get_db)):
    order = await crud.get(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.patch("/{order_id}", response_model=OrderOut)
async def update_order(order_id: UUID, patch: OrderUpdate, db: AsyncSession = Depends(get_db)):
    order = await crud.update(db, order_id, patch)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id: UUID, db: AsyncSession = Depends(get_db)):
    await crud.delete(db, order_id)

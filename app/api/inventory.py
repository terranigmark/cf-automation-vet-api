from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.inventory_item import InventoryItemCreate, InventoryItemOut, InventoryItemUpdate
from app.crud import inventory_items as crud
from app.dependencies import get_db

router = APIRouter(prefix="/inventory", tags=["inventory"])

@router.post("/", response_model=InventoryItemOut, status_code=status.HTTP_201_CREATED)
async def create_item(payload: InventoryItemCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create(db, payload)

@router.get("/{item_id}", response_model=InventoryItemOut)
async def read_item(item_id: UUID, db: AsyncSession = Depends(get_db)):
    item = await crud.get(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.patch("/{item_id}", response_model=InventoryItemOut)
async def update_item(item_id: UUID, patch: InventoryItemUpdate, db: AsyncSession = Depends(get_db)):
    item = await crud.update(db, item_id, patch)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: UUID, db: AsyncSession = Depends(get_db)):
    await crud.delete(db, item_id)

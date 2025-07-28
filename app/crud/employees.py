from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

async def create(db: AsyncSession, payload: EmployeeCreate) -> Employee:
    employee = Employee(**payload.model_dump())
    db.add(employee)
    await db.commit()
    await db.refresh(employee)
    return employee

async def get(db: AsyncSession, employee_id: UUID) -> Employee | None:
    result = await db.execute(select(Employee).where(Employee.id == employee_id))
    return result.scalar_one_or_none()

async def update(db: AsyncSession, employee_id: UUID, patch: EmployeeUpdate) -> Employee | None:
    employee = await get(db, employee_id)
    if not employee:
        return None
    for k, v in patch.model_dump(exclude_unset=True).items():
        setattr(employee, k, v)
    await db.commit()
    await db.refresh(employee)
    return employee

async def delete(db: AsyncSession, employee_id: UUID) -> None:
    employee = await get(db, employee_id)
    if employee:
        await db.delete(employee)
        await db.commit()


from fastapi import FastAPI
from app.api.patients import router as patients_router
from app.api.employees import router as employees_router
from app.api.inventory import router as inventory_router
from app.api.equipment import router as equipment_router
from app.api.prescriptions import router as prescriptions_router
from app.api.histories import router as histories_router
from app.api.payments import router as payments_router
from app.api.orders import router as orders_router

app = FastAPI(title="Veterinary Clinic API", version="0.1.0")

app.include_router(patients_router)
app.include_router(employees_router)
app.include_router(inventory_router)
app.include_router(equipment_router)
app.include_router(prescriptions_router)
app.include_router(histories_router)
app.include_router(payments_router)
app.include_router(orders_router)

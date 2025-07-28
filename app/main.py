
from fastapi import FastAPI
from app.api.patients import router as patients_router

app = FastAPI(title="Veterinary Clinic API", version="0.1.0")

app.include_router(patients_router)

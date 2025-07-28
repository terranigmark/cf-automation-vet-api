import uuid
from sqlalchemy import String, Column, ForeignKey
from app.models import Base, GUID

class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    patient_id = Column(GUID(), ForeignKey("patients.id"), nullable=False)
    medication = Column(String(128), nullable=False)
    dosage = Column(String(64))
    instructions = Column(String(256))

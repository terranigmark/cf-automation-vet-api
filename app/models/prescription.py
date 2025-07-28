import uuid
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.models import Base

class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    medication = Column(String(128), nullable=False)
    dosage = Column(String(64))
    instructions = Column(String(256))

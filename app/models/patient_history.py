import uuid
from sqlalchemy import String, Date, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.models import Base

class PatientHistory(Base):
    __tablename__ = "patient_histories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    visit_date = Column(Date)
    notes = Column(String(256))

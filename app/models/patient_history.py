import uuid
from sqlalchemy import String, Date, Column, ForeignKey
from app.models import Base, GUID

class PatientHistory(Base):
    __tablename__ = "patient_histories"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    patient_id = Column(GUID(), ForeignKey("patients.id"), nullable=False)
    visit_date = Column(Date)
    notes = Column(String(256))

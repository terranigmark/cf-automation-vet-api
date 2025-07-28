import uuid
from sqlalchemy import String, Date, Float, Column, ForeignKey
from app.models import Base, GUID

class Payment(Base):
    __tablename__ = "payments"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    patient_id = Column(GUID(), ForeignKey("patients.id"), nullable=False)
    amount = Column(Float, nullable=False)
    paid_on = Column(Date)
    method = Column(String(64))

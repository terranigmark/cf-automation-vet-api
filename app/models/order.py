import uuid
from sqlalchemy import String, Integer, Float, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.models import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    item_name = Column(String(128), nullable=False)
    quantity = Column(Integer, default=1)
    price = Column(Float, default=0.0)

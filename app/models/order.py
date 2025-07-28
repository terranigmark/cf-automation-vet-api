import uuid
from sqlalchemy import String, Integer, Float, Column, ForeignKey
from app.models import Base, GUID

class Order(Base):
    __tablename__ = "orders"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    patient_id = Column(GUID(), ForeignKey("patients.id"), nullable=False)
    item_name = Column(String(128), nullable=False)
    quantity = Column(Integer, default=1)
    price = Column(Float, default=0.0)

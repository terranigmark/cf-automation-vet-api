import uuid
from sqlalchemy import String, Integer, Float, Column
from app.models import Base, GUID

class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    name = Column(String(128), nullable=False)
    description = Column(String(256))
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0.0)

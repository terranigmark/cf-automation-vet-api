import uuid
from sqlalchemy import String, Date, Column
from app.models import Base, GUID

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    name = Column(String(128), nullable=False)
    purchase_date = Column(Date)
    status = Column(String(64))

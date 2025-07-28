import uuid
from sqlalchemy import String, Date, Column
from sqlalchemy.dialects.postgresql import UUID
from app.models import Base

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(128), nullable=False)
    purchase_date = Column(Date)
    status = Column(String(64))

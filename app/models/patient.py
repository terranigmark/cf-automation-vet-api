
import uuid
from sqlalchemy import String, Date, Column
from sqlalchemy.dialects.postgresql import UUID
from app.models import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(128), nullable=False)
    species = Column(String(64), nullable=False)
    breed = Column(String(128))
    sex = Column(String(2))
    birth_date = Column(Date)
    owner_name = Column(String(128))
    owner_phone = Column(String(32))

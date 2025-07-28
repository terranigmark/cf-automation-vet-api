import uuid
from sqlalchemy import String, Date, Column
from app.models import Base, GUID

class Employee(Base):
    __tablename__ = "employees"

    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    name = Column(String(128), nullable=False)
    role = Column(String(64), nullable=False)
    hire_date = Column(Date)

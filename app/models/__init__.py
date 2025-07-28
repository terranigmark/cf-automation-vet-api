
import uuid
from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import DeclarativeBase


class GUID(TypeDecorator):
    """Platform-independent GUID/UUID type."""

    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == "postgresql":
            return dialect.type_descriptor(postgresql.UUID(as_uuid=True))
        return dialect.type_descriptor(CHAR(36))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        if isinstance(value, uuid.UUID):
            return str(value)
        return str(uuid.UUID(value))

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        return uuid.UUID(str(value))

class Base(DeclarativeBase):
    pass

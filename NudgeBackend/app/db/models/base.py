from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy import (
    DateTime
)
from datetime import datetime 

class Base(AsyncAttrs, DeclarativeBase):
    type_annotation_map = {
        datetime: DateTime(timezone=True)
    }

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'

    def __repr__(self):
        return str(self) 





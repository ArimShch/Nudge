from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import func, Integer
from datetime import datetime 

class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), 
        onupdate=func.now()
    )

class SoftDeleteMixin: 
    deleted_at: Mapped[datetime | None] = mapped_column(
        nullable=True 
    )

class BaseMixin(SoftDeleteMixin, TimestampMixin):
    pass 

class BaseIdMixin(BaseMixin):
    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True, 
        autoincrement=True, 
    )


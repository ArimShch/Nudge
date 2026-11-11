from sqlalchemy import (
    String, Text, ForeignKey, Integer, BigInteger, Boolean, 
    DateTime, func, text, CheckConstraint, Index, and_
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime 
from typing import List, TYPE_CHECKING

from .base import Base 
from .mixins import BaseMixin, BaseIdMixin

if TYPE_CHECKING:
    from .chats import Chat 

class User(BaseMixin, Base):
    __table_args__ = (
        CheckConstraint("role IN ('user', 'admin')", name='ck_user_role'), 
    )

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=False, 
    )
    username: Mapped[str | None] = mapped_column(String(100))
    first_name: Mapped[str | None] = mapped_column(String(100))
    last_name: Mapped[str | None] = mapped_column(String(100))
    role: Mapped[str] = mapped_column(String(20), server_default='user')
    is_premium: Mapped[bool] = mapped_column(
        Boolean, server_default=text('false')
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, server_default=text('true')
    )
    is_blocked: Mapped[bool] = mapped_column(
        Boolean, server_default=text('false')
    )

    chats: Mapped[List["Chat"]] = relationship(
        back_populates='user', lazy='raise', 
    )

    def __str__(self):
        return (
            f'User(id={self.id}, username={self.username}, ' 
            f'first_name={self.first_name}, last_name={self.last_name})'
        )



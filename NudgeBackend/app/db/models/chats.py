from sqlalchemy import (
    Index, text, String, Boolean, BigInteger, ForeignKey, 
    CheckConstraint, 
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime 
from typing import List, TYPE_CHECKING

from .base import Base 
from .mixins import BaseIdMixin

if TYPE_CHECKING:
    from .users import User
    from .messages import Message


class Chat(BaseIdMixin, Base):
    __table_args__ = (
        CheckConstraint(
            'lead_score >= 0 AND lead_score <= 100', 
            name='ck_chat_lead_score'
        ), 
        Index(
            'idx_chat_user_id_and_last_message_at', 
            'user_id', 'last_message_at', 
            postgresql_where=text('deleted_at IS NULL')
        ), 
        Index(
            'idx_chat_next_followup_at', 
            'next_followup_at', 
            postgresql_where=text('deleted_at IS NULL AND next_followup_at IS NOT NULL')
        )
    )

    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, 
    )
    lead_name: Mapped[str | None] = mapped_column(
        String(255), 
    )
    lead_score: Mapped[int | None]
    is_archived: Mapped[bool] = mapped_column(
        Boolean, server_default=text('false'), 
    )
    next_followup_at: Mapped[datetime | None] 
    last_read_at: Mapped[datetime | None]
    last_message_at: Mapped[datetime | None]


    user: Mapped["User"] = relationship(
        back_populates='chats', lazy='raise', 
    )
    messages: Mapped[List["Message"]] = relationship(
        back_populates='chat', lazy='raise',
    )

    def __str__(self):
        return (
            f'Chat(user_id={self.user_id}, lead_name={self.lead_name}, lead_score={self.lead_score}, next_followup_at={self.next_followup_at})'
        )

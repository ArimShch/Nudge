from sqlalchemy import (
    Index, text as sql_text, String, Boolean, ForeignKey, 
    CheckConstraint, Enum as SQLEnum, Text, BigInteger
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime 
from typing import TYPE_CHECKING
from enum import StrEnum

from .base import Base 
from .mixins import BaseIdMixin, BaseMixin

if TYPE_CHECKING:
    from .chats import Chat 


class SenderEnum(StrEnum):
    SYSTEM = 'system'
    BOT = 'bot'
    USER = 'user'


class Message(BaseMixin, Base):
    __table_args__ = (
        CheckConstraint(
            "sender IN ('system', 'bot', 'user')", 
            name='ck_message_sender', 
        ), 
        CheckConstraint(
            'lead_score >= 0 AND lead_score <= 100', 
            name='ck_message_lead_score', 
        ), 
        Index(
            'idx_message_chat_id_and_created_at', 
            'chat_id', 'created_at', 
            postgresql_where=sql_text('deleted_at IS NULL'), 
        )
    )

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=False, 
    )
    chat_id: Mapped[int] = mapped_column(
        ForeignKey('chats.id', ondelete='CASCADE'), nullable=False, 
    )
    sender: Mapped[str] = mapped_column(
        String(20), nullable=False  
    )
    text: Mapped[str | None] = mapped_column(Text)
    options: Mapped[dict | None] = mapped_column(JSONB)
    lead_score: Mapped[int | None]
    tokens: Mapped[int | None]

    chat: Mapped["Chat"] = relationship(
        back_populates='messages', lazy='raise'
    )

    def __str__(self):
        return (
            f'Message(chat_id={self.chat_id}, sender={self.sender}, text={self.text[:50] if self.text else None}, lead_score={self.lead_score}, tokens={self.tokens})'
        )

    
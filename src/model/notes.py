from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from sqlalchemy.exc import DataError
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from src.config.db import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    note_text = Column(String)
    note_type = Column(String, default="text")
    file_id = Column(String, default=None)
    file_type = Column(String)
    chat_id = Column(Integer, ForeignKey("users.chat_id"))
    created_on = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_on = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), server_onupdate=func.now())

    def __repr__(self):
        return f"<Note(id={self.id}, note_text={self.note_text}, note_type={self.note_type}, file_id={self.file_id}, file_type={self.file_type}, chat_id={self.chat_id})>"
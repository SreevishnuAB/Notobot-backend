from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from bot_handler.config.db import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    note_text = Column(String)
    note_type = Column(String, default="text")
    file_id = Column(UUID(as_uuid=True), default=None)
    user_name = Column(String)

    def __repr__(self):
        return f"<Note(id={self.id}, note_text={self.text}, note_type={self.note_type}, file_id={self.file_id}, user_name={self.user})>"
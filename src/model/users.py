from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.sql import func

from src.config.db import Base


class User(Base):
    __tablename__ = "users"

    chat_id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    otp = Column(Integer)
    last_active = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    def __repr(self):
        return f"<User(user_name={self.user_name}, chat_id={self.chat_id}, last_active={self.last_active})>"

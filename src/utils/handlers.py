from sqlalchemy.orm import session
from src.config.db import Session
from src.model.notes import Note


def handle_text_update(text, chat):
    text_note = Note(note_text=text, user_name=chat.username.lower())
    print(text_note)
    session = Session()
    session.add(text_note)
    session.commit()
    session.close()
from src.config.db import Session
from src.model.notes import Note
from src.model.users import User


def handle_start(chat):
    session = Session()
    try:
        user = session.query(User).filter_by(user_name=chat.username.lower())
        print(user.count(), list(user))
        if user.count() != 0:
            return f"You are already registered with me, {chat.first_name}. Tell me what to note!"
        else:
            new_user = User(user_name=chat.username, chat_id=chat.id)
            print(new_user)
            session.add(new_user)
            session.commit()
            return f"Hi {chat.first_name}! You can start sending me notes!"
    except Exception as e:
        print(e)
        return "Oops, someting went wrong!"
    finally:
        session.close()


def handle_text_update(text, chat):
    text_note = Note(note_text=text, chat_id=chat.id)
    print(text_note)
    session = Session()
    session.add(text_note)
    try:
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        session.close()
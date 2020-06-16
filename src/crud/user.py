from src.database.models.user import User  # noqa
from src.database.session import db_session  # noqa
from src.utils.security import hash_pass


def create_user(username, email, password):
    user = User(usuario=username, email=email, hashed_password=hash_pass(password))
    try:
        db_session.add(user)
        db_session.commit()
        db_session.flush()
        return user
    except:
        db_session.rollback()
        return None


def connect_user(username, password):
    user = db_session.query(User).filter(User.usuario == username).first()
    if user and user.check_password(password=password):
        return user
    return None

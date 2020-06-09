from src.config import SUPER_USER_ID
from src.database.models.user import User
from src.database.session import db_session


user = db_session.query(User).filter(User.id == SUPER_USER_ID).first()
print(user)

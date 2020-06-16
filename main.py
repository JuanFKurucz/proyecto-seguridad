import hashlib


from src.config import SUPER_USER_ID  # noqa
from src.database.models.user import User  # noqa
from src.database.session import db_session  # noqa


# user = db_session.query(User).filter(User.id == SUPER_USER_ID).first()


def hash_pass(password):
    return hashlib.sha256(password).hexdigest()


def compare_hash(hash_one, text):
    return hash_one == hash_pass(text)


def encrypt_mail(mail):
    pass


def decrypt_mail(encrypted_mail):
    pass


def encrypt_user(user):
    pass


def decrypt_user(encrypted_user):
    pass


def encrypt_file(file_dir):
    pass


def decrypt_file(encrypted_file):
    pass


def generate_token():
    pass


def send_token(mail):
    pass


def send_key(mail):
    pass


def check_token(token):
    pass


def generate_key():
    pass


def sign_up(user, mail, password):
    pass


def run():
    pass

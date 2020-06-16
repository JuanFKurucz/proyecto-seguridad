import hashlib

from src.utils.config import PASSWORD_SALT


def hash_pass(password):
    hash = hashlib.sha256()
    hash.update(("%s%s" % (PASSWORD_SALT, password)).encode("utf-8"))
    return hash.hexdigest()


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

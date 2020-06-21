import hashlib

from src.utils.config import PASSWORD_SALT


def hash_md5(text):
    hash = hashlib.md5()
    hash.update(f"{text}".encode("utf-8"))
    return hash.hexdigest()


def hash_pass(password):
    hash = hashlib.sha256()
    hash.update(f"{PASSWORD_SALT}{password}".encode("utf-8"))
    return hash.hexdigest()


def compare_hash(hash_one, text):
    return hash_one == hash_pass(text)

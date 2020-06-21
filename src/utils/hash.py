import hashlib

from src.utils.config import PASSWORD_SALT


def hash_pass(password):
    hash = hashlib.sha256()
    hash.update(("%s%s" % (PASSWORD_SALT, password)).encode("utf-8"))
    return hash.hexdigest()


def compare_hash(hash_one, text):
    return hash_one == hash_pass(text)

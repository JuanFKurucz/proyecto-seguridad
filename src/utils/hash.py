import random, string

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


def generate_token():
    return "".join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for _ in range(4)
    )


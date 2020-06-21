import os
import uuid

from sqlalchemy import Column, BigInteger, String, Integer
from sqlalchemy.orm import relationship

from src.database.session import Base

from src.utils.hash import compare_hash, hash_pass
from src.utils.cipher import encrypt_file, decrypt_file

from src.database.models.file import File
from src.utils.hash import hash_md5


class User(Base):
    id = Column(BigInteger, primary_key=True, index=True, default=lambda: uuid.uuid4().hex)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    login_token = Column(String)
    login_token_expiration = Column(Integer)

    files = relationship("File")

    def check_password(self, password):
        return compare_hash(self.hashed_password, self.username, password)

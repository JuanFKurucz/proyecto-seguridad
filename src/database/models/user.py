import uuid

from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship

from src.database.session import Base

from src.utils.hash import compare_hash, hash_pass
from src.utils.cipher import encrypt_file, decrypt_file


class User(Base):
    id = Column(BigInteger, primary_key=True, index=True, default=lambda: uuid.uuid4().hex)
    usuario = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    def check_password(self, password):
        return compare_hash(self.hashed_password, password)

    def get_encryption_key(self):
        return hash_pass(self.usuario + self.email + self.hashed_password)[0:16].encode("utf8")

    def encrypt_file(self, path_in, path_out):
        encrypt_file(self.get_encryption_key(), path_in, path_out)

    def decrypt_file(self, path_in, path_out):
        decrypt_file(self.get_encryption_key(), path_in, path_out)

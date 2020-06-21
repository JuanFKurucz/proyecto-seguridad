import uuid

from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship

from src.database.session import Base

from src.utils.hash import compare_hash


class User(Base):
    id = Column(BigInteger, primary_key=True, index=True, default=lambda: uuid.uuid4().hex)
    usuario = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    def check_password(self, password):
        return compare_hash(self.hashed_password, password)

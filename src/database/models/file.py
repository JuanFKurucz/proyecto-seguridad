import uuid

from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database.session import Base


class File(Base):
    id = Column(BigInteger, primary_key=True, index=True, default=lambda: uuid.uuid4().hex)
    name = Column(String)
    encrypted_file = Column(String)
    nonce = Column(String)
    mac = Column(String)
    user_id = Column(BigInteger, ForeignKey("user.id"))


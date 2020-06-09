from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.orm import relationship

from src.database.session import Base


class User(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    usuario = Column(String)
    email = Column(String)
    hashed_password = Column(String)

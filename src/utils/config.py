import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

PASSWORD_SALT = "123"  # Example, we should change this later
CIPHER_KEY = (
    b"\xb2\xc8\xbf\x15\xbf;\xd4$\xaak\xb1PM|\x19\xb9\xd3C\xd7\xac\xfd|sQC\xd3\xf9;\xee1\xa0\xa7"
)


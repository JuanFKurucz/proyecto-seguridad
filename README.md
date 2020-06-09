# proyecto-seguridad

# Env File

```
DATABASE_URL = "<YOUR DATABASE URL>"
```

File should be named ".env" without quotes

# Database

For now we will be using SQLite, you can set your DATABASE_URL to: "sqlite:///./db.db"

# Running

To run the bot first install the dependencies with

```
pip install -r requirements.txt
alembic upgrade head
```

And run with

```
python main.py
```

@echo off

pip install -r requirements.txt
del *.db
del ./src/database/migrations/versions/*.py
alembic revision --autogenerate
alembic upgrade head
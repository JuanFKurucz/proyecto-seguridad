@echo off

pip install -r requirements.txt
del *.db
alembic upgrade head
from sqlalchemy import text
from src.database import db, DATABASE
from src.models import News


with db.engine.connect() as connection:
    connection.execute(text(f'CREATE DATABASE IF NOT EXISTS {DATABASE}'))


try:
    News().__table__.create(db.engine)
except:
    print('уже создано')

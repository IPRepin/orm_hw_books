import psycopg2
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from config import login, password, conn
from models import create_tables

'''создаем подключение'''
DSN = f'postgresql://{login}:{password}@{conn}/books_db'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

'''Создаем сессию'''
Session = sessionmaker(bind=engine) #переменная для создания сессий
session = Session() #созданная сессия




session.close()
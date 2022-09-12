# per https://sqla-wrapper.scaletti.dev/sqlalchemy-wrapper/
import os
# from sqla_wrapper import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"] 
# db = SQLAlchemy(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

""" db = SQLAlchemy(
    dialect="postgresql",
    user="scott",
    password="tiger",
    host="localhost",
    name="test",
) """

engine = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
Session = sessionmaker(bind=engine)
# conn = engine.connect()
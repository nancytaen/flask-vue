# config = utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://taen:west.tower.805.@localhost:5432/sqlalchemy')

# create a configured "Session" class
Session = sessionmaker(bind=engine)

Base = declarative_base()


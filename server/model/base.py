# config = utf-8
from datetime import datetime

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = ''
engine = create_engine(url, echo=True)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, String, Integer, Date, VARCHAR

from model.base import Base, engine


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(20))
    release_date = Column(Date)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date


class Pet(Base):
    __tablename__ = 'pet'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(20))

    def __init__(self, name):
        self.name = name


meta = Base.metadata
meta.create_all(engine)

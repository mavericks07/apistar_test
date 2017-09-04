import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column


Base = declarative_base()


class User(Base):

    __tablename__ = "User"
    id = Column(sqlalchemy.Integer, primary_key=True)
    username = Column(sqlalchemy.String(64))

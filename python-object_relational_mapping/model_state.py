#!/usr/bin/python3
""" Doc """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()
""" definition of a State and an instance Base = declarative_base(): """


class State(Base):
    """ class state inherits from Base """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
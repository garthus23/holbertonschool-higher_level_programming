#!/usr/bin/python3
"""
    module sys anf mysqld
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""
    class State: it's where we store american states
"""


class State(Base):
    """ class state """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))

    def __repr__(self):
        """ method to convert obj in str """
        return "{}: {}".format(self.id, self.name)

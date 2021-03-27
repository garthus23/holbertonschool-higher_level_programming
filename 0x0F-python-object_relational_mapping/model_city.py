#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State")

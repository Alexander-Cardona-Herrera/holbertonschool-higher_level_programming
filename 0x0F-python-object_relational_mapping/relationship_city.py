#!/usr/bin/python3
""" Creating the class definition of a state """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """Creating state class inherintace of Base"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))

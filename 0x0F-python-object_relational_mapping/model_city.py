#!/usr/bin/python3
"""
That contains the class definition of a City and an instance
Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """ Class State that inherits from Base
    Represens ORM for state
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")

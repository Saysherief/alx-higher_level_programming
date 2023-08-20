#!/usr/bin/python3
"""
That contains the class definition of a State and an instance
Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """ Class State that inherits from Base
    Represens ORM for state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


# Create the engine to connect to the MySQL server
engine = create_engine(
        'mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa'
        )

#!/usr/bin/python3
"""
That creates the State “California” with the City “San Francisco”
from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    # Get MySQL credentials from CLI
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine to connect to the MySQL server
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, database))

    # Bind the engine with the base class
    Base.metadata.bind = engine
    # Create all tables defined in the Base class (State & City)
    Base.metadata.create_all(engine)
    # Create a session factory
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()
    # Create a new State object
    calif = State(name='California')
    # Create the City and associate with above state
    san_f = City(name='San Francisco', state=calif)
    # Add the new object to the session
    session.add_all([calif, san_f])
    # Commit the session to change the database
    session.commit()
    # Close the session
    session.close()

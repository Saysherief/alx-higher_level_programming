#!/usr/bin/python3
"""
That lists all State objects that contain the letter a from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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
    # Create a session factory
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()
    # Perform database operations
    states = session.query(State).filter(
            State.name.like('%a%')
            ).order_by(State.id).all()
    # Display the States containing a
    for state in states:
        print("{}: {}".format(state.id, state.name))
    # Close the session
    session.close()

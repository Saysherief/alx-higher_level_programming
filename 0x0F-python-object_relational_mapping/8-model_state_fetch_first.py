#!/usr/bin/python3
"""
That prints the first State object from the database hbtn_0e_6_usa"""

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
    state = session.query(State).order_by(State.id).first()
    # Display the 1st State
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    # Close the session
    session.close()

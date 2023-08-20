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
    # Find the State object with id=2
    state = session.query(State).filter_by(id=2).first()
    # Change the name if the state with id=2 exists
    if state:
        state.name = "New Mexico"
        # Commit the session to change the database
        session.commit()
    # Close the session
    session.close()

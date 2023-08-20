#!/usr/bin/python3
"""
That deletes all State objects that contain the letter a from the database
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
    # Find the State object containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()
    # Delete the State objects with the above specification
    if states:
        for state in states:
            session.delete(state)
        # Commit the session to change the database
        session.commit()
    # Close the session
    session.close()

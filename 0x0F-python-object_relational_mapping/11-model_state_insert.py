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
    # Create a new State object
    louisiana = State(name="Louisiana")
    # Add the new object to the session
    session.add(louisiana)
    # Commit the session to change the database
    session.commit()
    # Print the id of the new added object
    print(louisiana.id)
    # Close the session
    session.close()

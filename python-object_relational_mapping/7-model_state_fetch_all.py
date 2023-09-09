"""
Script to list all State objects from the hbtn_0e_6_usa database.

This script connects to a MySQL server running on localhost at port 3306
and retrieves a sorted list of State objects from the specified database.

Usage:
    state_listing.py <mysql username> <mysql password> <database name>

Arguments:
    <mysql username>    MySQL username for database connection.
    <mysql password>    MySQL password for the specified username.
    <database name>     Name of the database to connect to.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    List all State objects from the specified MySQL database.

    Args:
        username (str): MySQL username for database connection.
        password (str): MySQL password for the specified username.
        db_name (str): Name of the database to connect to.

    Returns:
        list: A list of State objects sorted by their IDs in ascending order.
    """

    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create a connection to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    # Bind the engine to the Base class to enable declarative classes
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database and list all State objects in asc order by states.id
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
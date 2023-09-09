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


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def get_first_state(username, password, db_name):
    """
    Retrieve and print the first State object from the
    specified MySQL database.

    Args:
        username (str): MySQL username for database connection.
        password (str): MySQL password for the specified username.
        db_name (str): Name of the database to connect to.
    """
    # Create a connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    # Bind the engine to the Base class to enable declarative classes
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database to retrieve first State object in asc. order by states.id
    first_state = session.query(State).order_by(State.id).first()

    # Close the session
    session.close()

    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    get_first_state(username, password, db_name)
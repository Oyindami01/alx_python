"""
A script to list State objects containing the letter 'a'
from our database.

This script uses SQLAlchemy to connect to a MySQL database and
retrieve a list of state objects that contain the letter 'a' in
their name. The results are sorted by their IDs in ascending
order.

Usage:
    state_with_a.py <mysql username> <mysql password> <database name>

Arguments:
    <mysql username>    MySQL username for database connection.
    <mysql password>    MySQL password for the specified username.
    <database name>     Name of the database to connect to.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def list_states_with_a(username, password, db_name):
    """
    List State objects containing the letter 'a' from the
    specified MySQL database.

    Args:
        username (str): MySQL username for database connection.
        password (str): MySQL password for the specified username.
        db_name (str): Name of the database to connect to.
    """
    # Create a connection to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    # Bind the engine to the Base class to enable declarative classes
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database to retrieve State objects containing the letter 'a'
    # and order them by states.id
    states_with_a = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
        .all()
    )

    # Close the session
    session.close()

    # Display the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states_with_a(username, password, db_name)
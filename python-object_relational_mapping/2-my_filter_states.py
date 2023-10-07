"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.

Usage:
    python script.py <username> <password> <database>

This script connects to a MySQL server running on localhost at port 3306.
It retrieves a sorted list of states from the specified database
and displays them.

Arguments:
    <username>: MySQL username.
    <password>: MySQL password.
    <database>: Database name.
"""


import MySQLdb
import sys


def search_states(username, password, database, search_name):
    """
    Searches for and lists states from the hbtn_0e_0_usa database
    that match the given state name.

    Args:
        <username>: MySQL username.
        <password>: MySQL password.
        <database>: Database name.
        <search_name>: State name to search for.
    Returns:
        None
    """
    
    try:
        # Connect to the server using context manager
        with MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306
        ) as connection:
            # Create a cursor that aids interaction with database
            cursor = connection.cursor()
            # Create the SQL query using user input
            query_template = (
                "SELECT * FROM states "
                "WHERE BINARY name = '{}' "
                "ORDER BY states.id ASC"
            ).format(search_name)
            cursor.execute(query_template)
        # Fetch all the rows from the result
        rows = cursor.fetchall()

        # Print results
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> "
              "<state_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        search_states(username, password, database, state_name)

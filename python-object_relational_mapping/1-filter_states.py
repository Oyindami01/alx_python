#!/usr/bin/env python

"""
Script to list all states with a name starting with N (upper N) from
the hbtn_0e_0_usa database.

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


def list_states_with_n(username, password, database):
    """
    Fetches and lists all states with a name starting with N (upper N)
    from the hbtn_0e_0_usa database.

    Args:
        <username>: MySQL username.
        <password>: MySQL password.
        <database>: Database name.
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
            # Create a cursor that aids interaction with the database
            cursor = connection.cursor()
            # Execute the SQL query to retrieve states
            query = (
                "SELECT * FROM states "
                "WHERE BINARY name LIKE 'N%' "
                "ORDER BY states.id ASC"
            )
            cursor.execute(query)
            # Fetch all the rows from the result
            rows = cursor.fetchall()

            # Print results
            for row in rows:
                print(row)
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states_with_n(username, password, database)

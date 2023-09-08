"""
Script to list all states from the hbtn_0e_0_usa database.

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


def list_states(username, password, database):
    """
    Fetches and lists all states from the hbtn_0e_0_usa database

    Args:
        <username>: MySQL username.
        <password>: MySQL password.
        <database>: Database name.
    Returns:
        None
    """

    try:
        # connect to the server using context manager
        with MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306
        )as connection:
            # create a cursor that aids interaction with database
            cursor = connection.cursor()
            # execute th sql query to retrieve states
            query = "SELECT * FROM states ORDER BY states.id ASC"
            cursor.execute(query)
        # fetch all the rows from the result
        rows = cursor.fetchall()

        # print results
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
        list_states(username, password, database)
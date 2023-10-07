"""
Script to list all cities from the hbtn_0e_4_usa database.

Usage:
    python script.py <username> <password> <database>

This script connects to a MySQL server running on localhost at port 3306.
It retrieves a sorted list of cities from the specified database
and displays them along with their state names.

Arguments:
    <username>: MySQL username.
    <password>: MySQL password.
    <database>: Database name.
"""

import MySQLdb
import sys


def list_cities(username, password, database):
    """
    Fetches and lists all cities from the hbtn_0e_4_usa database.

    Args:
        <username>: MySQL username.
        <password>: MySQL password.
        <database>: Database name.
    Returns:
        None
    """
    try:
        # Connect to the server using the context manager
        with MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306
        ) as connection:
            # Create a cursor that aids interaction with the database
            cursor = connection.cursor()
            # Execute the SQL query to retrieve cities along with state names
            query = (
                "SELECT cities.id, cities.name, states.name "
                "FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC"
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
        list_cities(username, password, database)

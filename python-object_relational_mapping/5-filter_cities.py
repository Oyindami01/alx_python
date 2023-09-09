"""
Script to list all cities of a given state from the hbtn_0e_4_usa database.

Usage:
    python script.py <username> <password> <database> <state_name>

This script connects to a MySQL server running on localhost at port 3306.
It retrieves a sorted list of cities of the specified state from the database
and displays them.

Arguments:
    <username>: MySQL username.
    <password>: MySQL password.
    <database>: Database name.
    <state_name>: Name of the state to search for cities.
"""


import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):
    """
    Fetches and lists all cities of the specified state from the
    hbtn_0e_4_usa database.

    Args:
        <username>: MySQL username.
        <password>: MySQL password.
        <database>: Database name.
        <state_name>: Name of the state to search for cities.
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
            # Execute the SQL query to retrieve cities
            query = (
                "SELECT cities.name "
                "FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC"
            )
            cursor.execute(query, (state_name,))
            # Fetch all the rows from the result
            rows = cursor.fetchall()

            # Print results
            city_names = [row[0] for row in rows]
            if city_names:
                print(", ".join(city_names))
            else:
                print()
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
        list_cities_by_state(username, password, database, state_name)
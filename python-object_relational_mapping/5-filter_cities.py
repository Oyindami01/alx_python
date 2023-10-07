import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):
    try:
        # Connect to the MySQL server using the context manager
        with MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306
        ) as connection:
            cursor = connection.cursor()

            # Use a single execute() statement to fetch the results
            query = (
                "SELECT cities.name "
                "FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC"
            )
            cursor.execute(query, (state_name,))

            # Fetch and print the results
            results = cursor.fetchall()
            for row in results:
                print(row[0])
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        list_cities_by_state(username, password, database, state_name)

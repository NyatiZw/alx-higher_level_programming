#!/usr/bin/python3
"""Python Script to list all states from a database"""

import sys
import MySQLdb


def filter_states(mysql_username, mysql_password, database_name):
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8"
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows returned by query
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error in your arguments")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        filter_states(username, password, dbname)

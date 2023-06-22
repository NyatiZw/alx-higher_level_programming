#!/usr/bin/python3
"""Python Script to list all states from a database"""

import sys
import MySQLdb


def safe_filter(mysql_username, mysql_password, database_name, state_name):
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8"
    )

    # Creatsor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    try:
        cursor.execute(query, (state_name,))

        # Fetch all the rows returned by query
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("Error executing the query: ", e)

    # Close the database connection
    cursor.close()
    db.close()


__name__ == "__main__":
    if len(sys.argv) != 5:
        print("Error in your arguments")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state = sys.argv[4]
        safe_filter(username, password, dbname, state)

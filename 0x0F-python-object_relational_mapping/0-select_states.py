#!/usr/bin/python3
#Python Script to list all states from a database


import MySQLdb


def list_states(username, password, dbname):
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname, charset="utf8")


    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows returned by query
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
    print(row)

    # Close the database connection
    cursor.closr()
    db.close()

if __name__ == "__main__":
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    dbname = input("Enter database name: ")
    list_states(username, password, dbname)

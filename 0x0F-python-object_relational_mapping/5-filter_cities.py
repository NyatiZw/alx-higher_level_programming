#!/usr/bin/python3
"""Script to list cities of a specific state from a database """

import sys
import MySQLdb


def list_cities_by_state(mysql_username, mysql_password, database_name, state_name):
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8"
    )

    cursor = db.cursor()
    query = "SELECT * FROM cities WHERE state_name = %s ORDER BY id ASC"

    cursor.execute(query, (state_name))

    row = cursor.fetchall()

    for row in rows:
        print(row)

        cursor.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Error in arguments")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state = sys.argv[4]
        list_cities_by_state(username, password, dbname, state)

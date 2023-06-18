#!/usr/bin/python3

#Python Script to list all states from a database

import MySQLdb
import sys


def list_states(username, password, dbname):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname, charset="utf8")

    try:
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to the MySQL database:", e)

    finally:
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]

        list_states(username, password, dbname)

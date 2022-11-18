#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in 
the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv


def mysqlconnect():
    """ Function for connecting to MySQL database"""
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password='',
        database=argv[3],
        port=3306
        )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = BINARY '{}' \
             ORDER BY states.id ASC".format(argv[4]))

    rows = cursor.fetchall()
    for col in rows:
        print(col)

    db.close()


if __name__ == "__main__":
    mysqlconnect()

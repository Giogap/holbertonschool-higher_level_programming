#!/usr/bin/python3
"""
Write a script that lists
all cities from the database hbtn_0e_4_usa
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

    cursor.execute("SELECT C.id, C.name, S.name \
            FROM states S \
            INNER JOIN cities C \
            ON S.id = C.state_id;")

    rows = cursor.fetchall()
    for col in rows:
        print(col)

    db.close()


if __name__ == "__main__":
    mysqlconnect()

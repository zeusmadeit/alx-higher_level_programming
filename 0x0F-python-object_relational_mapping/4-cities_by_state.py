#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the cities
    from the database.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
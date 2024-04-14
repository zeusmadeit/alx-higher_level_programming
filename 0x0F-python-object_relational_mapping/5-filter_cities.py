#!/usr/bin/python3
"""
This script takes in the name 
of a state as an argument and 
lists all cities of that state, 
using the database hbtn_0e_4_usa
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

    with db.cursor() as cursor:
        cursor.execute("SELECT cities.name FROM cities WHERE states.name = %(state)s JOIN states \
                       ON cities.state_id = states.id ORDER BY cities.id ASC", {"state", argv[4]})
        rows = cursor.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
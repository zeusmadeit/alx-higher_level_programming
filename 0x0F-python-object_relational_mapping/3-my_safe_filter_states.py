#!/usr/bin/python3
"""
This script that takes in arguments and 
displays all values in the states table 
of hbtn_0e_0_usa where name matches the 
argument. But this time, the script is 
safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY %(name)s ORDER BY \
                        states.id ASC", {'name': argv[4]})
    rows = cursor.fetchall()

    for row in rows:
        print(row)
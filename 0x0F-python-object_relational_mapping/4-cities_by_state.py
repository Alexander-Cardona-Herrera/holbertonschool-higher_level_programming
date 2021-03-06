#!/usr/bin/python3
"""
4-cities_by_state file


"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ The file is not executed when imported
    """
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], password=argv[2],
                           db=argv[3], charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM states INNER JOIN \
                cities ON cities.state_id = states.id ORDER BY cities.id")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()

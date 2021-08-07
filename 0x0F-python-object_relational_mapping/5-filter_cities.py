#!/usr/bin/python3
"""


"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], password=argv[2],
                           db=argv[3], charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT cities.name FROM states INNER JOIN \
                cities ON cities.state_id = states.id WHERE states.name = %s", (argv[4], ))

    query_rows = cur.fetchall()

    x = ''
    for row in query_rows:
        print(x, end='')
        print(row[0], end='')
        x = ', '
    print()

    cur.close()
    conn.close()

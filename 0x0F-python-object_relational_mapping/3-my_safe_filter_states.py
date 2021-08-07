#!/usr/bin/python3
"""
3-my_safe_filter_states file


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

    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (argv[4],))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()

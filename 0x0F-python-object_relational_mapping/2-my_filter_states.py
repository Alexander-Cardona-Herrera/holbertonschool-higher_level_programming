#!/usr/bin/python3
"""
2-my_filter_states file


"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ The file is not executed when imported
    """
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2],
                           db=argv[3], charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE '{}' \
                ORDER BY id ASC".format(argv[4]))

    query_rows = cur.fetchall()
    for row in query_rows:
        if (row[1] == argv[4]):
            print(row)

    cur.close()
    conn.close()

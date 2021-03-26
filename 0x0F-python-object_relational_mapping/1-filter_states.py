#!/usr/bin/python3
"""
    module sys anf mysqld
"""
import sys
import MySQLdb

"""
    Retrieve all states name starting with N
"""

if __name__ == "__main__":

    argnum = len(sys.argv)
    if (argnum == 4):
        conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER \
                     BY states.id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()

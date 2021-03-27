#!/usr/bin/python3
"""
    module sys anf mysqld
"""
import sys
import MySQLdb

"""
    Retrieve all states name starting with argv4
"""

if __name__ == "__main__":

    argnum = len(sys.argv)
    if (argnum == 5):
        conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               charset="utf8")
        cur = conn.cursor()
        var = "{}".format(sys.argv[4])
        cur.execute("SELECT * FROM states WHERE name LIKE '%s' ORDER \
                    BY states.id ASC" % (var))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()

#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":

    argnum = len(sys.argv)
    if (argnum == 5):
        conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT cities.name  \
                     FROM cities INNER JOIN states \
                     ON states.id=cities.state_id \
                     WHERE states.name = %(state)s\
                     ORDER BY cities.id ASC", {'state': sys.argv[4]})
        query_rows = cur.fetchall()
        result = " ".join(str(x) for x in query_rows)
        result = result.replace(")", "")
        result = result.replace("(", "")
        result = result.replace("'", "")
        result = result[:-1]
        print(result)
        cur.close()
        conn.close()

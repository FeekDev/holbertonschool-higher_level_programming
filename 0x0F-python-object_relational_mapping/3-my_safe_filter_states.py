#!/usr/bin/python3
"""
this script offering protection
from Python SQL injection
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                    passwd=argv[2], db=argv[3])
    cur = db_connection.cursor()
    cur.execute("""SELECT *
                FROM states\
                WHERE name
                LIKE %(state)s ORDER BY states.id ASC""", {'state': argv[4]})
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db_connection.close()

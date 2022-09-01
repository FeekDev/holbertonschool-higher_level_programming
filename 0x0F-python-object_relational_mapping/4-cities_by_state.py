#!/usr/bin/python3
"""This script inser data in db"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                    passwd=argv[2], db=argv[3])
    cur = db_connection.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states
                ON cities.id = states.id
                ORDER BY cities.id""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db_connection.close()

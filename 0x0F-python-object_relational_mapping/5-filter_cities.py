#!/usr/bin/python3
"""This script inser data in db"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                    passwd=argv[2], db=argv[3])
    cur = db_connection.cursor()
    cur.execute("SELECT cities.name FROM cities WHERE state_id IN\
                (SELECT id FROM states WHERE name LIKE BINARY %s)\
                ORDER BY cities.state_id;", (argv[4], ))
    query_rows = cur.fetchall()
    print(", ".join(city[0] for city in query_rows))
    cur.close()
    db_connection.close()

#!/usr/bin/python3
"""This script inser data in db"""
import MySQLdb
from sys import argv

db_connection = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
cur = db_connection.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db_connection.close()

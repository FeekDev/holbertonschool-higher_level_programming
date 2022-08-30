#!/usr/bin/python3
"""This script inser data in db"""
import MySQLdb
from sys import argv

host = "localhost"
port = 3306
usr = argv[1]
key = argv[2]
dB = argv[3]

db_connection = MySQLdb.connect(host, port=3306, user=usr, password=key, db=dB)
cur = db_connection.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db_connection.close()

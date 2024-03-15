#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves
all rows from the `states` table.
It takes command-line arguments for MySQL username,
password, and database name.
The script connects to a MySQL server running
on localhost at port 3306.
The retrieved rows are displayed in the console.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         password=argv[2], db=argv[3])


cur = db.cursor()
cur.execute("SELECT * FROM states")
rows = cur.fetchall()

for row in rows:
    print(row)

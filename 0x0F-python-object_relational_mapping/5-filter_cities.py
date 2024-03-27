#!/usr/bin/python3

"""This script connects to a MySQL database and retrieves
the names of cities located in a specified state.
It takes command-line arguments for MySQL username, password,
database name, and the name of the state.
The script connects to a MySQL server running on localhost at port 3306.
The retrieved city names are concatenated into a
single string and displayed in the console.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT name"
                " FROM cities"
                " WHERE state_id IN ("
                " SELECT id"
                " FROM states"
                " WHERE name = %s"
                ")"
                " ORDER BY id", (sys.argv[4],))
    rows = cur.fetchall()
    ls = ", ".join([row[0] for row in rows])
    print(ls)
    cur.close()
    db.close()

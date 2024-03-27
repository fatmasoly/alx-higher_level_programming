#!/usr/bin/python3

"""This script connects to a MySQL database and
retrieves rows from the `states` table
where the `name` column matches the provided argument.
It takes command-line arguments for MySQL username, password,
database name, and state name to search for.
The script connects to a MySQL server
running on localhost at port 3306.
The retrieved rows are displayed in the console."""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name"
                " LIKE BINARY '{}' ORDER BY id;".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

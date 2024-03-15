#!/usr/bin/python3

"""This script connects to a MySQL database and
retrieves data from the `cities` and `states` tables.
It performs an inner join operation to retrieve cities
along with their corresponding state names.
The script takes command-line arguments for
MySQL username, password, and database name.
It connects to a MySQL server running on localhost at port 3306.
The retrieved data is displayed in the console.
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
    cur.execute("SELECT 'cities'.'id', 'cities'.'name', 'states'.'name'"
                " FROM cities"
                " JOIN states ON 'cities'.'state_id' = 'states'.'id'"
                " ORDER BY 'cities'.'id'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

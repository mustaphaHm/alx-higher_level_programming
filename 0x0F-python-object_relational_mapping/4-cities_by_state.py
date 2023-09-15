#!/usr/bin/python3
"""Get cities."""
import MySQLdb
import sys


if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    db = MySQLdb.connect(user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities c INNER JOIN states s\
            ON c.state_id = s.id ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

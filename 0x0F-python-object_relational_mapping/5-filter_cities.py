#!/usr/bin/python3
"""Get cities name by state name."""
import MySQLdb
import sys


if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    STATE_NAME = sys.argv[4]

    db = MySQLdb.connect(user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT c.name FROM cities c INNER JOIN states s ON c.state_id\
            = s.id WHERE s.name = %s ORDER BY s.id ASC", (STATE_NAME,))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()

#!/usr/bin/python3
"""Get list of all states where the name starts with N."""
import MySQLdb
import sys


if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    db = MySQLdb.connect(user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name like 'N%' ORDER BY id asc")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

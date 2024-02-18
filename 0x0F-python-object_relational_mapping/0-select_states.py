#!/usr/bin/python3
"""connecting to db"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    con = MySQLdb.connect(host = "localhost",port=3306,user=argv[1],
                        password=argv[2],db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

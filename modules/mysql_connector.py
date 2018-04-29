#!/usr/bin/python3

import json
import MySQLdb
import sys


HOST   = "127.0.0.1"
USER   = "root"
PASSWD = "passroot"

try:
    con = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, charset="utf8", use_unicode=True)
    cur = con.cursor()
except:
    print("\nMySQL connection NOT OK...\n")
    sys.exit()


def get_version():
    query = "SELECT VERSION()"
    cur.execute(query)
    con.commit()
    data = cur.fetchall()
    return "Version: %s" % data


def get_connections():
    query = "SHOW PROCESSLIST"
    cur.execute(query)
    con.commit()
    data = cur.fetchall()
    return "Connections: %s" % json.dumps(data, indent=4)

print(get_connections)

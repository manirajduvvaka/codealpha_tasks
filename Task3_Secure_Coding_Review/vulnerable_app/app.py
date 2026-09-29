# Intentionally vulnerable training example. DO NOT deploy.
import sqlite3, subprocess

DB = "users.db"

def login(username, password):
    conn = sqlite3.connect(DB)
    query = "SELECT id FROM users WHERE username='%s' AND password='%s'" % (username, password)
    return conn.execute(query).fetchone()

def ping_host(host):
    return subprocess.check_output("ping -c 1 " + host, shell=True, text=True)

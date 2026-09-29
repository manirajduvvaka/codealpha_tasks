# Defensive reference implementation.
import sqlite3
import subprocess
import ipaddress

DB = "users.db"

def login(username, password):
    conn = sqlite3.connect(DB)
    query = "SELECT id FROM users WHERE username=? AND password=?"
    return conn.execute(query, (username, password)).fetchone()

def ping_host(host):
    ipaddress.ip_address(host)
    return subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True, text=True, check=False
    )

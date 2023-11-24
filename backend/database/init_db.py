import sqlite3
import os

def check_db(filename):
    return os.path.exists(filename)

db_file = '../dbstorage/database.sqlite'
schema_file = 'init_db.sql'

with open(schema_file, 'r') as rf:
    schema = rf.read()

with sqlite3.connect(db_file) as conn:
    conn.executescript(schema)

import sqlite3

def initialize_db():
    dbname = "database.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = "DROP TABLE IF EXISTS data"
    c.execute(sql)
    sql = "CREATE TABLE data (name text)"
    c.execute(sql)
    conn.close()

def insert_data(data):
    dbname = "database.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = "INSERT INTO data VALUES (\'{}\')".format(data)
    c.execute(sql)
    conn.commit()
    conn.close()

def select_data():
    dbname = "database.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS data (name text)"
    c.execute(sql)
    sql = "SELECT * FROM data"
    ret = ""
    for s in c.execute(sql):
        ret += s[0] + " "
    conn.close()
    return ret

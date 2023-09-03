import sqlite3 as sq


def database():
    with  sq.connect("db/avtoservise.db") as conn:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY, 
                    surname TEXT,
                    username TEXT, 
                    password TEXT)''')
        

import sqlite3

def create_db():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(Cid INTEGER PRIMARY KEY AUTOINCREMENT, Name text, Duration text, Charges text, Description text)")
    con.commit()

create_db()
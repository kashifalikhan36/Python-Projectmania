import sqlite3

con=sqlite3.connect('helo.db')
cur=con.cursor()
# cur.execute("CREATE TABLE book (p_id INTEGER PRIMARY KEY AUTOINCREMENT,TEXT NOT NULL,price REAL,quantity INTEGER)")
# print("ALL DONE")
cur.execute("INSERT INTO book (p_id, TEXT, price, quantity) VALUES (1, 'office', 200, 11)")
con.commit()
print("done")
cur.close()
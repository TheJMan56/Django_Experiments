import sqlite3

conn = sqlite3.connect('Books3.db')
curs = conn.cursor()

curs.execute('SELECT * FROM Books')
rows = curs.fetchall()

print(rows)

for row in rows:
    print(row)
    print(f"Book ID: {row[0]}")
    print(f"Book Title: {row[1]}")
    print(f"Book Author: {row[2]}")
    print(f"Book Publisher: {row[3]}")
    print(f"Book Description: {row[4]}")

conn.close()

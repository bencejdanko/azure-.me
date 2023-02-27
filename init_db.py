import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

with open('schema.sql') as f:
    #executescript() method executes multiple SQL statements at once
    conn.executescript(f.read())

#conn.cursor() creates a cursor object that can execute SQL statements
cur = conn.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Test Post 1', 'This is a test. Only a test.')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Test Post 2', 'This is a test. Only a test.')
            )

conn.commit()
conn.close()
print ("Records created successfully, database closed.")
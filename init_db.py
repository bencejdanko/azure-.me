import sqlite3
from datetime import datetime
import os
import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite

conn = None

try:

    conn = sqlite3.connect('database.db')
    print ("Opened database successfully")

    with open('schema.sql') as f:
        #executescript() method executes multiple SQL statements at once
        conn.executescript(f.read())

    #conn.cursor() creates a cursor object that can execute SQL statements
    cur = conn.cursor()

    title = ""
    content = ""
    date = ""
    timestamp = 0

    for post in os.listdir('templates/posts'):
        title = post.rsplit('.', 1)[0]
        with open('templates/posts/' + post ) as f:
            mk_content = f.read()
            content = markdown.markdown(mk_content, 
                                        extensions=['fenced_code' , 'codehilite'])
            timestamp = os.path.getctime('templates/posts/' + post)
            date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        cur.execute("INSERT INTO posts (title, timestamp, content, date) VALUES (?, ?, ?, ?)",
            (title, timestamp, content, date))
    
    print("Posts added successfully")

except sqlite3.Error as e:
    print ("Error %s:" % e.args[0])
    exit(1)

finally:
    if conn:
        conn.commit()
        conn.close()
        print ("Database closed.")
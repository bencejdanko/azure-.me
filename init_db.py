import sqlite3
from datetime import datetime
import os
import markdown

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
    topics = ""

    for post in os.listdir('templates/posts'):
        title = post.rsplit('.', 1)[0]
        with open('templates/posts/' + post ) as f:
            markdown_content = f.read()
            content = markdown.markdown(markdown_content)
            timestamp = os.path.getmtime('templates/posts/' + post)
            date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        cur.execute("INSERT INTO posts (title, content, date, topics) VALUES (?, ?, ?, ?)",
            (title, content, date, topics))
    
    print("Posts added successfully")

except sqlite3.Error as e:
    print ("Error %s:" % e.args[0])
    exit(1)

finally:
    if conn:
        conn.commit()
        conn.close()
        print ("Database closed.")
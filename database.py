import sqlite3

conn = sqlite3.connect('blog.db')
print('connected to blog.db')

conn.execute('CREATE TABLE IF NOT EXISTS post (title TEXT, date TEXT, summary TEXT, content TEXT)')
print('post table created')

conn.close()
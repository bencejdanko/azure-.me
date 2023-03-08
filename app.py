import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app)

@app.route('/')
@app.route('/index')
def index():
   conn = sqlite3.connect('database.db')
   conn.row_factory = sqlite3.Row

   #q: how can I extract from the database by timestamp?
   #a: https://stackoverflow.com/questions/1011431/how-do-i-sort-a-sqlite3-query-by-date
   posts = conn.execute('SELECT * FROM posts ORDER BY timestamp').fetchall()
   conn.close()
   return render_template('index.html', posts=posts)

if __name__ == '__main__':
   #app.run('0.0.0.0', debug=True, port=8100, ssl_context=('adhoc'))
   app.run()
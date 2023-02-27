from datetime import datetime
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app)

def get_db_connection():
   conn = sqlite3.connect('database.db')
   #sqlite3.Row tells the connection to return rows that behave like dicts
   conn.row_factory = sqlite3.Row
   return conn

@app.route('/')
@app.route('/index')
def index():

   conn = get_db_connection()
   #fetchall() method fetches all (remaining) rows of a query result
   posts = conn.execute('SELECT * FROM posts').fetchall()
   conn.close()

   return render_template('index.html', posts=posts)

if __name__ == '__main__':
   app.run('0.0.0.0', debug=True, port=8100, ssl_context=('adhoc'))
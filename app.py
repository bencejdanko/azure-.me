import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_talisman import Talisman
import markdown
import markdown.extensions.fenced_code

app = Flask(__name__)
Talisman(app)

@app.route('/')
@app.route('/index')
def index():
   conn = sqlite3.connect('database.db')
   conn.row_factory = sqlite3.Row
   posts = conn.execute('SELECT * FROM posts ORDER BY timestamp DESC').fetchall()
   conn.close()
   return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
   conn = sqlite3.connect('database.db')
   conn.row_factory = sqlite3.Row
   post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
   conn.close()
   return render_template('post.html', post=post)

if __name__ == '__main__':
   app.run('0.0.0.0', debug=True, port=8100, ssl_context=('adhoc'))
   #app.run()
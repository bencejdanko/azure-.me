from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_talisman import Talisman
from os import listdir as ls

app = Flask(__name__)
Talisman(app)

@app.route('/')
@app.route('/index')
def index():

   return render_template('index.html')

@app.route('/blog')
def blog():
   posts = ls('templates/posts')
   return render_template('blog.html', posts=posts)

if __name__ == '__main__':
   app.run('0.0.0.0', debug=True, port=8100, ssl_context=('adhoc'))
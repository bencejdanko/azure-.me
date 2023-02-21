from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_talisman import Talisman

app = Flask(__name__, template_folder='templates', static_folder='static')
Talisman(app)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('/templates/index.html')

@app.route('/blog')
def blog():
   print('Request for blog page received')
   return render_template('/templates/blog.html')

if __name__ == '__main__':
   app.run()
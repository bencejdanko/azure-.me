from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

if __name__ == '__main__':
   app.run()
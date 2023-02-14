from datetime import datetime
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.before_request
def before_request():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

   

if __name__ == '__main__':
   app.run()
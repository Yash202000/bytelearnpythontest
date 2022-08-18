import string
from flask import Flask,render_template,request
import datetime
import os

app = Flask(__name__)


@app.route('/')
def slash():
    return 'hello world'

@app.route('/time')
def currtime():
    return str(datetime.datetime.now())

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

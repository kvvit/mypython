from collections import namedtuple

from flask import Flask, render_template

app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []

# https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/main')
def main():
    return render_template('main.html', messages=messages)

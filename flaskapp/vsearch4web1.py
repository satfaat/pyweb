from flask import Flask
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'from Flask'

@app.route('/search5')
def do_search() -> str:
    return str(search4letters('life, the univers'))

app.run()
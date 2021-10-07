from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'
    
    
@app.route('/sobre')
def sobre():
    return '<h1>Melhor site do mundo</h1>'

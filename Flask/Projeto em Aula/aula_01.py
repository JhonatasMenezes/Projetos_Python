from flask import Flask

app = Flask(__name__)

@app.route('/')
def raiz():
    return 'Olá Mundo!'
    
@app.route('/rota2')
def rota2():
    return '<h1>Olá Mundo! Segunda rota!</h1>'

app.run()

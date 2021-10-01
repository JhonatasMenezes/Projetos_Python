import requests

def dolar():
    api = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    cotacao = api.json()
    return cotacao['USDBRL']['bid']

def euro():
    api = requests.get('https://economia.awesomeapi.com.br/last/EUR-BRL')
    cotacao = api.json()
    return cotacao['EURBRL']['bid']

def bitcoin():
    api = requests.get('https://economia.awesomeapi.com.br/last/BTC-BRL')
    cotacao = api.json()
    retorno = cotacao['BTCBRL']['ask']
    return retorno
    
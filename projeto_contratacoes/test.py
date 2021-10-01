import datetime
from dateutil.relativedelta import relativedelta

def idade(dataNasc:str):
    """
    Função que determina a idade em anos, à partir de uma data informada.
    
    :param dataNasc: uma data no formato DD/MM/AAAA
    """
    # dividir as informações em uma lista
    dataNasc = dataNasc.split('/')
    # transformar os dados em uma data
    data = datetime.date(int(dataNasc[2]),int(dataNasc[1]),int(dataNasc[0]))
    # pegar data atual
    atual = datetime.datetime.utcnow()
    atual = atual.date()
    # calcular diferença de anos entre as datas
    idade = relativedelta(atual, data)
    idade = idade.years
    return idade

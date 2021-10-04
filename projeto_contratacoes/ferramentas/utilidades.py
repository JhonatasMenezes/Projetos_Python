import os
import time
from dateutil.relativedelta import relativedelta
import datetime

"""
Módulo que criei com algumas funcionalidades úteis no dia a dia.
Contém funções de textos coloridos no terminal, uma função de menu 
e uma função que calcula a idade conforme a data de nascimento e a data atual.
"""

def mensagemTopo(mensagem, inicio=False, tamanho=35):
    """
    Função que gera um cabeçalho formatado e dependendo do parâmetro 'inicio',
    limpa as informações anteriores do terminal, para uma melhor apresentação.
    
    :param mensagem: mensagem a ser exibida no cabeçalho
    :param inicio: limpa as informações anteriores do terminal 
    """
    if inicio == True:
        os.system('cls')
    mensagem = str(mensagem)
    linhaUnica(tamanho)
    print(mensagem.center(tamanho))
    linhaUnica(tamanho)
    
    
def linhaUnica(tamanho=35):
    """
    Exibe uma linha com o tamanho especificado (35 por padrão) no terminal.
    
    :param tamanho: quantidade de caracteres 
    """
    print('-'*tamanho)
        

def textoCor(texto,cor=37,end=False, retorno=False):
    """
    Função que muda a cor de um texto a ser exibido no terminal
    e que pode, ou não, subistituir o comando print() dentro do programa.
    
    :param texto: texto a ser exibido
    :param cor: cor do texto de acordo com tabela ANSI
    :param end: utiliza o padrão do comando print(), mas pode ser alterado em parâmetro
    :param retorno: quando True, retorna uma string e não um comando print().
    """
    if end == False:
        if retorno == True:
            return f'\033[0;{cor}m{texto}\033[m'
        else:
            print(f'\033[0;{cor}m{texto}\033[m')
    else:
        if retorno == True:
            return f'\033[0;{cor}m{texto}\033[m'
        else:
            print(f'\033[0;{cor}m{texto}\033[m', end=end)


def menu(opcoes:list, principal=False):
    """
    Função que gera um menu com tratamento de erros para opções inválidas.
    Recebe lista com opções em formato string e gera os números das opções
    de acordo com sua posição na lista.
    
    :param opcoes: lista com opções em forma de strings
    :param principal: se True, retorna 'MENU PRINCIPAL' invés de apenas 'MENU'
    :return resposta: retorna a opção desejada em formato int
    """
    if not principal:
        menu = 'MENU'
    else:
        menu = 'MENU PRINCIPAL'
    
    while True:
        os.system('cls')
        print('-'*35)
        print(menu.center(35))
        print('-'*35)
        for i in range(0, len(opcoes)):
            textoCor(f'{i+1} - ', 33,end=''),textoCor(f'{opcoes[i]}', 34)
        linhaUnica(35)
        try:
            resposta = int(input(textoCor('Sua opção: ',33,retorno=True)))
            return resposta
        except ValueError:
            print('ERRO: Opção Inválida! Digite uma opção válida!')
            time.sleep(2)
            pass
        except KeyboardInterrupt:
            print('ERRO: Entrada inválida ou vazia!')


def idade(dataNasc:str):
    """
    Função que determina a idade em anos, à partir de uma data informada 
    no formato string.
    
    :param dataNasc: uma data no formato 'DD/MM/AAAA'
    :return idade: retorna a idade calculada em forma de int
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
    return int(idade)

def carragando():
    string = '........'
    string = string.strip()
    print('Carregando', end=' ')
    for c in string:
        print(c, end=' ')
        time.sleep(0.3)
        

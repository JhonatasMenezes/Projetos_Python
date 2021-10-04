import os
from .create_db import Candidatos, Vagas

"""
Módulo criado para permitir a vizualização dos dados das tabelas e
tornar o programa principal mais interativo e completo.
"""


def consultaTabela(todos=False,id=1,tabela='Candidatos'):
    """
    Função que efetua uma busca na tabela passada por parâmetro e
    retorna os dados formatados no terminal.
    
    :param todos: no caso de True, retorna todos os registros da tabela
    :param id: necessário para mostrar uma linha específica
    :param tabela: recebe o nome da tabela a ser buscada
    """
    # Consulta de todos os dados da tabela
    if not todos:
        if tabela == 'Candidatos':
            consulta = Candidatos.select().where(Candidatos.id==id)
            os.system("cls")
            print('Id  |    Nome    | Sobrenome  |      CPF      |  Data Nasc.  | Idade | Maior | Vaga')
            print('-'*90)
            for row in consulta:
                print(str(row.id).center(3),'|',str(row.nome).center(10),'|',str(row.sobrenome).center(10),'|',str(row.CPF).center(13),'|',str(row.data_nascimento).center(12),'|',str(row.idade).center(5),'|',str(row.maior).center(5),'|',str(row.vaga).center(5))
        elif tabela == 'Vagas':
            consulta = Vagas.select().where(Vagas.id==id)
            os.system('cls')
            print('Id |  Vaga')
            print('-'*20)
            for dado in consulta:
                print(dado.id,' | ',dado.vaga)
   
    # Consulta de uma linha específica
    else:
        if tabela == 'Candidatos':
            os.system("cls")
            consulta = Candidatos.select()
            print('Id  |     Nome     |  Sobrenome   |      CPF      |  Data Nasc.  | Idade | Maior | Vaga')
            print('-'*90)
            for row in consulta:
                print(str(row.id).center(3),'|',str(row.nome).center(12),'|',str(row.sobrenome).center(12),'|',str(row.CPF).center(13),'|',str(row.data_nascimento).center(12),'|',str(row.idade).center(5),'|',str(row.maior).center(5),'|',str(row.vaga).center(5))
        elif tabela == 'Vagas':
            os.system('cls')
            consulta = Vagas.select()
            print('Id |  Vaga')
            print('-'*20)
            for dado in consulta:
                print(dado.id,' | ',dado.vaga)

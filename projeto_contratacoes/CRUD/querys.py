import os
from CRUD.create_db import Candidatos, Vagas, db

def consultaTabela(todos=False,id=1,tabela='Candidatos'):
    if not todos:
        if tabela == 'Candidatos':
            consulta = Candidatos.select().where(Candidatos.id==id)
            os.system("cls")
            print('Id  |    Nome    | Sobrenome  |      CPF      |  Data Nasc.  | Idade | Vaga')
            print('-'*75)
            for row in consulta:
                print(str(row.id).center(3),'|',str(row.nome).center(10),'|',str(row.sobrenome).center(10),'|',str(row.CPF).center(13),'|',str(row.data_nascimento).center(12),'|',str(row.idade).center(5),'|',str(row.vaga).center(5))
        elif tabela == 'Vagas':
            consulta = Vagas.select().where(Vagas.id==id)
            os.system('cls')
            print('Id |  Vaga')
            print('-'*20)
            for dado in consulta:
                print(dado.id,' | ',dado.vaga)
    else:
        if tabela == 'Candidatos':
            os.system("cls")
            consulta = Candidatos.select()
            print('Id  |    Nome    | Sobrenome  |      CPF      |  Data Nasc.  | Idade | Vaga')
            print('-'*75)
            for row in consulta:
                print(str(row.id).center(3),'|',str(row.nome).center(10),'|',str(row.sobrenome).center(10),'|',str(row.CPF).center(13),'|',str(row.data_nascimento).center(12),'|',str(row.idade).center(5),'|',str(row.vaga).center(5))
        elif tabela == 'Vagas':
            os.system('cls')
            consulta = Vagas.select()
            print('Id |  Vaga')
            print('-'*20)
            for dado in consulta:
                print(dado.id,' | ',dado.vaga)

consultaTabela(tabela='Vagas')
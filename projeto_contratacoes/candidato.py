from ferramentas.utilidades import idade, mensagemTopo
from ferramentas.manipulacao_dados import *
from ferramentas.create_db import Candidatos
 
"""
Criada a classe Candidato para receber os dados do candidato
no momento de cadastro e possibilitar a persistência dos dados
no Banco de Dados.
"""

class Candidato:
    # Atributos
    def __init__(self, pessoa:dict):
        self.dados = {}
        self.dados['nome'] = pessoa['nome']
        self.dados['sobrenome'] = pessoa['sobrenome']
        self.dados['CPF'] = pessoa['CPF']
        self.dados['dataNascimento'] = pessoa['dataNascimento']
        self.addIdade()
        self.dados['vaga'] = pessoa['vaga']
    
    def retornarDados(self):
        return self.dados
    # Função que irá calcular a idade
    def addIdade(self):
        self.dados['idade'] = idade(self.dados['dataNascimento'])
        
        
    def dadosCandidato(self):
        mensagemTopo(f"Esses são os dados de {self.dados['nome']}", inicio=True, tamanho=((6*17)-2))
        for k in self.dados.keys():
            print(f"{k}".center(14),'|',end=' ')
        print('\n','-'*((6*17)-2))
        for v in self.dados.values():
            print(f"{v}".center(14),'|',end=' ')
        print('\n','-'*((6*17)-2))
    
    def inserirDados(self):
        inserir(self.dados,tabela='Candidato')

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
    
    # Função que retorna os dados em forma de dicionário para 
    # permitir que mais de 1 candidato seja adicionado de 1 só vez
    def retornarDados(self):
        return self.dados
        
    # Função que irá calcular a idade e se a pessoa é maior ou não
    def addIdade(self):
        self.dados['idade'] = idade(self.dados['dataNascimento'])
        if self.dados['idade'] >= 18:
            self.dados['maior'] = 'S'
        else:
            self.dados['maior'] = 'N'
        
    # Função que mostra todos os dados dos candidatos, usei ela 
    # para mostrar os dados antes da confirmação SALVAR
    def dadosCandidato(self,inicio=True):
        mensagemTopo(f"Esses são os dados de {self.dados['nome']}", inicio=inicio, tamanho=((6*17)-2))
        for k in self.dados.keys():
            print(f"{k}".center(12),'|',end=' ')
        print('\n','-'*((6*18)-2))
        for v in self.dados.values():
            print(f"{v}".center(12),'|',end=' ')
        print('\n','-'*((6*18)-2))
    
    # No caso de apenas 1 candidato, a classe possúi essa função 
    # que permite já inserir os dados no BD.
    def inserirDados(self):
        inserir(self.dados,tabela='Candidatos')


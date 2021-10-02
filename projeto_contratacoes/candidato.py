from ferramentas.utilidades import idade, mensagemTopo
from CRUD.manipulacao_dados import *
 


class Candidato:
    def __init__(self, pessoa:dict):
        self.dados = {}
        self.dados['nome'] = pessoa['nome']
        self.dados['sobrenomenome'] = pessoa['sobrenome']
        self.dados['CPF'] = pessoa['CPF']
        self.dados['dataNascimento'] = pessoa['dataNascimento']
        self.dados['vaga'] = pessoa['vaga']

    
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
    
    def inserirDados(self, *pessoas:dict):
        
    
    
    
    
pessoa = {
    'nome': 'Jhonatas',
    'sobrenome': 'Menezes',
    'CPF': '46681125859',
    'dataNascimento': '12/02/1997',
    'vaga': 'Programador'    
}

candidato = Candidato(pessoa)
candidato.addIdade()
candidato.dadosCandidato()

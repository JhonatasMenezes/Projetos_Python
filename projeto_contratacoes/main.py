from ferramentas.create_db import *
from ferramentas.manipulacao_dados import *   
from ferramentas.querys import *
from ferramentas.utilidades import *
from ferramentas.validaDado import *
from time import sleep
import os
from candidato import Candidato


"""
Inicio o programa principal importando todas as funções que criei e libs que irei utilizar.
No caso, uso as libs 'os' e 'time' para melhorar a interação geral com o usuário
que irá utilizar o programa, permitindo pausas e limpeza de dados desnecessários
do terminal no momento da utiliação.
"""


# Definindo os layouts dos menus usados 
menuPrincipal = ['Cadastrar novo candidato', 'Cadastrar nova vaga', 
                'Vizualizar candidatos', 'Vizualizar vagas', 'Sair']
menuVizualizarCandidatos = ['Ver todos os candidatos', 'Ver candidato específico','Voltar']
menuVizualizarVagas = ['Ver todas as vagas', 'Ver vaga específica', 'Voltar']

# No caso de o BD ainda não existir, já será criado junto com as tabelas
# e se já existir, apenas ira conectar no mesmo
criarTabela()

# Mensagem de abertura para mostrar que o programa está iniciando
os.system('cls')  
mensagemTopo(textoCor('INICIANDO PROGRAMA DE CONTRATAÇÕES',cor=36,retorno=True), inicio=True, tamanho=40)
sleep(2)
carragando()

# Coloquei todo o funcionamento em um loop para permitir a execução de várias
# ações de uma vez só, sem precisar executar o programa novamente a todo instante
while True:
    # variáveis suporte para a adição de candidatos
    pessoa = {}
    pessoas = []
    # menu principal
    opcao = menu(menuPrincipal,principal=True)
    # Opção 5 SAIR
    if opcao == 5:
        textoCor('Você escolheu sair! Até mais...', 31)
        sleep(2)
        break
    # 1 Inserção de novos candidatos
    elif opcao == 1:
        # Opção que permite adicionar quantos candidatos desejar
        numCandidatos = int(input('Quantos candidatos deseja inserir? '))
        if numCandidatos == 1:
            os.system('cls')
            print('Dados do candidato')
            linhaUnica()
            # Chamando todas as validações no momento da inserção de dados
            pessoa['nome'] = validaNome()
            pessoa['sobrenome'] = validaNome(mensagem='Sobrenome: ')
            pessoa['CPF'] = validaCPF()
            pessoa['dataNascimento'] = validaNascimento()
            pessoa['vaga'] = validaVaga()
            pessoa = Candidato(pessoa)
            os.system('cls')
            # Vizalização dos dados e opção de salvar ou não, caso aviste algum erro
            pessoa.dadosCandidato()
            salvar = str(input('Deseja salvar os dados inseridos? [S/N] ')).upper()
            if salvar == 'N':
                textoCor('Apagando dados...',31)
                sleep(3)
                pass
            elif salvar == 'S':
                pessoa.inserirDados()
                textoCor('Retornando ao menu...')
                sleep(3)
            else:
                textoCor('Opção inválida! Dados Apagados!',31)
                sleep(3)
        else:
            for num in range(0, numCandidatos):
                os.system('cls')
                print(f'Dados do candidato {num+1}')
                linhaUnica()
                pessoa['nome'] = validaNome()
                pessoa['sobrenome'] = validaNome(mensagem='Sobrenome: ')
                pessoa['CPF'] = validaCPF()
                pessoa['dataNascimento'] = validaNascimento()
                pessoa['vaga'] = validaVaga()
                pessoas.append(Candidato(pessoa).retornarDados())
                os.system('cls')
            for num in range(0, len(pessoas)):
                cada = Candidato(pessoas[num])
                cada.dadosCandidato(inicio=False)
            salvar = str(input('Deseja salvar os dados inseridos? [S/N] ')).upper()
            if salvar == 'N':
                textoCor('Apagando dados...',31)
                pass
            elif salvar == 'S':
                inserir(pessoas,tabela='Candidatos')
                textoCor('Retornando ao menu...')
                sleep(3)
            else:
                textoCor('Opção inválida! Dados Apagados!',31)
                sleep(3)
    
    # 2 Inserção de novas Vagas    
    elif opcao == 2:
        os.system('cls')
        print('Inserir vaga')
        linhaUnica()
        # Validações
        vaga = str(input('Digite o nome da vaga: '))
        validar = validaVaga(inserir=True, vagaNome=vaga)
        if validar == True:
            textoCor('Vaga já existe! Retornando ao menu!',31)
            sleep(3)
        else:
            inserir(vaga,tabela='Vagas')
            textoCor('Retornando ao menu...')
            sleep(3)
    # 3 Vizualização da tabela Candidatos    
    elif opcao == 3:
        # Submenu que permite vizualizar 1 ou todos os candidatos e voltar 
        while True:
            opcao3 = menu(menuVizualizarCandidatos)
            if opcao3 == 1:
                consultaTabela(todos=True)
                linhaUnica(90)
                sair = input('Pressione enter para voltar')
            if opcao3 == 2:
                idCandidato = int(input('Digite o ID do candidato: '))
                consultaTabela(id=idCandidato)
                sair = input('Pressione enter para voltar')
            if opcao3 == 3:
                break
    
    # 4 Vizualização de Vagas
    elif opcao == 4:
        # Submenu que permite vizualizar 1 ou todas as vaga e voltar 
        while True:
            opcao3 = menu(menuVizualizarVagas)
            if opcao3 == 1:
                consultaTabela(todos=True, tabela='Vagas')
                linhaUnica(20)
                sair = input('Pressione enter para voltar')
            if opcao3 == 2:
                idVaga = int(input('Digite o ID da vaga: '))
                consultaTabela(id=idVaga,tabela='Vagas')
                linhaUnica(20)
                sair = input('Pressione enter para voltar')
            if opcao3 == 3:
                break
    


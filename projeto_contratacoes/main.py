from ferramentas.create_db import *
from ferramentas.manipulacao_dados import *   
from ferramentas.querys import *
from ferramentas.utilidades import *
from ferramentas.validaDado import *
from time import sleep
import os
from candidato import Candidato

menuPrincipal = ['Cadastrar novo candidato', 'Cadastrar nova vaga', 
                'Vizualizar candidatos', 'Vizualizar vagas', 'Sair']
menuVizualizarCandidatos = ['Ver todos os candidatos', 'Ver candidato específico','Voltar']
menuVizualizarVagas = ['Ver todas as vagas', 'Ver vaga específica', 'Voltar']

criarTabela()

os.system('cls')  
mensagemTopo(textoCor('INICIANDO PROGRAMA DE CONTRATAÇÕES',cor=36,retorno=True), inicio=True, tamanho=40)
sleep(2)
carragando()


while True:
    pessoa = {}
    pessoas = []
    opcao = menu(menuPrincipal,principal=True)
    if opcao == 5:
        textoCor('Você escolheu sair! Até mais...', 31)
        sleep(2)
        break
    elif opcao == 1:
        numCandidatos = int(input('Quantos candidatos deseja inserir? '))
        if numCandidatos == 1:
            os.system('cls')
            print('Dados do candidato')
            linhaUnica()
            pessoa['nome'] = validaNome()
            pessoa['sobrenome'] = validaNome(mensagem='Sobrenome: ')
            pessoa['CPF'] = validaCPF()
            pessoa['dataNascimento'] = validaNascimento()
            pessoa['vaga'] = validaVaga()
            pessoa = Candidato(pessoa)
            os.system('cls')
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
        
    elif opcao == 2:
        os.system('cls')
        print('Inserir vaga')
        linhaUnica()
        vaga = str(input('Digite o nome da vaga: '))
        validar = validaVaga(inserir=True, vagaNome=vaga)
        if validar == True:
            textoCor('Vaga já existe! Retornando ao menu!',31)
            sleep(3)
        else:
            inserir(vaga,tabela='Vagas')
            textoCor('Retornando ao menu...')
            sleep(3)
        
    elif opcao == 3:
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
    elif opcao == 4:
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
    


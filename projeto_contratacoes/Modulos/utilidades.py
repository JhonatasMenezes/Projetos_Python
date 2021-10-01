import os
import time

def mensagemTopo(mensagem, inicio=False):
    if inicio == True:
        os.system('cls')
    mensagem = str(mensagem)
    linhaUnica()
    print(mensagem.center(35))
    linhaUnica()
    
    
def linhaUnica(tamanho=35):
    print('-'*tamanho)
        

def textoCor(texto,cor=37,end=False, retorno=False):
    if end == False:
        if retorno == True:
            return f'\033[0;{cor}m{texto}\033[m'
        else:
            print(f'\033[0;{cor}m{texto}\033[m')
    else:
        print(f'\033[0;{cor}m{texto}\033[m',end=end)


def menuPrincipal(opcoes):
    while True:
        print('-'*35)
        print('MENU PRINCIPAL'.center(35))
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

def menuSimples(opcoes):
    while True:
        print('-'*35)
        print('MENU'.center(35))
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

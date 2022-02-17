# Libs necessárias
import sys
import time
import os


class Ferramentas:
    """
    Conjunto de 'ferramentas' úteis para o desenvolvimento do projeto e funções
    que utilizo muitas vezes no código, evitando hardcode.
    """
    def carragando(self):
        """
        Função que retorna uma pequena "animação" que simula
        o carregamento do sistema. Fiz para parecer mais agradável
        ao usuário. :)
        """
        string = '. . . . . . . . . .'
        string = string.split()
        print('Carregando', end=' ')
        for c in string:
            time.sleep(0.3)
            print(c, end=' ', flush=True)


    
    def mensagemTopo(self, mensagem, inicio=False, tamanho=35):
        """
        Função que gera um cabeçalho formatado e dependendo do parâmetro 'inicio',
        limpa as informações anteriores do terminal, para uma melhor apresentação.
        
        :param mensagem: mensagem a ser exibida no cabeçalho
        :param inicio: limpa as informações anteriores do terminal 
        """
        if inicio == True:
            os.system('cls')
        mensagem = str(mensagem)
        self.linhaUnica(tamanho)
        print(mensagem.center(tamanho))
        self.linhaUnica(tamanho)


    def linhaUnica(self, tamanho=35):
        """
        Exibe uma linha com o tamanho especificado (35 por padrão) no terminal.
        
        :param tamanho: quantidade de caracteres 
        """
        print('-'*tamanho)


    def textoCor(self, texto,cor=37, end=False, retorno=False):
        """
        Função que muda a cor de um texto a ser exibido no terminal
        e que pode, ou não, subistituir o comando print() dentro do programa.
        
        :param texto: texto a ser exibido.
        :param cor: cor do texto de acordo com tabela ANSI.
        :param end: utiliza o padrão do comando print(), mas pode ser alterado em parâmetro.
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


    def linhaUnica(self,tamanho=35):
        """
        Exibe uma linha com o tamanho especificado (35 por padrão) no terminal.
        
        :param tamanho: quantidade de caracteres.
        """
        print('-'*tamanho)

    
    def finalizar_execucao(self, confirmar=False):
        """
        Finaliza a execução do programa e limpa o terminal.
        """

        if not confirmar:
            self.textoCor('Você escolheu sair. Até logo!', 33)
            time.sleep(3)
            os.system('cls')
            sys.exit()
        else:
            resposta = self.input_str('Deseja salvar antes de sair? [ S / N ] ')
            if resposta.upper() == 'N':
                self.textoCor('Você escolheu sair. Até logo!', 33)
                time.sleep(3)
                os.system('cls')
                sys.exit()
            elif resposta.upper() == 'S':
                return False
            else:
                self.textoCor('Opção inválida. Tente novamente!', 31)
                time.sleep(3)

    def menu(self, opcoes:list, principal=False):
        """
        Função que gera um menu com tratamento de erros para opções inválidas.
        Recebe lista com opções em formato string e gera os números das opções
        de acordo com sua posição na lista.
        
        :param opcoes: lista com opções em forma de strings.
        :param principal: se True, retorna 'MENU PRINCIPAL' invés de apenas 'MENU'.
        :return resposta: retorna a opção desejada em formato int.
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
                self.textoCor(f'{i+1} - ', 33,end=''),self.textoCor(f'{opcoes[i]}', 34)
            self.linhaUnica(35)
            try:
                resposta = int(input(self.textoCor('Sua opção: ',33,retorno=True)))
                return resposta
            except ValueError:
                print('ERRO: Opção Inválida! Digite uma opção válida!')
                time.sleep(2)
                pass
            except KeyboardInterrupt:
                print('ERRO: Entrada inválida ou vazia!')


    def input_float(self, mensagem):
        """
        Recebe uma entrada do usuário já tratando os erros.
        
        :param mensagem: string de saída no terminal.
        """
        try:
            entrada = float(input(mensagem))
            return entrada
        except ValueError:
            self.textoCor('Valor inválido! Tente novamente.', 31)
        except KeyboardInterrupt:
            self.textoCor('\nInterrompido pelo usuário.', 33)
        except:
            self.textoCor('\nAlgo deu errado. Operação não realizada!', 31)
    
    
    def input_int(self, mensagem):
        """
        Recebe uma entrada do usuário já tratando os erros.
        
        :param mensagem: string de saída no terminal.
        """
        try:
            entrada = int(input(mensagem))
            return entrada
        except ValueError:
            self.textoCor('Valor inválido! Tente novamente.', 31)
        except KeyboardInterrupt:
            self.textoCor('\nInterrompido pelo usuário.', 33)
        except:
            self.textoCor('\nAlgo deu errado. Operação não realizada!', 31)
    
    
    def input_str(self, mensagem):
        """
        Recebe uma entrada do usuário já tratando os erros.
        
        :param mensagem: string de saída no terminal.
        """
        try:
            entrada = str(input(mensagem))
            if entrada.isnumeric():
                raise ValueError
            return entrada                
        except ValueError:
            self.textoCor('ValKeyboardInterruptor inválido! Tente novamente.', 31)
        except KeyboardInterrupt:
            self.textoCor('\nInterrompido pelo usuário.', 33)
        except:
            self.textoCor('\nAlgo deu errado. Operação não realizada!', 31)


    def manipular_arquivo(self, dicionario, nome_arquivo='default.txt', modo='r'):
        """
        Manipula um arquivo podendo ler ou escrever no mesmo.

        :param *args: recebe lista de valores para escrita.
        :param nome_arquivo: recebe o nome do arquivo no caso de escrita.
        :param modo: modo de abertura do arquivo.
        """
        try:
            with open(nome_arquivo, modo, encoding='utf-8') as file:
                if modo == 'r':
                    file.readlines()
                elif modo in ('w','a'):
                    for key, value in dicionario.items():
                        file.write(f'{key}: {value}\n')
                    file.write('=-'*30+'\n')
                else:
                    self.textoCor('Modo inválido. Tente novamente!', 31)
            self.textoCor('Salvo com sucesso!', 32)
            time.sleep(3)
        except FileNotFoundError:
            self.textoCor('Arquivo NÂO ENCONTRADO!', 31)
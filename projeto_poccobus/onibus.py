import os
import time
from datetime import datetime
from ferramentas import Ferramentas


class Onibus:
    """
    Responsável por todos os atributos e métodos relacionados exclusivamente
    ao Ônibus representado no programa. Gerar os assentos, ocupar algum assento,
    cancelar uma reserva de assento, entre outros, são alguns dos
    métodos presentes nesta calsse.
    """
    def __init__(self, lugares=40):
        self.colunas = 5
        self.linhas = int(lugares/self.colunas)
        self.assentos = self.gerar_assentos()
        self.vendidos = []
        self.tools = Ferramentas()


    def gerar_assentos(self):
        """ 
        Retorna uma matriz preenchida com posições representando
        assentos de um ônibus.

        :return -> list: 
        """
        letras = [''] + list(map(chr, range(65,80)))
        assentos = []

        for i in range(self.linhas):
            linha = []
            for y in range(self.colunas):
                linha.append(letras[i] + (str(i)+str(y+1)))
            linha[2] = '   '
            assentos.append(linha)
        assentos[0][0] = 'MOT'

        for i in assentos[0]:
            if i != 'MOT':
                assentos[0][assentos[0].index(i)] = '   '
        return assentos


    def ocupar_assento(self, id_assento):
        """
        Substitui o valor de uma posição da variável 'self.assentos'
        conforme a identificação passada em parâmetro.

        :param id_assento -> str: identificação do assento através de string
        """
        try:
            if self.linhas == 40:
                if len(id_assento) >= 4 or len(id_assento) <= 2:
                    raise Exception
            elif self.linhas == 80:
                if len(id_assento) >= 5 or len(id_assento) <= 2:
                    raise Exception
        except Exception:
            self.tools.textoCor('Código inválido. Tente novamente!', 31)

        try:
            for i in range(len(self.assentos)):
                for y in range(len(self.assentos[i])):
                    if self.assentos[i][y] == id_assento:
                        self.assentos[i][y] = ' X '
                        self.vendidos.append(id_assento)
                        return True
            raise Exception 
        except Exception:
            self.tools.textoCor('Assento ocupado ou não localizado!', 31)
                    

    def devolucao(self, assento):
        """
        Efetua o cancelamento na reserva do assento e
        possibilita a devolução do diheiro.

        :param assento -> str: recebe o id do assento.
        """
        try:
            if assento in self.vendidos:            
                c = int(assento[-1])
                l = int(assento[1])
                if len(assento) > 3:
                    l = int(assento[1:3])
                if self.assentos[l][c-1] == ' X ':
                    self.assentos[l][c-1] = assento
                self.tools.textoCor('Reserva cancelada com sucesso!', 33)
                time.sleep(3)
                self.vendidos.remove(assento)
                return True
            else:
                raise Exception
        except Exception:
            self.tools.textoCor('Assento não vendido ou inválido!', 31)
            time.sleep(3)
            return False
        

    def mostrar_assentos(self):
        """ 
        Mostra os assentos em disposição tabular no 
        terminal de saída. 
        """
        if len(self.assentos) == 8:
            os.system('cls')
            for i in self.assentos:
                for y in i:
                    if y == ' X ':
                        print(self.tools.textoCor(y,31,retorno=True), end=' | ')
                    else:
                        print(self.tools.textoCor(y,32,retorno=True), end=' | ')
                print(' ')
        elif len(self.assentos) == 16:
            os.system('cls')
            for i in range(8):
                for y in range(len(self.assentos[i])):
                    if self.assentos[i][y] == ' X ':
                        print(self.tools.textoCor(self.assentos[i][y],31,retorno=True).center(5), end=' | ')
                    else:
                        print(self.tools.textoCor(self.assentos[i][y],32,retorno=True).center(5), end=' | ')
                print('       ', end='')
                for y in range(len(self.assentos[i])):
                    if self.assentos[i+8][y] == ' X ':
                        print(self.tools.textoCor(self.assentos[i+8][y],31,retorno=True).center(5), end=' | ')
                    else:
                        print(self.tools.textoCor(self.assentos[i+8][y],32,retorno=True).center(5), end=' | ')
                print(' ')


    def gerar_relatório(self):
        """
        Escreve os dados da instância atual da classe no
        documento 'Relatório_passagens.txt' no mode 'a' (append),
        gerando assim uma espécie de log de compras e reservas.
        """
        if self.linhas == 16:
            tipo_onibus = 'Ônibus 2 andares'
        elif self.linhas == 8:
            tipo_onibus = 'Ônibus padrão'
        disponiveis = [ assento for fileira in self.assentos[1:-1] for assento in fileira if assento != ' X ' or assento != '   ' ]
        relatorio  = {
            'Disponiveis': disponiveis,
            'Vendidos': self.vendidos,
            'Qtd_vendidos': len(self.vendidos),
            'Qtd_livres': len(disponiveis),
            'Tipo_onibus': tipo_onibus,
            'Data': datetime.today()
        }
        self.tools.manipular_arquivo(relatorio, 'Relatório_passagens.txt', 'a')


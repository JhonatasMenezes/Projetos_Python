import time

from ferramentas import Ferramentas
from onibus import Onibus


class Interacao:
    """
    Classe responsável por executar toda a interação com o usuário.
    """
    def __init__(self):
        self.tools = Ferramentas()
        self.onibus_padrao = Onibus()
        self.onibus_2_andares = Onibus(80)
        self.menu_compra_opcoes = ['Vizualizar assentos', 'Escolher assento', 'Voltar', 'Sair']
        self.menu_cancelar_opcoes = ['Digitar código de assento (Ônibus padrão)',
                                    'Digitar código de assento (Ônibus 2 andares)', 'Voltar', 'Sair']
        self.menu_andares_opcoes = ['Ônibus padrão', 'Ônibus 2 andares', 'Voltar', 'Sair']
        self.menu_consulta_opcoes = ['Digitar código de assento (Ônibus padrão)',
                                     'Digitar código de assento (Ônibus 2 andares)', 'Voltar', 'Sair']
        self.menu_principal_opcoes = ['Comprar passagem', 'Cancelar viagem', 
                                      'Consultar reserva', 'Salvar','Sair']


    def menu_compra(self, tipo_onibus):
        while True:
            opcao_compra = self.tools.menu(self.menu_compra_opcoes)
            if opcao_compra == 4:
                if not self.tools.finalizar_execucao(confirmar=True):
                    self.onibus_padrao.gerar_relatório()
                    self.onibus_2_andares.gerar_relatório()
                    self.tools.finalizar_execucao()
            elif opcao_compra == 3:
                break
            elif opcao_compra == 1:
                tipo_onibus.mostrar_assentos()
                input('Digite ENTER para retornar ')
                continue
            elif opcao_compra == 2:
                tipo_onibus.mostrar_assentos()
                self.tools.linhaUnica()
                assento = self.tools.input_str('Digite o código do assento escolhido: ')
                tipo_onibus.ocupar_assento(assento)
                self.tools.carragando()
                tipo_onibus.mostrar_assentos()
                self.tools.linhaUnica()
                self.tools.textoCor(f'Assento {assento} RESERVADO com sucesso!', 32)
                self.tools.linhaUnica()
                input('Digite ENTER para retornar ')
                continue
    

    def menu_cancelar(self):
        while True:
            opcao_cancelar = self.tools.menu(self.menu_cancelar_opcoes)
            if opcao_cancelar == 4:
                if not self.tools.finalizar_execucao(confirmar=True):
                    self.onibus_padrao.gerar_relatório()
                    self.onibus_2_andares.gerar_relatório()
                    self.tools.finalizar_execucao()  
            elif opcao_cancelar == 3:
                break
            elif opcao_cancelar == 1:
                assento = self.tools.input_str('Digite o código do assento: ')
                if not self.onibus_padrao.devolucao(assento):
                    continue
                else:
                    self.onibus_padrao.mostrar_assentos()
                    input('Digite ENTER para retornar ')
                    continue
            elif opcao_cancelar == 2:
                assento = self.tools.input_str('Digite o código do assento: ')
                if not self.onibus_2_andares.devolucao(assento):
                    continue
                else:
                    self.onibus_2_andares.mostrar_assentos()
                    input('Digite ENTER para retornar ')
                    continue

    def menu_andares(self):
        while True:
            opcao_andares = self.tools.menu(self.menu_andares_opcoes)
            if opcao_andares == 4:
                if not self.tools.finalizar_execucao(confirmar=True):
                    self.onibus_padrao.gerar_relatório()
                    self.onibus_2_andares.gerar_relatório()
                    self.tools.finalizar_execucao()  
            elif opcao_andares == 3:
                break
            elif opcao_andares == 1:
                self.menu_compra(self.onibus_padrao)
            elif opcao_andares == 2:
                self.menu_compra(self.onibus_2_andares)
    
    def menu_consulta(self):
        while True:
            opcao_consulta = self.tools.menu(self.menu_consulta_opcoes)
            if opcao_consulta == 4:
                if not self.tools.finalizar_execucao(confirmar=True):
                    self.onibus_padrao.gerar_relatório()
                    self.onibus_2_andares.gerar_relatório()
                    self.tools.finalizar_execucao()  
            elif opcao_consulta == 3:
                break
            elif opcao_consulta == 1:
                assento = self.tools.input_str('Digite o código do assento: ')
                if assento in (self.onibus_padrao.vendidos):
                    self.tools.textoCor('Reserva ATIVA!', 33)
                    time.sleep(3)
                    input('Digite ENTER para retornar')
                    continue
                else:
                    self.tools.textoCor('Reserva NÃO ENCONTRADA!', 31)
                    time.sleep(3)
                    input('Digite ENTER para retornar')
                    continue
            elif opcao_consulta == 2:
                assento = self.tools.input_str('Digite o código do assento: ')
                if assento in (self.onibus_2_andares.vendidos):
                    self.tools.textoCor('Reserva ATIVA!', 33)
                    time.sleep(3)
                    input('Digite ENTER para retornar')
                    continue
                else:
                    self.tools.textoCor('Reserva NÃO ENCONTRADA!', 31)
                    time.sleep(3)
                    input('Digite ENTER para retornar')
                    continue

    def menu_principal(self):
        while True:
            opcao_inicio = self.tools.menu(self.menu_principal_opcoes,principal=True)
            if opcao_inicio == 5:
                if not self.tools.finalizar_execucao(confirmar=True):
                    self.onibus_padrao.gerar_relatório()
                    self.onibus_2_andares.gerar_relatório()
                    self.tools.finalizar_execucao()             
            elif opcao_inicio == 4:
                self.onibus_padrao.gerar_relatório()
                self.onibus_2_andares.gerar_relatório()
            elif opcao_inicio == 1:
                self.menu_andares()
            elif opcao_inicio == 2:
                self.menu_cancelar()
            elif opcao_inicio == 3:
                self.menu_consulta()
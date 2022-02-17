import os
from time import sleep
from ferramentas import Ferramentas
from interacao import Interacao


class App:
    """
    Classe geradora da aplicação, responsável por chamar as funções bases
    para toda a execução necessária.
    """
    def __init__(self) -> None:
        self.tools = Ferramentas()
        self.interacao = Interacao()

    def executar(self):
        """
        Inicia o programa e chama a função de menu principal
        que está ligado a todos os outros menus na classe interação.
        """
        os.system('cls')  
        self.tools.mensagemTopo(self.tools.textoCor('INICIANDO PROGRAMA DE VIAGENS',cor=36,retorno=True), inicio=True, tamanho=40)
        sleep(2)
        self.tools.carragando()
        self.interacao.menu_principal()


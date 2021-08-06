# importando as libs
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

#criando classe para window
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #setando o título
        self.setWindowTitle('@JhonatasMenezes')
        
        #setando dimensões da janela
        self.setGeometry(100, 100, 450, 350)
        
        #chamando o método
        self.UiComponents()
        
        #abrindo os widgets 
        self.show()

    #método para os componentes    
    def UiComponents(self):
        
        #criando um objeto QCalenderWidget
        calender = QCalendarWidget(self)
        
        #stando a dimensão do calendário
        calender.setGeometry(10, 10, 420, 250)
        
        #criando um botão e definindo a dimensão dele
        push = QPushButton("Next Year", self)
        push.setGeometry(160, 280, 120, 40)
        
        #adiconando a ação de push
        push.clicked.connect(lambda: do_action())

        def do_action():
            #mostrar o próximo ano
            calender.showNextYear()

#criar um app PyQt5            
App = QApplication(sys.argv)

#criar a instância da sua janela
window = Window()  

#startar o app
sys.exit(App.exec())

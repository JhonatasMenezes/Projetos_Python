from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('@JhonatasMenezes')
        self.setGeometry(100, 100, 450, 350)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        calender = QCalendarWidget(self)
        calender.setGeometry(10, 10, 420, 250)
        push = QPushButton("Next Year", self)
        push.setGeometry(160, 280, 120, 40)
        push.clicked.connect(lambda: do_action())

        def do_action():
            calender.showNextYear()

App = QApplication(sys.argv)

window = Window()  

sys.exit(App.exec())
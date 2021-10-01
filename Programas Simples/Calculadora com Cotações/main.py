import PySimpleGUI.PySimpleGUI as sg
import layout as lay
import os
import time

layout = lay.layout
menu_layout = lay.menu_layout

# tema da janela
sg.theme('Reddit')

class App:    
    def __init__(self) -> None:
        self.janela = sg.Window('Calculadora Invest', layout, size=(280,450), return_keyboard_events=False)
        self.result = 0
        self.janela.read(timeout=5)
        self.numEvento = {'zero':0, 'um':1, 'dois':2, 'tres':3, 'quatro':4, 'cinco':5,
                          'seis':6, 'sete':7, 'oito':8, 'nove':9,'virgula':','}
        self.operEvento = {'somar':'+', 'subtrair':'-', 'multiplicar':'x', 'dividir':'/','porcentagem':'%','potencia':'^'}
        
    
    def sair(self):
        os._exit()
    
    
    def about(self):
        sg.popup('Sobre','Para mais informações, acesse o link:','github.com/JhonatasMenezes')
    
    
    def resultado(self,oper,val1,val2):
        if oper == '+':
            return float(val1) + float(val2)
        if oper == '-':
            return float(val1) - float(val2)
        if oper == '/':
            return float(float(val1) / float(val2))
        if oper == 'x':
            return float(val1) * float(val2)
        if oper == '%':
            val1 = float(val1)
            return float(val1/100) * float(val2)
        if oper == '^':
            val1 = float(val1)
            val2 = int(val2)
            exp = val1
            for cont in range(1, val2):
                val1 *= exp
            return val1
        
            
    def start(self):
        while True:
            evento, self.valores = self.janela.read()
            
            if evento in (None, 'Exit', sg.WIN_CLOSED):
                break
            
            if evento in ('Sobre'):
                self.about()
            
            if evento in ('Sair'):
                self.sair()
            
            if evento in self.numEvento.keys():
                self.janela['entrada'].update(value=self.valores['entrada'] + str(self.numEvento[evento]))
            
            if evento in ('clear'):
                self.janela['entrada'].update(value='')
            
            if evento in ('backspace'):
                self.janela['entrada'].update(value=self.valores['entrada'][:-1])
            
            if evento in self.operEvento.keys():
                eventoLocal = self.operEvento[evento]
                val1 = self.valores['entrada']
                self.janela['entrada'].update(value='')
                while True:
                    evento, valores = self.janela.read()
                    if evento in self.numEvento.keys():
                        self.janela['entrada'].update(value=valores['entrada'] + str(self.numEvento[evento]))
                    elif evento == 'igual':
                        val2 = valores['entrada']
                        break
                self.result = self.resultado(eventoLocal,val1,val2)
                self.janela['entrada'].update(value=self.result)
    
calculadora = App()
calculadora.start()         

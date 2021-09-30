import PySimpleGUI.PySimpleGUI as sg
from modulos.moedas_cotacao import *
import os
import time

# pegando cotações
cotacoes = [str(dolar()),
            str(euro()),
            str(bitcoin())]

# tema da janela
sg.theme('Reddit')
#layout do menu
menu_layout = [['Arquivo',['Salvar', 'Sair']], 
               ['Ajuda', ['Sobre']]]
# layout da janela toda
layout = [
    # layout menu
    [sg.Menu(menu_layout)],
    # visor de entrada e respostas
    [sg.Input(key='entrada',size=(25,3), background_color='gray',font=('Arial 22'))],
    # cotações das moedas
    [sg.Text(text='Cotação Dólar    R$',font=('Arial 12')),sg.Text(text=cotacoes[0],font=('Arial 12'))],
    [sg.Text(text='Cotação Euro     R$',font=('Arial 12')),sg.Text(text=cotacoes[1],font=('Arial 12'))],
    [sg.Text(text='Cotação Bitcoin  R$',font=('Arial 12')),sg.Text(text=cotacoes[2],font=('Arial 12'))],
    # primeira linha de botões
    [sg.Button('/',size=(3,1),font=('Arial 20'),key='dividir'), 
        sg.Button('x',size=(3,1),font=('Arial 20'),key='multiplicar'), 
        sg.Button('-',size=(3,1),font=('Arial 20'),key='subtrair'), 
        sg.Button('+',size=(3,1),font=('Arial 20'),key='somar')],
    # segunda linha de botões
    [sg.Button('7',size=(3,1),font=('Arial 20'),key='sete'), 
        sg.Button('8',size=(3,1),font=('Arial 20'),key='oito'), 
        sg.Button('9',size=(3,1),font=('Arial 20'),key='nove'), 
        sg.Button('%',size=(3,1),font=('Arial 20'),key='porcentagem')],
    # terceira linha de botões
    [sg.Button('4',size=(3,1),font=('Arial 20'),key='quatro'), 
        sg.Button('5',size=(3,1),font=('Arial 20'),key='cinco'), 
        sg.Button('6',size=(3,1),font=('Arial 20'),key='seis'), 
        sg.Button('C',size=(3,1),font=('Arial 20'),key='clear')],
    # quarta linha de botões
    [sg.Button('1',size=(3,1),font=('Arial 20'),key='um'), 
        sg.Button('2',size=(3,1),font=('Arial 20'),key='dois'), 
        sg.Button('3',size=(3,1),font=('Arial 20'),key='tres'), 
        sg.Button('<<',size=(3,1),font=('Arial 20'),key='backspace')],
    # quinta linha de botões
    [sg.Button('^',size=(3,1),font=('Arial 20'),key='potencia'), 
        sg.Button('0',size=(3,1),font=('Arial 20'),key='zero'), 
        sg.Button(',',size=(3,1),font=('Arial 20'),key='virgula'), 
        sg.Button('=',size=(3,1),font=('Arial 20'),key='igual')]
]

class App():    
    def __init__(self) -> None:
        self.janela = sg.Window('Calculadora Invest',
                                layout, 
                                size=(280,450),
                                resizable=True,
                                return_keyboard_events=False,
                                finalize=True)
        self.result = 0
        self.janela.read(timeout=5)
        self.numEvento = {'zero':0, 'um':1, 'dois':2, 'tres':3, 'quatro':4, 'cinco':5, 'seis':6, 'sete':7, 'oito':8, 'nove':9,'virgula':','}
        self.operEvento = {'somar':'+', 'subtrair':'-', 'multiplicar':'x', 'dividir':'/','porcentagem':'%','potencia':'^'}
        
    # for i in range(0, 4):
    #     for button in layout[i]:
    #         button.expand(expand_x=True,expand_y=True)
    
    def about(self):
        sg.popup('Sobre', 
                 'Para mais informações, acesse o link:',
                 'github.com/JhonatasMenezes')
    
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
            
            
            
            
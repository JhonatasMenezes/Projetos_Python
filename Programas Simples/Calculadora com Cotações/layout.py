from PySimpleGUI import PySimpleGUI as sg
from modulos.moedas_cotacao import *

sg.theme("Reddit")
# pegando cotações
cotacoes = [str(dolar()),
            str(euro()),
            str(bitcoin())]

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
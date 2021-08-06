import tkinter as tk
import requests as rq
from bs4 import BeautifulSoup

search = 'Weather in São Bernardo do Campo'
url = f'https://www.google.com/search?&q={search}'

r = rq.get(url)
s = BeautifulSoup(r.text,'html.parser')
update = s.find('div',class_='BNeawe').text

class MinhaGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.minsize(60,50)
        self.main_window.title('Wheater Today!')
        self.label1 = tk.Label(self.main_window,text= '   Olá Jhonatas, essa é previsão do tempo hoje!   ')
        self.label2 = tk.Label(self.main_window,text= update)
        self.label1.pack()
        self.label2.pack()
        tk.mainloop()
        
minha_gui = MinhaGUI()

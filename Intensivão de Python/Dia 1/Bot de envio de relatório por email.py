import pyautogui 
import time
import pyperclip
import pandas as pd

pyautogui.PAUSE = 1
#Passo 1
#Abrir uma noa aba
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')
#Entrar no link do sistema
link = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

#Passo 2
#Entrar no diretório do arquivo de vendas
time.sleep(5)
pyautogui.click(389, 270, clicks=2)

#Passo 3
#Download do arquivo
time.sleep(5)
pyautogui.click(401,337) #clicar no arquivo
time.sleep(3)
pyautogui.click(1162,160) #clicar nos 3 pontinhos
time.sleep(2)
pyautogui.click(1006, 524)
time.sleep(10)

#Passo 4
#Abrir e analisar o arquivo da tabela 
tabela = pd.read_excel(r'C:\Users\John\Downloads\Vendas - Dez.xlsx')
faturamento = tabela['Valor Final'].sum() #soma da coluna valor final
quantidade = tabela['Quantidade'].sum() #soma da coluna quantidade

#Passo 5
#Enviar o e-mail
pyautogui.hotkey('ctrl', 't')
link = 'https://mail.google.com/mail/u/0/#inbox' #e-mail da sua preferencia
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
time.sleep(5)
pyautogui.click(92,165)
time.sleep(3)
pyautogui.write('jhoniedw.com@gmail.com')
time.sleep(1)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
assunto = 'Relatório de vendas.'
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')
email = f"""
Prezados, bom dia.

O nosso faturamento de ontem foi de: {faturamento:,.2f}
A quantidade foi de: {quantidade:,.2f}

Atenciosamente, Jhonatas.
"""
pyperclip.copy(email)
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.hotkey('ctrl', 'enter')
time.sleep(3)
exit()  
#Análise de dados para resolução de problemas

#passo 1 - Impotar a base de dados
#sempre usar PANDAS para análise de dados em python
import pandas as pd

tabela = pd.read_csv('C:/users/john/documents/Intensivão de Python/Dia 2/telecom_users.csv')

#passo 2 - vizualizara base de dados
    # - entender as informações disponiveis
    # - resolver erros e problemas
# print(tabela)
# print(tabela.info())

#passo 3 - tratar a base de dados 
    # - valores de texto que estão como números
    # - valores vazios
tabela = tabela.drop('Unnamed: 0', axis=1)
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
tabela = tabela.dropna(how='all', axis=1)
tabela = tabela.dropna(how='any', axis=0)
# print(tabela.info())

#passo 4 - análise inicial(análise exploratória) -> ver como estão os cancelamentos
print(tabela['Churn'].value_counts(normalize=True))

#passo 5 - analisar características do cliente e associar aos cancelamentos
import plotly.express as px

grafico = px.histogram(tabela, x='MesesComoCliente', color='Churn')
grafico.show()

for coluna in tabela:
    grafico = px.histogram(tabela, coluna, color='Churn')
    grafico.show()



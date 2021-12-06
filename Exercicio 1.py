import pandas as pd
from twilio.rest import Client

# Your Auth Token from twilio.com/console
account_sid = "Código"
auth_token  = "Código"
client = Client(account_sid, auth_token)
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print (f'{vendedor} realizou um venda no valor de {vendas} no mês de {mes}')
        message = client.messages.create(
            to=""
               "numero",
            from_="numero",
            body="Suas vendas ultrapassaram 55.000")

        print(message.sid)

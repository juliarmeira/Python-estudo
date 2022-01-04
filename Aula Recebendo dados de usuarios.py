# Recebendo dados de usuários
"""
input --> Todo dado recebido é do tipo string
Em python, string é tudo que estiver entre:
-Aspas simples;
-Aspas duplas;
-Aspas simples triplas;
-Aspas duplas triplas;
Exemplos:
-Aspas simples -'Angelina'
-Aspas duplas - "Angelina"
-Aspas simples triplas - '''Angelina'''
"""
# Entrada de dados

#print('Qual o seu nome?')
#nome = input() # Input --> Entrada

nome = input ('Qual seu nome?')

# Exemplo de print 'antigo' 2x
# print ('seja bem vindo(a) %s' % nome)
# Exemplo de print 'moderno' 3x
# print ('Seja bem vinfo(a) {0}'. format (nome))
# Exemplo de print 'mais atual' 3.6/3.7

print (f'Seja bem vindo (a) {nome}')

#print('Qual a sua idade?')
#idade=input()

idade = input ('Qual a sua idade?')

# Processamento
# Saída de dados
# Exemplo de print 'antigo' 2x
# print (' %s tem %s anos' % (nome, idade))

print(f'{0} tem {0} anos'. format (nome, idade))

print(f'{nome} nasceu em {2022-int(idade)}') #int(idade) --> cast



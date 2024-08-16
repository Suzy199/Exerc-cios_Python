
#################   EXERCÍCIO 1   #################
"""
resposta = input('Xavier merece aumento?')

if (cadatrado):
    print('emita nota fiscal')

if (resposta == 'sim'):
    print('Dê um aumento para o Xavier')
else:
    print('Não dê um aumento para o Xavier')



#################   EXERCÍCIO 2   #################

resposta = int(input('Informe um número: '))

if resposta % 2 == 1:
    print('O número é ímpar.')
else: 
    print('O número é par.')



#################   EXERCÍCIO 3   #################

resposta = float(input('Qual é a sua temperatura? '))

if resposta > 37: cancela = False
else: cancela = True

if cancela == True: print('Liberado')
else: print('Não liberado')

"""

#################   EXERCÍCIO 4   #################

i = 0
respirador = []
taxa = []

for i in range(4):
    respirador.append(int(input(f'Quantidade de respiradores no hospital {i + 1} é: ')))
    taxa.append(int(input('Taxa de ocupação em porcentagem: ')))
    if taxa[i] > 60:
        respirador[i] += 5
    print('A quantidade final de respiradores no hospital', i + 1, 'é: ', respirador[i])
    i =+ 1

################# ATIVIDADE FINAL #################

"""

import random

cliente = []
telefone = []
id = []
i = 0
x = input('Informe o nome do cliente: ')

cliente[0] = x
telefone[i] = int(input('Informe o telefone do cliente: '))


while cliente != 'fim':
    i += 1
    id = i
    cliente[i] = input('Informe o nome do cliente: ')
    telefone[i] = int(input('Informe o telefone do cliente: '))

tam = i

choice = random.randint(1,tam)

print('O ID escolhido foi o:', choice, '.')
print('Para esse ID, o usuário escolhido foi o:', cliente[choice], '. O telefone do cliente é:', telefone[choice], '.')


"""
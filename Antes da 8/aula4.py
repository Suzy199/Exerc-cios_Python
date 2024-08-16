
"""
from random import randrange

x = randrange(1,10)
y = 0

while x != y:
    y = int(input('Chute um número que esteja entre 1 e 10: '))
    print(x)
    print(y)

    if x > y: print('ERRADO! \nChute um valor maior.')
    elif x < y: print('ERRADO! \nChute um valor menor.')
    else: print(f'Parabéns, o número {x} é o correto.')


"""


"""
################# ATIVIDADE 1 #################


for num in (1,2,3,4,5):
        print(num)
input('tecle enter para continuar... \n')

for j in range(5):
    print(j)
input('Tecle enter para continuar...\n')

for x in range(0,8,2):
        print(x)
input('Tecle enter para continuar...\n')

for x in 'infinity':
        print(x)
input('Tecle enter para continuar...\n')
    

palavra = input('Informe uma palavra: ')
ctv = 0

"""


"""

################# ATIVIDADE 2 #################

### a palavra é contada, e a letra é guardada em l, caso a variável l for guardada em a, ctv é somado + 1

for l in palavra:
    if ((l == 'a') or (l == 'e') or (l == 'i') or (l == 'o') or (l == 'u')):
        ctv += 1
        
print("Esta palavra ({0}) tem {1} vogais.".format(palavra,ctv))

"""


"""

################# ATIVIDADE 3 #################

qtd = int(input("Informe a quantidade de notas que deseja inserir no sistema: "))
media = 0
media_total = 0

for i in range(qtd):
    media = float(input(f'Informe a média {i}: '))
    media_total += media 
    i +=1

media = media_total/qtd

print(f'A média das notas é {media :.2f}.')
""" 

################# ATIVIDADE 4 #################

"""

leve = int(input("Quantos pacientes estão com sintomas leves? "))
grave = int(input("Quantos pacientes estão com sintomas graves? "))
assintomatico = int(input("Quantos pacientes estão assintomaticos? "))
qtd = leve + grave + assintomatico

print(f'Do total de {qtd} pacientes, {((leve/qtd)*100):.2f}% estão com sintomas leves, {((grave/qtd)*100):.2f}% estão com sintomas graves e {((assintomatico/qtd)*100):.2f}% estão assintomáticos.')

"""

################# ATIVIDADE 5 #################


"""
qtd_leves = 0
qtd_assintomaticos = 0
qtd_graves = 0

for p in range(10):
    tipo_paciente = input('Informe o tipo de paciente (l,a,g): ')
    if (tipo_paciente == 'l'): qtd_leves += 1
    elif (tipo_paciente == 'a'): qtd_assintomaticos += 1
    elif (tipo_paciente == 'g'): qtd_graves += 1
    else: 
        print('A letra digitada está errada')
        p = p - 1
    print(p)


print(f'Do total de 10 pacientes, {((qtd_leves/10)*100):.2f}% estão com sintomas leves, {((qtd_graves/10)*100):.2f}% estão com sintomas graves e {((qtd_assintomaticos/10)*100):.2f}% estão assintomáticos.')

"""

"""
################# ATIVIDADE 6 #################

#item retorna a chave e o valor, key retorna apenas a chave, values retorna apenas o valor

provasFinais = {'Marta':9, 'Paulo':5, 'Helena':7, 'Roberto':10}

print('Todas as provas:', provasFinais)
print('chave [Marta]:', provasFinais['Marta'])

######################################## Uso do item

for aluno, nota in provasFinais.items():
    print ('A nota do(a) aluno(a)',aluno,'foi',nota)

input ('Tecle enter para continuar...\n')

# Outro dicionário
######################################## Uso do keys

pessoas = {'Marcos':'astronauta','Ana':'médica','Eduardo':'professor','Beatriz':'médica'}
if 'Ana' in pessoas.keys():   # OBS: apenas o nome do dicionário também funciona
    print ('Existe "Ana" na coleção do dicionário')
else:
    print ('Não "Ana" na coleção do dicionário')

###################################### Uso do Value

if 'professor' in pessoas.values():
    print ('Existe(m) professor(es) na coleção do dicionário')
else:
    print ('Não existe(m) professor(es) na coleção do dicionário')

input ('Tecle enter para continuar...\n')

print ('----- FIM DA EXECUÇÃO -----')

"""

################# ATIVIDADE 7 #################

for x in range (100):
    print(x)
    print('---------')
    if x == 50: break
    
print('TERMINOU!!!')
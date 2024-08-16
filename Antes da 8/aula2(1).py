###################### EXERCÍCIO 1 ######################

tempF = float(input('Informe a temperatura em Farenheit: '))
tempC = 5 * ((tempF - 32)/9)

print ('RESPOSTA:', temF, 'Farenheit equivale a', tempC, 'Celcius')
print('RESPOSTA: {0} Farenheit equivalem a {1} Celcius'.format(tempF, tempC))
print('----- FIM DA EXECUÇÃO -----')


###################### EXERCÍCIO 2 ######################

base = float(input('Informe a base'))
altura = float(input('Informe a altura'))

area = base * altura

print('A área é:', area)


###################### EXERCÍCIO 3 ######################

brancos = int(input('Informe a quantidade de votos brancos: '))
nulos = int(input('Informe a quantidade de votos nulos: '))
valido = int(input('Informe a quantidade de votos válidos: '))
total = int(input('Informe a quantidade total de votos: '))

perbranco = (brancos/total)*100
pernul = (nulos/total)*100
perval = (valido/total)*100

print('A porcentagem de votos brancos é:',perbranco, 'dos nulos: ',pernul, 'e dos válidos: ',perval)

###################### EXERCÍCIO 4 ######################

A = int(input('Informe o valor de A: '))
B = int(input('Informe o valor de B: '))

C = A
A = B
B = C

print('O novo valor de A é:', A ,'. O novo valor de B é:', B)

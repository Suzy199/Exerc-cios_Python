#### primeira aula de python ####

### função ###

"""
def funcSoma (parm1, parm2):
    soma = parm1 + parm2
    return soma

x = int(input('Valor 1: '))
y = int(input('Valor 2: '))

resultado = funcSoma(x,y)

print('Resultado da soma:', resultado)

################################

################################
 
 
from datetime import datetime
 
def diferenca (data_info):
    
    data_info = datetime.strptime(data_info, '%d/%m/%Y')
     
    data_atual = datetime.today()
    daydiference = abs((data_atual - data_info).days)
    return daydiference
 
 
data_info = input('Informe uma data no formato DD/MM/AAAA: ')
print(f'A diferença de dias é: {diferenca(data_info)}')

"""
################################

################################

"""
def avaliaroupa (tamanho, sexo = None): ###se sexo não informado, atribuir vazio
    if sexo = 'm': tamanho += 5
    else: tamanho += 3
"""  


###############################

################################

"""

def soma(valores):
    a = valores[0] + valores[1]
    return a

def sub(valores):
    b = valores[0] - valores[1]
    return b

def multi(valores):
    c = valores[0] * valores[1]
    return c

def div(valores):
    d = valores[0] / valores[1]
    return d

i = 0  
valores = []

while i < 2: 
    valor = int(input('Informe 1 valor:'))
    valores.append(valor)
    print('\n')
    i += 1
    
    
print(f'Soma: {soma(valores)}. \n')
print(f'Subtração: {sub(valores)}. \n')
print(f'Multiplicação: {multi(valores)}. \n')
print(f'Divisão: {div(valores):.2f}. \n')

"""
###############################

###############################

"""
def ordenar (valores):
    
    valores.sort()
    return valores


i = 0
valores = []

while i < 3: 
    valor = int(input('Informe 1 valor:'))
    valores.append(valor)
    i += 1


print(f'Os valores ordenados ficará da seguinte forma: {ordenar(valores)}')
"""
"""
#Maneira difícil

def organiza ():
    
    a = int(input('Valor 1: '))
    b = int(input('Valor 2: '))
    c = int(input('Valor 3: '))
    
    if a < b:
        k = a
        a = b
        b = k
        
        if  a < c:
            k = a
            a = c
            c = k
        
    if b < c:
        k = b
        b = c
        c = k
        
    return a, b, c

a, b, c = organiza()

print(c,b,a)

"""
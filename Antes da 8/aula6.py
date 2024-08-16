
################################################## LISTAS ##################################################
## FUNÇÕES: lista.copy(), lista.clear(), 

"""
alunos = ['Adalberto', 'Alejandro', 'Giovana']

## tipo, tamanho, lista inteira, elemento específico da lista ##
print(type(alunos))
print(len(alunos))
print(alunos)
print(alunos[2])

## Insere elemento no fim, insere elemento na posição expecífica, retira elemento na posição expecífica, retira no fim ##
alunos.append('Carmen')
print(alunos)
alunos.insert(2,"Larissa")
print(alunos)
alunos.pop(1)
print(alunos)
alunos.remove('Giovana')
print(alunos)
"""

################################################## TUPLAS ##################################################

"""
alunos = (1, 2, 3, 4)

## elemento específico, toda a tupla, tamanho, soma, multiplicação, elemento existe, interação ## 
## Tupla é imutável, não se pode alterar um elemento ##

print(alunos[0])
print(alunos[0:4])
print(len(alunos))
print(alunos + alunos)
print(alunos * 3)
print(3 in alunos)
for x in alunos: print(x)
"""

################################################## DICIONÁRIO ##################################################


"""
dados_aluno = {
    'nome': 'Giovana',
    'endereco': 'Rua abc',
    'telefone': '123',
}

dados_aluno['cpf'] = '123456'
dados_aluno.pop('telefone')
print(dados_aluno)

"""

##################################################### FIM #####################################################

################################################# ATIVIDADE 1 #################################################

"""
palavra = input('Insira uma palavra: ')

a, e, i, o, u = 0, 0, 0, 0, 0

vogais = {}

for letra in palavra:
    if letra.lower() == 'a': a += 1
    elif letra.lower() == 'e': e += 1
    elif letra.lower() == 'i': i += 1
    elif letra.lower() == 'o': o += 1
    elif letra.lower() == 'u': u += 1

vogais['a'] = a
vogais['e'] = e
vogais['i'] = i
vogais['o'] = o
vogais['u'] = u

print(vogais)

"""

################################################# ATIVIDADE 2 #################################################

aluno = {}

def mediaNotas(a):
    return sum(aluno[a])/2

while (True):
    nome = input('Nome do aluno: ')
    if (nome == ''): break;
    n1 = float(input ('Nota 1: '))
    n2 = float(input ('Nota 2: '))
    aluno[nome] = [n1,n2]


print(aluno)

for a in aluno:
    print(f'A média do aluno {a} é {mediaNotas(a)}. ')
from datetime import date


################# ATIVIDADE 1 #################

time1 = input('Time 1: ')
time2 = input('Time 2: ')
gols1 = input(f'Quantidade de gols marcados pelo {time1}:')
gols2 = input(f'Quantidade de gols marcados pelo {time2}:')

if gols1 > gols2:
    print(f'O {time1} ganhou.')
elif gols2 > gols1:
    print(f'O {time2} ganhou.')
else:
    print('Os times empataram.')


################# ATIVIDADE 2 #################

"""
int(input("Informe o seu código: "))
nas  = int(input('Informe o seu ano de nascimento: '))
tra = int(input('Informe o seu ano de ingresso na empresa: '))

ano = date.today().year

if (ano - nas >= 65) or (ano - tra >= 30) or (ano - nas >= 60 and ano - tra >= 25):
    print('Requerer aposentadoria.')
else:
    print('Não requerer aposentadoria.')


"""


################# ATIVIDADE 3 #################




from random import randrange

num_sorteado = randrange(1,10)

num_digitado = int(input('digite um número: '))


while num_digitado != num_sorteado:
    if num_digitado > num_sorteado:
        print('o número digitado é maior do que o número sorteado. \nTente outra vez.')
    elif num_digitado < num_sorteado:
        print('o número digitado é menor do que o número sorteado. \nTente outra vez.')
    else:
        break
    num_digitado = int(input('digite um número: '))
    
    
print('VOCÊ ACERTOU!!')    
palavra = input('digite uma palavra: ')

contador = 0
 
for letra in palavra:
    if letra in 'aeiou':
        contador += 1
        
print(f'A palavra {palavra} tem {contador} vogais.')
        
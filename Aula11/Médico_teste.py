from Médico import medico
from Médico import auxiliar
from Médico import cirurgiao


med1 = medico(54,"Cléber",54,8904)
med2 = medico(56,"Genilson",56,10000)

aux1 = auxiliar(64,"Jhonatan",64,8904)
aux2 = auxiliar(56,"Jeferson",56,10000)

cir1 = cirurgiao(24,"Carlos",6424,8904)
cir2 = cirurgiao(52,"Alfredo",52,10000)

print(f'O médico é: {med1._Nome}, ele tem {med1._Idade} e sua aposentadoria é de {med1.aposentadoria()} reais.')
print(f'O médico é: {med2._Nome}, ele tem {med2._Idade} e sua aposentadoria é de {med2.aposentadoria()} reais.')
print(f'O médico é: {aux1._Nome}, ele tem {aux1._Idade} e sua aposentadoria é de {aux1.aposentadoria()} reais.')
print(f'O médico é: {aux2._Nome}, ele tem {aux2._Idade} e sua aposentadoria é de {aux2.aposentadoria()} reais.')
print(f'O médico é: {cir1._Nome}, ele tem {cir1._Idade} e sua aposentadoria é de {cir1.aposentadoria()} reais.')
print(f'O médico é: {cir2._Nome}, ele tem {cir2._Idade} e sua aposentadoria é de {cir2.aposentadoria()} reais.')
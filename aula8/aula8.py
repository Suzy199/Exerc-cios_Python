####################################### ATIVIDADE 1 - CONTA CORRENTE #######################################
"""
from ContaCorrente import ContaCorrente 

contaSuzy = ContaCorrente('14788-9','123456') #atribui conta a um objeto da classe ContaCorrente 
contaBillGates = ContaCorrente('14788-9','123456','555','05',400000000) #conta é um objeto da classe ContaCorrente 

print('Saldo de Suzy:', contaSuzy.saldo) #saldo é um atributo do objeto conta, que pertence a classe ContaCorrente
print('Saldo de Bill Gates:', contaBillGates.saldo)

contaSuzy.depositar(1000) #Como conta pertence à classe ContCorrente, pode chamar um método para esse objeto.


contaBillGates.transferir(contaSuzy,500)
print('NOVO saldo de Suzy', contaSuzy.saldo)

"""
########################################### ATIVIDADE 2 - CARRO ###########################################

from Carro import Carro

carroSuzy = Carro('PEGEOUT','207','2013',0,'SIM','SIM')

print('Marca do carro:', carroSuzy.marca)
print('Modelo do carro:', carroSuzy.modelo)
print('Ano do carro:', carroSuzy.ano)
print('Velocidade do carro:', carroSuzy.velocidade)
print('O carro está ligado?:', carroSuzy.ligado)
print('O caro é automático?:', carroSuzy.automatico)

print(carroSuzy.ligar())
print(carroSuzy.desligar())
print(carroSuzy.ligar())

carroSuzy.acelerar(110)
carroSuzy.acelerar(20)
carroSuzy.marcha()

print(carroSuzy.desligar())
print(carroSuzy.ligar())
carroSuzy.acelerar(20)
carroSuzy.marcha()
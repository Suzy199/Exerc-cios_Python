#objeto é a parte física que é categorizada por uma classe (pertence a ela)
#classe é o passo a passo para fazer uma ação, os parâmetros que categorizam algo
#objeto em uma da classe fruta (que possui tamanho, cor...)

#classe possui atributo(característica) e método(função)

class ContaCorrente: #classe
    def __init__(self, num, sen, agen = '555', ba = '01', sal = 15): #construção de uma classe, senha chama a própria classe
        # Quando já está atribuido o valor, não é pedido ao usuário mais uma vez
        self.numero = num
        self.senha = sen
        self.agencia = agen
        self.banco = ba
        self.saldo = sal
        
    
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        self.saldo -= valor
        
    def transferir(self, conta_destino, valor):
        self.sacar(valor)
        conta_destino.depositar(valor) #alteração do saldo de outra pessoa, não usa o self
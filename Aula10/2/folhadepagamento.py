class Folhadepagamento:
    def __init__ (self, lista_pessoa):
        self.__lista_pessoa = lista_pessoa
    
    def valortotal(self):
        total = 0.0
        for p in self.__lista_pessoa:
            total += p.valor 
        return total
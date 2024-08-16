#método GET - visualiza uma variável de uma classe
#método SET - altera o valor de uma variável em uma classe
#Sugestão do python: Quando quero proteger uma variável, eu a declaro da seguinte forma: self.__preco = valor. Coloco o __.
#Quando utilizo um arroba em uma classe, quer dizer que eu estou definindo uma forma de comportamento em minha classe.

#Quando eu chamo o produto.preco, não chamo o produto, eu chamo o get. 

class Produto:
    def __init__(self, nome, valor, descricao):
        self.nome = nome
        self.__preco = valor                     #declarando uma variável fixa, imutável. Tudo aqui são atributos.
        self.descricao = descricao
        

    @property                                        #comportamento do GET, sempre usa o property. Não é atributo
    def preco(self):
        return self.__preco

    @preco.setter                                    #comportamento do SET, sempre usa o @xxxx.setter. Não é atributo
    def preco(self,valor):
        preco_min = self.__preco*0.10
        preco_min = self.preco - preco_min
        
        if (valor >= preco_min):
            self.__preco = valor
            return True
        else:
            return False
    

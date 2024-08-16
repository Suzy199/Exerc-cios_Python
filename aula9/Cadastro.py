class Cadastro:
    def __init__(self, nome, novo_salario, matricula, funcao):
        self.nome = nome
        self.__salario = novo_salario
        self.matricula = matricula
        self.funcao = funcao 
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, novo_salario):
        salario_max = self.__salario * 1.2
        
        if (novo_salario <= self.__salario):
            return False
        elif (novo_salario > salario_max):
            return False
        else:
            self.__salario = novo_salario
            return True
            
        
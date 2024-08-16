class medico:
    def __init__ (self,CRM,Nome,Idade,Salario):
        self._CRM = CRM
        self._Nome = Nome
        self._Idade = Idade
        self._Salario = Salario
    
    def aposentadoria(self): 
        if self._Idade >= 55:
            return self._Salario*0.8
        else: return 0

class auxiliar(medico):
    def __init__(self,CRM,Nome,Idade,Salario):
        super().__init__(CRM,Nome,Idade,Salario)
            
    def aposentadoria(self): 
        if self._Idade >= 60:
            return self._Salario*0.8
        else: return 0
        
class cirurgiao(medico):
    def __init__(self,CRM,Nome,Idade,Salario):
        super().__init__(CRM,Nome,Idade,Salario)
    
    def aposentadoria(self):
        if self._Idade >= 50:
            return self._Salario*0.8 + 2000
        else: return 0
            
            
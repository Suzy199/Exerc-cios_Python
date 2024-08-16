class professor:
    def __init__(self,nome_professor,pontuacao_professor):
        self._nome = nome_professor
        self._pontuacao_professor = pontuacao_professor




class instrumento:
    def __init__(self, nome_instrumento,nome_professor):
        self._nome_instrumento = nome_instrumento
        self._nome_professor = nome_professor
    
    def grau_de_dificuldade(self):
        return self.professor.pontuacao_professor
        

class corda(instrumento):
    def __init__(self, quantidade_corda, tipo_corda):
        def super().__init__(self, nome_instrumento,nome_professor)
    
        self._quantidade_corda = quantidade_corda
        self._tipo_corda = tipo_corda
    
    def dificuldade(self,tipo_corda):
        if tipo_corda == "aço": 
            return super().grau_de_dificuldade()*quantidade_corda
        else: 
            return super().grau_de_dificuldade()


class percussao(instrumento):
    def __init__(self, baqueta):
        def super().__init__(self, nome_instrumento,nome_professor)
    
        self._baqueta = baqueta
        
    def dificuldade(self):
        return super().grau_de_dificuldade()


class sopro(instrumento):
    def __init__(self):
        def super().__init__(self,nome_instrumento,nome_professor)
    
    def dificuldade(self):
        return super().grau_de_dificuldade()


    
    
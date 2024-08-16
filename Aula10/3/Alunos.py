import ntpath


class alunos:
    def __init__(self, nome, matricula, score):
        self.__nome = nome
        self.__matricula = matricula 
        self.__nota = nota

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def score(self):
        return self.__score
    
    @nota.setter
    def nota(self, score):
        self.__score = score

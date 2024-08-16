class patrocinador:
    def __init__(self, nome, valor):
        self.nome = nome
        self._valor = valor

class atleta:
    def __init__(self, nome, idade, pontuacao, categoria):
        self._nome = nome
        self._idade = idade
        self._pontuacao = pontuacao
        self._categoria = categoria

class campeonato:
    def __init__(self, categoria, nome, local, premiacao, patrocinadores):
        self._categoria = categoria
        self._nome = nome
        self._local = local
        self._premiação = premiacao
        self._patrocinadores = patrocinadores
        self.lista_de_atletas = []
        self._vencedor = ''
        
    def todos_atletas(self, atleta): ## puxando da classe atleta
        self.lista_de_atletas = atleta
    
    def vencido_por(self, atleta): ## puxando da classe atleta
        self._vencedor = str(atleta._nome)



class campeonato_amador(campeonato):
    def __init__(self, categoria, nome, local, premiação, patrocinadores):
        super().__init__(categoria, nome, local, premiação, patrocinadores) ## puxando da classe campeonato
    
    def todos_atletas(self, atleta): ## puxando da classe atleta
        for a in atleta:
            if ((a._categoria == 'amador') | (a._categoria == "profissional") | (a._categoria == 'lenda')):
                self.lista_de_atletas.append(a)#se alguém da lista atleta geral for amador, ele é incluso na lista daclasse
    
    def vencido_por(self, atleta):  ## puxando da classe atleta
        self._vencedor = atleta._nome
        atleta._pontuacao += 10


class campeonato_profissional(campeonato):
    def __init__(self, categoria, nome, local, premiação, patrocinadores):
        super().__init__(categoria, nome, local, premiação, patrocinadores) ## puxando da classe campeonato
    
    def todos_atletas(self, atleta): ## puxando da classe atleta
        for a in atleta:
            if ((a._categoria == 'profissional') | (a._categoria == 'lenda')):
                self.lista_de_atletas.append(a)#se alguém da lista atleta geral for profi, ele é incluso na lista da classe
    
    def vencido_por(self, atleta): ## puxando da classe atleta
        self._vencedor = atleta._nome
        atleta._pontuacao += 50
  
        
class campeonato_lenda(campeonato):
    def __init__(self, categoria, nome, local, premiação, patrocinadores):
        super().__init__(categoria, nome, local, premiação, patrocinadores) ## puxando da classe campeonato
    
    def todos_atletas(self, atleta): ## puxando da classe atleta
        for a in atleta:
            if (a._categoria == 'lenda'):
                self.lista_de_atletas.append(a)#se alguém da lista atleta geral for lenda, ele é incluso na lista da classe
    
    def vencido_por(self, atleta): ## puxando da classe atleta
        self._vencedor = atleta._nome
        atleta._pontuacao += 100
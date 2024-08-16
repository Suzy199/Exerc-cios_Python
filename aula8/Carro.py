class Carro:
    def __init__(self, marca, modelo, ano, velocidade = 0, ligado = 'NÃO', automatico = 'NÃO'):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        self.ligado = ligado
        self.automatico = automatico
    
    def ligar(self):      
        self.ligado = 'SIM'
        return 'O carro está ligado'
    
    def desligar(self):      
        self.ligado = 'NÃO'
        self.velocidade = 0
        return 'O carro está desligado'
    
    def acelerar(self, valor):
        if self.ligado == 'SIM':
            self.velocidade += valor
            if self.velocidade > 120: self.velocidade = 120       
            print(f'A nova velocidade é {self.velocidade} km/h.')   
            
        else: print('O carro está desligado, não é possível acelerar.')
        
    
    def marcha(self):
        if self.velocidade == 0: print('Carro desligado')
        elif self.velocidade >= 0 and self.velocidade < 20: print('Primeira marcha.')
        elif self.velocidade >= 20 and self.velocidade < 30: print('Segunda marcha.')
        elif self.velocidade >= 30 and self.velocidade < 45: print('Terceira marcha.')
        elif self.velocidade >= 45 and self.velocidade < 60: print('Quarta marcha.')
        else: print('Quinta marcha.')
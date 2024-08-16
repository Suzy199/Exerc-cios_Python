from Cadastro import Cadastro
    
pessoa1 = Cadastro('Suzy',1104,'ETB346200', 'Estagiaria')
print('---------------')
print(f'O Salário atual de {pessoa1.nome} que é {pessoa1.funcao} é: {pessoa1.salario}')
pessoa1.salario = 1320
print('---------------')
print(f'O Salário atual de {pessoa1.nome} que é {pessoa1.funcao} é: {pessoa1.salario}')
print('---------------')
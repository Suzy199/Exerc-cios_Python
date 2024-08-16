from RH import Pessoa
from folhadepagamento import Folhadepagamento

num = int(input("Quantas pessoas você deseja cadastrar?")) 
lista_pessoa = []

for x in range(num):
    nome = input("Qual o nome das pessoa?")
    valor = int(input("Qual o salário da pessoa?"))
    matricula = int(input("Qual o número da matrícula?"))
    pessoa = Pessoa(nome, valor, matricula)
    lista_pessoa.append(pessoa)

folha = Folhadepagamento(lista_pessoa)
 
print(folha.valortotal())
 
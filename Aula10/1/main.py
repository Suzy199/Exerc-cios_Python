from Endereco import endereco
from Cliente import Cliente


#DADOS DO CLIENTE
nome = input("Informe o seu nome: ")
email = input("Informe o seu e-mail: ")
senha = input("Informe a sua senha: ")


#DADOS DO ENDEREÇO DO CLIENTE
cep = input("Informe o cep da rua: ")
rua = input("Informe a rua: ")
numero = input("Informe o número: ")
cidade = input("Informe a cidade: ")
estado = input("Informe o estado: ")
pais = input("Informe o país: ")

#CRIANDO ENDEREÇO
endereco1 = endereco(cep, rua, numero, cidade, estado, pais)

#CRIANDO UM CLIENTE 
cliente1 = Cliente(nome, email, senha, endereco1)
print("Nome: ", cliente1.nome)
print("Email: ", cliente1.email)
print("Endereço: ", cliente1.endereco.rua,", ", cliente1.endereco.numero)


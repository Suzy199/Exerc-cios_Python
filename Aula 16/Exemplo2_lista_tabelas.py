import mysql.connector
from mysql.connector import Error

try:
    conexaoBD = mysql.connector.connect (
        host='localhost',       # Nome ou IP do servidor
        user='root',            # Usuário 
        password='aluno99',    # Senha
        database='aula16'    # Nome do banco de dados    
    )

    #testando se a conexão ao BD funcionou
    if (conexaoBD.is_connected()):
        # Enviando um comando SQL para ser executado no servidor
        print ('-------------------------------------')
        sql = "show tables"
        resposta = conexaoBD.cursor()
        resposta.execute(sql)
        # Recebendo e tratando os resultados da execução do comando
        for result in resposta:
            print ('tabela:',result)
        print ('-------------------------------------')
except Error as erro:
    # tratando erros na execução
    print('--------------------------------------------')
    print('Ocorreu um erro ao acessar o banco de dados:')
    print(erro)
    print('--------------------------------------------')
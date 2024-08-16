import mysql.connector
from mysql.connector import Error

# -------
# Funções
# -------
def conecta_banco():
    try:
        # Conectando ao banco de dados no servidor
        return mysql.connector.connect (
            host = 'localhost', 
            user = 'root',
            password = 'aluno99',
            database = 'aula16'
        )
        
    except Error as erro:
        # tratando erros na conexão
        print('>>> ERRO na conexão com o banco de dados: ',erro)

def processa_comando(conexao,comando):
    try:
        # Execução do comando no servidor e recebimento da resposta no cursor
        print ('>>> Executando o comando: ',comando)
        cursor = conexao.cursor()
        cursor.execute(comando)
        return cursor
    except Error as erro:
        # tratando erros na execução
        print('>>> ERRO na execução do comando SQL: ',erro)

def exibe_resposta(r):
        # Recebendo e tratando os resultados da execução do comando
        for result in r:
            print ('Dados recebidos:',result)


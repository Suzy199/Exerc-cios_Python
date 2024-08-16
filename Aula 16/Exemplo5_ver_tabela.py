import mysql.connector
from mysql.connector import Error

try:
    conexaoBD = mysql.connector.connect (
       host = 'localhost', 
       user = 'root',
       password = 'aluno99',
       database = 'aula16'
    )
    
    if (conexaoBD.is_connected()):
            print ('-----------------------------------------------')
            print ('Conexao realizada com sucesso!')
            print ('-----------------------------------------------')
            print ('---(Lendo a tabela "alunos")---')
            sql = 'select * from alunos'
            resposta = conexaoBD.cursor()
            resposta.execute(sql)
            
            
            for result in resposta:
                print ('Aluno:', result)
            print ('---(fim dos dados da tabela "alunos")---')
        
except Error as erro:
    print('Ocorreu um erro ao acessar o banco de dados:')
    print(erro)
from exemplo4_classe_geral import conecta_banco, processa_comando, exibe_resposta

# ---------------------------
# Aqui começa o processamento
# ---------------------------


try:
    conexaoBD = conecta_banco()
    #testando se a conexão ao BD funcionou
    if (conexaoBD.is_connected()):
        # Enviando um comando SQL (SELECT)
        print ('-------------------------------------')
        print ('Lendo dados da aluna "Ana"...')
        sql = "SELECT * FROM Alunos WHERE nome = 'Ana'"
        resposta = processa_comando(conexaoBD,sql)
        exibe_resposta(resposta)

        # Enviando um comando SQL (UPDATE)
        print ('-------------------------------------')
        print ('Alterando dados da aluna "Ana"... (antes de alterar)')
        sql = "UPDATE Alunos SET curso = 'DEVHC' WHERE nome = 'Ana'"
        resposta = processa_comando(conexaoBD,sql)
        # Confirmando a alteração (COMMIT) ----- O COOMIT altera o campo curso para o nome ANA
        conexaoBD.commit()

        # Enviando um novo comando SQL (SELECT)
        print ('-------------------------------------')
        print ('Lendo dados da aluna "Ana"... (depois de alterar)')
        sql = "SELECT * FROM Alunos WHERE nome = 'Ana'"
        resposta = processa_comando(conexaoBD,sql)
        exibe_resposta(resposta)

        print ('-------------------------------------')
        
except Error as erro:
    # tratando erros
    print('>>> ERRO no processamento principal: ',erro)
    

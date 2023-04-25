import sqlite3

# conecta ao banco de dados
conn = sqlite3.connect('exemplo.db')

# cria a tabela
conn.execute('''CREATE TABLE IF NOT EXISTS alunos
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             NOME TEXT NOT NULL,
             IDADE INT NOT NULL);''')

# adiciona um registro
conn.execute("INSERT INTO alunos (NOME, IDADE) VALUES ('João', 20)")

# atualiza um registro
conn.execute("UPDATE alunos SET NOME = 'Maria' WHERE ID = 1")

# remove um registro
conn.execute("DELETE FROM alunos WHERE ID = 1")

# lê todos os registros
cursor = conn.execute("SELECT * FROM alunos")
for linha in cursor:
    print("ID = ", linha[0])
    print("NOME = ", linha[1])
    print("IDADE = ", linha[2])

# fecha a conexão
conn.close()
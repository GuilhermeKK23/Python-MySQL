import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "gerenciador_de_horarios_db"
)

mycursor = mydb.cursor()

# insere valores na tabela 'administradores_tbl'
mycursor.execute("INSERT INTO administradores_tbl VALUES (DEFAULT, 'Ash', 'Pikachu', 'Ash@gmail.com')")

# # salva as mudanças feitas (é necessário para fazer mudanças na tabela)
mydb.commit()

# exibe o número de registros inseridos
print(mycursor.rowcount, "inserido")
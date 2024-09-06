import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "gerenciador_de_horarios_db"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO administradores_tbl VALUES (DEFAULT, 'Ash', '1234', 'Ash@gmail.com')")

# é necessário para fazer mudanças na tabela
mydb.commit()

print(mycursor.rowcount, "inserido")
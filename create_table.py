import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "gerenciador_de_horarios_db"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE administradores_tbl(id_adm INT PRIMARY KEY AUTO_INCREMENT, usuario_adm VARCHAR(50), senha_adm VARCHAR(50), email_adm VARCHAR(50))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
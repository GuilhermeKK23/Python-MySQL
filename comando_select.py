import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "gerenciador_de_horarios_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT usuario_adm FROM administradores_tbl")

# busca todas as linhas do último comando executado
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "gerenciador_de_horarios_db"
)

mycursor = mydb.cursor()

# seleciona todos os registros da tabela 'administradores_tbl'
mycursor.execute("SELECT * FROM administradores_tbl")

# busca todas as linhas do último comando executado
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
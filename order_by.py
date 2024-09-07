import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "gerenciador_de_horarios_db"
)

cursor = mydb.cursor()

# ordena os registros pela coluna 'usuario_adm', evitando SQL injection
sql = "SELECT * FROM administradores_tbl ORDER BY usuario_adm"
cursor.execute(sql)

# busca todas as linhas do último comando executado
result = cursor.fetchall()

for x in result:
    print(x)
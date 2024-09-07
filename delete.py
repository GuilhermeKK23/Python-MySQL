import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "gerenciador_de_horarios_db"
)

cursor = mydb.cursor()

# mostra os registros antes do delete
cursor.execute("SELECT * FROM administradores_tbl")
result = cursor.fetchall()
for x in result:
    print(x)

# deleta os registros, prevenindo SQL injection
sql = "DELETE FROM administradores_tbl WHERE usuario_adm = %s"
val = ("Ash", )
cursor.execute(sql, val)

# salva as mudanças feitas
mydb.commit()

# mostra os registros depois do delete
cursor.execute("SELECT * FROM administradores_tbl")
result = cursor.fetchall()
for x in result:
    print(x)

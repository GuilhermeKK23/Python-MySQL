import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "gerenciador_de_horarios_db"
)

cursor = mydb.cursor()

sql = "UPDATE administradores_tbl SET usuario_adm = %s, senha_adm = %s, email_adm = %s WHERE id_adm = %s"
val = ('Red', 'Charizard', 'Red@gmail.com', '1')
cursor.execute(sql, val)

# salva as mudanças feitas
mydb.commit()

print(cursor.rowcount, "linha(s) afetada(s)")
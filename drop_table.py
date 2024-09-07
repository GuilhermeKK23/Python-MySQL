import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "gerenciador_de_horarios_db"
)

cursor = mydb.cursor()

# mostra as tabelas antes do drop table
sql = "SHOW TABLES"
cursor.execute(sql)
for x in cursor:
    print(x)

# apaga a tabela, prevenindo erros e SQL injection
sql = "DROP TABLE IF EXISTS administradores_tbl"
cursor.execute(sql)

# mostra as tabelas depois do drop table
sql = "SHOW TABLES"
cursor.execute(sql)
for x in cursor:
    print(x)
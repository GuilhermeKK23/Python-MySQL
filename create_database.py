import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE gerenciador_de_horarios_db")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x) 
# importa o driver MySQL Connector para poder se conectar ao MySQL
import mysql.connector

# faz a conexão com o banco de dados
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "1234",
  database = "gerenciador_de_horarios_db"
)

# cria um cursor, que é um objeto que permite executar comandos SQL
mycursor = mydb.cursor()

# executa comando SQL
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x) 
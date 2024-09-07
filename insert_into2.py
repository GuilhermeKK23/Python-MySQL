import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "gerenciador_de_horarios_db"
)

mycursor = mydb.cursor()

# insere cada tupla da lista como um registro
sql = "INSERT INTO administradores_tbl VALUES (DEFAULT, %s, %s, %s)"
val = [
    ('Ash', 'Pikachu', 'Ash@gmail.com'),
    ('Misty', 'Gyarados', 'Misty@gmail.com'),
    ('Brock', 'Steelix', 'Brock@gmail.com')
]

# executa o comando várias vezes
mycursor.executemany(sql, val)

# salva as mudanças feitas
mydb.commit()

# exibe o número de registros inseridos
print(mycursor.rowcount, "inserido")
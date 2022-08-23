import mysql.connector

mydb =mysql.connector.connect(
    host = 'localhost',
    user = 'vitor',
    password = '2802',
    database = 'python'
)

mycursor = mydb.cursor()


### Variaveis ###
cliente = 'jessica'
telefone = '8789797'
cidade = 'São Paulo'

### INSERT TABELA ###
print('INSERT CLIENTE')
sql = "INSERT INTO cliente (Nome, Telefone, Cidade) values (%s,  %s, %s)"
val = (cliente, telefone, cidade)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, 'record(s) inserted')


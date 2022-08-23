import mysql.connector

mydb =mysql.connector.connect(
    host = 'localhost',
    user = 'vitor',
    password = '2802',
    database = 'python'
)

mycursor = mydb.cursor()


### Variaveis ###
cidade = 'Rio de Janeiro'
idCliente = '2'

### UPDATE TABELA ###
print('UPDATE CLIENTE')
sql = "UPDATE cliente SET Cidade = %s WHERE  IdCliente = %s"
val = (cidade, idCliente)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, 'record(s) updated')
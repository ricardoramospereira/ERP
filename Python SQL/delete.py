import mysql.connector

mydb =mysql.connector.connect(
    host = 'localhost',
    user = 'vitor',
    password = '2802',
    database = 'python'
)

mycursor = mydb.cursor()

### DELETE TABELA ###
print('DELETE CLIENTE')
sql = "DELETE FROM cliente WHERE IdCliente = '5'"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, 'record(s) deleted')


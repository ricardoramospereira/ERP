import mysql.connector

mydb =mysql.connector.connect(
    host = '',
    user = '',
    password = '',
    database = ''
)

mycursor = mydb.cursor()

### CONSULTA TABELA ###
print('CONSULTA TABELA CLIENTE')
mycursor.execute('SELECT * FROM cliente')
myresult = mycursor.fetchall()

for line in myresult:
    print('line: ', line)

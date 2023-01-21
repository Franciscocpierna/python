import mysql.connector
con = mysql.connector.connect(host='localhost',database='cadastro',user='root',password='')
if con.cursor():
    db_info = con.get_server_info()
    print("conectado ao servidor MySql versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print('conectado ao Banco de dados', linha)
sql= ('''
select * from cursos
''')

cursor.execute(sql)
for x in cursor:
    print(x)


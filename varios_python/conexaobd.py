import mysql.connector
sql=''
con = mysql.connector.connect(host='localhost',database='',user='root',password='')
if con.cursor():
    db_info = con.get_server_info()
    print("conectado ao servidor MySql versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print('conectado ao Banco de dados', linha)
    #sql= ("create database processos;")
    #sql = ("drop database processos") # apaga banco de dados drop database 
    cursor.execute(sql)
    if con.is_connected():
        cursor.close()
        con.close()
        print("conexão ao MySql foi encerrada")
        

        '''codigo varchar(5),
        nome varchar(50),
        num  varchar(1), 
        hora varchar(1)'''
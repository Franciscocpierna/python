import mysql.connector
sql=''
con = mysql.connector.connect(host='localhost',user='root',password='')
if con.cursor():
    db_info = con.get_server_info()
    print("conectado ao servidor MySql versão ",db_info)
    cursor = con.cursor()
    #sql= ("create database processos;") # criar banco de dados
    #sql = ("drop database processos") # apaga banco de dados drop database 
    cursor.execute(sql)
if con.is_connected():
    cursor.close()
    con.close()
    print("conexão ao MySql foi encerrada")
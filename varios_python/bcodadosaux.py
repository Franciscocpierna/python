import mysql.connector
con = mysql.connector.connect(host='localhost',user='root',password='')
if con.cursor():
    db_info = con.get_server_info()
    print("conectado ao servidor MySql versão ",db_info)
    cursor = con.cursor()
    sql= ('''create database processosaux 
          default character set utf8
          default collate utf8_general_ci;
          ''') # criar banco de dados

    cursor.execute(sql)
if con.is_connected():
    cursor.close()
    con.close()
    print("conexão ao MySql foi encerrada")
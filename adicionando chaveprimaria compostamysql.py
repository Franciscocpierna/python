import mysql.connector
con = mysql.connector.connect(host='localhost',database='processos',user='root',password='')
if con.cursor():
    db_info = con.get_server_info()
    print("conectado ao servidor MySql versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print('conectado ao Banco de dados', linha)
    sql= ('alter table pross add primary key(codigo, processo, junta, cidade)'); #chave primaria composta
    cursor.execute(sql)
    if con.is_connected():
      cursor.close()
      con.close()
      print("conexão ao MySql foi encerrada")

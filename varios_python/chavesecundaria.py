import mysql.connector
sql=''
con = mysql.connector.connect(host='localhost',database='processos',user='root',password='')
if con.cursor():
    db_info = con.get_server_info()
    print("conectado ao servidor MySql versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print('conectado ao Banco de dados', linha)
    sql= ('''
         alter table pross
         add foreign key (cidade)
         references cidade(CODIGO);
    ''')  #chave estrageira formando relacionamento com pross(cidade)-> cidade(codigo) 
    cursor.execute(sql)
    if con.is_connected():
        cursor.close()
        con.close()
        print("conexão ao MySql foi encerrada")
        

       
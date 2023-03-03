import mysql.connector
con = mysql.connector.connect(host='localhost',database='cadastro',user='root',password='')
if con.cursor():
    db_info = con.get_server_info()
    print("conectado ao servidor MySql versão ",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print('conectado ao Banco de dados', linha)
sql= (
    '''select gafanhotos.nome, cursos.nome, cursos.ano
from gafanhotos left outer join cursos
on  cursos.idcurso = gafanhotos.cursopreferido
order by gafanhotos.id'''
)
cursor.execute(sql)
for id,nome,sexo  in cursor:
  print(id,nome,sexo)
'''sql = ("select idcurso,nome,descricao from cursos")
cursor.execute(sql)
for idcurso,nome,descricao in cursor:
    print(idcurso,nome,descricao)'''
if con.is_connected():
    cursor.close()
    con.close()
    print("conexão ao MySql fi encerrada")
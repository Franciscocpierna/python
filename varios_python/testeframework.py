username="Maria"
password="mariauser"

usuariosautorizados={"Maria":"mariauser", "João":"joaouser","Antonio":"Antoniouser" }
if username in  usuariosautorizados and password== usuariosautorizados[username]:
    print(f"usuario existe {username} e senha {usuariosautorizados[username]} ")
else:
    print(f"usuario não existe digitado {username} e senha = {password}")

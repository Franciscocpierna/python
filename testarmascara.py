import os
teste = input("CPF: ") # 12345678900
if len(teste) < 11:
    teste = teste.zfill(11)
    print (teste)
cpf = '{}.{}.{}-{}'.format(teste[:3], teste[3:6], teste[6:9], teste[9:])

os.system('cls')
print(f'CPF: {cpf}') # 123.456.789-00

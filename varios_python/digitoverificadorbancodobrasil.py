'''001 - BANCO DO BRASIL
Tamanho da Agência - 4 Dígitos + 1 DV
Tamanho da Conta - 8 Dígitos + 1 DV
Exemplo:
Agência: 1584-9
Conta: 00210169-6
Para obter o DV da agência, multiplica-se os quatro primeiros dígitos da
agência pelos multiplicadores 5,4,3,2 nesta ordem.
Ex:
Agência: 1584 1 5 8 4 D
Peso : 5432 5 4 3 2
 | | | |____: 8
 | | |______: 24
 | |________: 20
 |__________: 5
 -----
 57
Os valores são somados 5 + 20 + 24 + 8 = 57
O DV da Agência será, 11 subtraído da soma dos algarismos e o resto da
divisão por 11.
Mod (11) 57/11 = 2 Resto = 2 Digito = 11 - 2 = 9
Se o Resto for 10 então o DV é X
Se o Resto for 11 então o DV é 0
Para obter o DV da conta corrente, multiplicam-se os oito primeiros
dígitos da conta pelos multiplicadores 9,8,7,6,5,4,3,2 nesta ordem.
Ex:
Conta: 00210169 0 0 2 1 0 1 6 9 D
Peso : 98765432 9 8 7 6 5 4 3 2
 | | | | | | | |____: 18
 | | | | | | |______: 18
 | | | | | |________: 4
 | | | | |__________: 0
 | | | |____________: 6
 | | |______________: 14
 | |________________: 0
 |__________________: 0
 -----
 60
Os valores são somados 0 + 0 + 14 + 6 + 0 + 4 + 18 + 18 = 60
O DV da conta será, 11 subtraído da soma dos algarismos e o resto da
divisão por 11.
Mod (11) 60/11 = 5 Resto = 5 Digito = 11 - 5 = 6
Se o resultado for 10 então o DV da conta é X
Se o resultado for 11 então o DV da conta é 0
'''
def continua():
    while True:
        try:
            r=str(input('quer continuar:[S/N] ').upper()[0])
        except (KeyboardInterrupt):
            print('\n\033[31mErro: interrompeu execução\033[m')
            return 'N'
        except IndexError:
            print('\033[31mdigite opção valida S ou N: \033[m')
        else:
            if r not in "SN":
                 print('\033[31mdigite opção valida S ou N: \033[m')
            else:
                 return r


def leiaStr(msg):
  while True:
    try:
       n=str(input(msg))
       if flag != "agencia":
          if len(n) == 7:
              n='00'+ n
          if len(n) == 8:
              n= '0'+n 
    except (KeyboardInterrupt):
        print('\n\033[31mErro: interrompeu execução\033[m')
    except IndexError:
        print('\033[31mdigite opção valida S ou N: \033[m')
    else:
        if flag=="agencia":
          if  len(n) != 5 or not n[0:4].isnumeric():
             print('\033[31mdigite número valido\033[m')
          else:
             return n
        else:
           if len(n) != 9 or not n[0:8].isnumeric():
             print('\033[31mdigite número valido\033[m')
           else:
             return n
    
while True:    
 caluladigagencia=0
 calculadigconta=0
 flag="agencia"
 soma=0
 conta=''
 verificaagencia=leiaStr('Digite Agencia com número ou x se for o caso sem ponto e sem traço:') # obs fiz a lógica assimd igitando números direto, só mudar a lógica  
 agencia=verificaagencia[0:4]
 indice=0
 
 
 # calculando dig agencia XXXX-X
 for x in range(5,1,-1): #de 5 até 2   
   soma=soma + int(agencia[indice]) *  x
   indice+=1
 calculadigagencia=11-(soma % 11)
 if calculadigagencia == 10:
     agencia  = agencia+"x"
 elif calculadigagencia==11:
      agencia = agencia+"0" 
 else:
     agencia = agencia + str(calculadigagencia)

 if  verificaagencia != agencia:
      print('Você digitou o numero da agencia  errada a agencia errada ditado digito verficador não é esse')
      resp=continua()
      if resp=='N':
        break
      else:
        continue
     
 print(f'Agencia digitada foi correta igual {agencia[0:4]}' + f'-{agencia[4:5]} que é =  {verificaagencia} digitada') 
 soma = 0 
 flag=''
 verificaconta=leiaStr('Digite a Conta com número e x se for o caso sem ponto e sem traço:') # obs fiz a lógica assimd igitando

 calculadigconta=0
 indice = 0
 conta = verificaconta[0:8]
 #  calculando digito verificador da conta  
 for x in range(9,1,-1): #de 9 até 2 
    soma=soma + int(conta[indice]) *  x
    indice+=1
 # o segundo for completa a soma para determinar primeiro dígito  
 calculadigconta=11-(soma % 11)
 if calculadigconta == 10:
     conta  = conta+"x"
 elif calculadigconta ==11:
      conta = conta+"0" 
 else:
     conta= conta + str(calculadigconta)
  
  
 if  verificaconta != conta:
      print(f'Você digitou o numero da conta  errada {conta}')
 else:
      print(f'conta digitada foi correta igual {conta[0:8]}' + f'-{conta[8:9]} que é =  {verificaconta}')
   
 resp=continua()
 if resp=='N':
  break



from time import sleep 

'''Outra regra muito importante é que CPFs com números iguais como: 111.111.111-11 , 222.222.222-22 
entre outros, são CPFs válidos pelo algoritmo mas
não existem no registro oficial. Assim esse tipo de CPF não pode ser usado'
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
    except (KeyboardInterrupt):
        print('\n\033[31mErro: interrompeu execução\033[m')
    except IndexError:
            print('\033[31mdigite opção valida S ou N: \033[m')
    else:
        if len(n) != 11 or not n.isnumeric():
             print('\033[31mdigite número valido\033[m')
        else:
             return n
    
while True:    
 verifica=leiaStr('Digite o número sem ponto e sem traço:') # obs fiz a lógica assimdigitando números direto, só mudar a lógica  
 verifica1=verifica[9:11]
 nove=0
 calulaprimeiro=0
 calculasegundo=0

 soma=0
 for x in range(10,1,-1): #de 10 até 2
   soma=soma + int(verifica[nove]) *  x
   nove+=1

 calculaprimeiro=11-(soma % 11)
 if calculaprimeiro >=10:
     calclaprimeiro=0
 
 soma=0
 nove=0
 verifica = verifica[0:9]+str(calculaprimeiro)

 for x in range(11,1,-1): #de 11 até 2
   soma=soma + int(verifica[nove]) *  x
   nove+=1
 calculasegundo=11-(soma % 11)
 if calculasegundo >=10:
    calculasegundo=0
 
 verifica = verifica+str(calculasegundo)
 if verifica1==verifica[9:11]:
   verifica=verifica[0:3]+'.'+verifica[3:6]+'.'+verifica[6:9]+'-'+verifica[9:11]
   print(f'digito verificador calculado é válido: {verifica} ' )      
   verifica = verifica[0:9]+'-'+str(calculaprimeiro)+str(calculasegundo)
   print(f'digito verificador calculado é = {str(calculaprimeiro)+str(calculasegundo)}' )
 else:
   print('digito verificador calculado é inválido')    
 resp=continua()
 if resp=='N':
   break

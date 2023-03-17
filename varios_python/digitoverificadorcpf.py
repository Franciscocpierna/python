
from time import sleep 

'''No caso do CNPJ, o DV módulo 11 corresponde ao resto da divisão por 11 do somatório da multiplicação de cada algarismo da base respectivamente por 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6 e 5, a partir da unidade. O resto 10 é considerado 0 (algumas instituições, como o Banco do Brasil, tratam o 10, em seus números de contas, como "X").

O DV módulo 10 corresponde ao número que faltar para inteirar múltiplo de 10, em relação ao somatório da multiplicação de cada algarismo da base respectivamente por 2, 1, 2, 1, 2, 1 e 2, a partir da unidade, sendo que em cada multiplicação valores superiores a 9 deverão sofrer a operação "noves fora".

Veja, abaixo, exemplo de cálculo de DV módulo 11 (o mais usado pelos bancos) e de DV módulo 10 para o CNPJ nº 18781203/0001:

1  8  7  8  1  2  0  3  0  0  0  1 = 2               
x  x  x  x  x  x  x  x  x  x  x  x               
6  7  8  9  2  3  4  5  6  7  8  9            
----------------------------------                   
6+56+56+72+ 2+ 6+ 0+15+ 0+ 0+ 0+ 9 = 222÷11=20, com resto 2

1  8  7  8  1  2  0  3  0  0  0  1  2 = 8
x  x  x  x  x  x  x  x  x  x  x  x  x
5  6  7  8  9  2  3  4  5  6  7  8  9
-------------------------------------
5+48+49+64+ 9+ 4+ 0+12+ 0+ 0+ 0+ 8+18 = 217÷11=19, com resto 8

Portanto, CNPJ+DV = 18.781.203/0001-28

-------------------------------------------------------

Conferência do oitavo dígito:

1  8  7  8  1  2  0  =  3
x  x  x  x  x  x  x
2  1  2  1  2  1  2
-------------------
2+ 8+ 5*+8+ 2+ 2 +0 = 27, para 30 = 3 (*noves fora)
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

'''
1	4	5	3	8	2	2	0	6
X	X	X	X	X	X	X	X	X
10	9	8	7	6	5	4	3	2
10	36	40	21	48	10	8	0	12
10 + 36 + 40 + 21 + 48 + 10 + 8 + 0 + 12 = 185
Com esse resultado em mãos, vamos dividí-lo por 11, mas o importante para nós não é resultado, mas sim o módulo (resto) da divisão.

185 % 11 = 9
O resto da divisão é 9. Agora para calcular o dígito verificador vamos subtrair este resto do número 11:

11 - 9 = 2
Como o resultado da da subtração foi 2, o primeiro dígito verificador é igual a 2. Caso o resultado dessa divisão for 10 ou maior, o penúltimo dígito verificador será o 0.
1	4	5	3	8	2	2	0	6	2
X	X	X	X	X	X	X	X	X	X
11	10	9	8	7	6	5	4	3	2
11	40	45	24	56	12	10	0	18	4
11 + 40 + 45 + 24 + 56 + 12 + 10 + 0 + 18 + 4 = 220
Novamente vamos efetuar a divisão por 11 usando o módulo:

220 % 11 = 0
E vamos fazer a subtração:

11 - 0 = 11
Como o valor é igual ou maior que 10, o último dígito é 0.
'''
from time import sleep 
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
             print(f'vc digitou {n}')
             print('\033[31mdigite número valido\033[m')
        else:
             return n
    
verifica=leiaStr('Entre com número inteiro:.')
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
digitos=''
soma=0
nove=0
verifica = verifica[0:9]+str(calculaprimeiro)

for x in range(11,1,-1): #de 11 até 2
   soma=soma + int(verifica[nove]) *  x
   nove+=1
calculasegundo=11-(soma % 11)
if calculasegundo >=10:
    calculasegundo=0
digitos=str(calculaprimeiro)+str(calculasegundo)
verifica = verifica+str(calculasegundo)
if digitos==verifica[9:11]:
  print(f'digito verificador calculado é valido' )      
verifica = verifica[0:9]+'-'+str(calculaprimeiro)+str(calculasegundo)

print(f'digito verificador calculado é = {digitos}' )

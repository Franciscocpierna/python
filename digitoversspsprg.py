'''

Dígito verificador do RG
Isso porque cada estado tem autonomia para emitir o RG – sigla para “Registro Geral” – da maneira como quiser. Em São Paulo e no Rio de Janeiro, por exemplo, o RG segue o modelo mais comum no país: oito algarismos mais um dígito de confirmação, o tipo 12 345 678-9.
3021415
quando for 10 representa po X

No caso da carteira de identidade (o cálculo abaixo é realizado pelo SSP-SP) a seguinte rotina é utilizada:

Imagine que o RG em questão é: 23 674 985. Com isso, vamos fazer uma espécie de tabela:
236749857
2 3 6 7 4 9 8 5

x x x x x x x x

9 8 7 6 5 4 3 2

quando tem 7 números primeiro 0

Primeiro, multiplicamos cada número de cima pelo número de baixo da tabela. Seria 2×9, 3×8, e assim por diante. Com isso, temos os seguintes resultados:

18 24 42 42  20  36  24 10

O total dessa soma é 216. Por fim, dividimos por 11, resultando no valor 19,63 e o resto é arrendondado para cima, ou seja, 7. Este é nosso dígito!
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
       if len(n)==8:
           n='0'+ n   
    except (KeyboardInterrupt):
        print('\n\033[31mErro: interrompeu execução\033[m')
    except IndexError:
            print('\033[31mdigite opção valida S ou N: \033[m')
    else:
        if len(n) != 9 or not n.isnumeric():
             print('\033[31mdigite número valido\033[m')
        else:
             return n
    
while True:    
 verifica=leiaStr('Digite o número sem ponto e sem traço:') # obs fiz a lógica assimd digitando números direto, só mudar a lógica  
 
 verifica1=verifica[8:9]
 nove=0
 caluladigito=''
 soma=0
 for x in range(9,1,-1): #de 9 até 2
   soma=soma + int(verifica[nove]) *  x
   nove+=1
 
 calculadigito=str(soma % 11)
 if calculadigito ==10:
     calculadigito= 'X'
 
 nove=0
 
 verifica = verifica[0:8]+str(calculadigito)
 
 if verifica1==verifica[8:9]:
   verifica=verifica[0:2]+'.'+verifica[2:5]+'.'+verifica[5:8]+'-'+verifica[8:9]
   print(f'o numero digitado válido e formatado {verifica}') 
   print(f'digito verificador calculado é = {calculadigito}' )
 else:
   print('digito verificador calculado é inválido')    
 resp=continua()
 if resp=='N':
   break

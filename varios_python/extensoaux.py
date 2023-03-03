
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

def leiaFloat(msg):
  while True:
   try:
        n = float(input(msg))

   except (ValueError, TypeError):
          print('\033[0;31m erro: digite um numero real valido.\033[m')
          continue
   except (KeyboardInterrupt):
          print('\033[31mUsuário preferiu não digitar esse número:\033[m')
          return 0

   return n

def centavo():
    global centavos

    centavos = ''

    if cnum1[cnum1.find('.') + 1] == '0':
        if cnum1[cnum1.find('.') + 2] > '0':
            centavos = unidades[int(cnum1[cnum1.find('.') + 2])]
            if cnum1[cnum1.find('.') + 2] == '1':
                centavos = centavos + ' centavo'
            else:
                centavos = centavos + ' centavos'
    else:
        if cnum1[cnum1.find('.') + 1] == '1':
            centavos = unidonze[int(cnum1[cnum1.find('.') + 2])] + ' centavos'

        else:
            centavos = decimais[int(cnum1[cnum1.find('.') + 1])]
            if cnum1[cnum1.find('.') + 2] != '0':
               centavos = centavos + ' e ' + unidades[int(cnum1[cnum1.find('.') + 2])] + ' centavos'
            else:
               centavos = centavos + unidades[int(cnum1[cnum1.find('.') + 2])] + ' centavos'

def menorquetres(cnum):

        if len(cnum) == 1:
            cnum = '00' + cnum
            vextenso = unidades[int(cnum[2])]
            if cnum[2] > '1':
                vextenso = vextenso + ' Reais'
            else:
                 vextenso = vextenso + ' Real'
        else:
            cnum = '0' + cnum
            if cnum[1] > '1':

              vextenso =  decimais[int(cnum[1])] + ' e ' + unidades[int(cnum[2])]  + ' Reais'

            else:
              vextenso = unidonze[int(cnum[2])] + ' Reais'


        return vextenso

def nurext(*num):
    vextenso = centos[int(cnum2[0])]
    if cnum2[1:3] != "00":
        if cnum2[0] !='0':
           vextenso = vextenso + " e "

    if cnum2[1] > "1":
        vextenso = vextenso + decimais[int(cnum2[1])]
        if cnum2[2] > "0":
            vextenso = vextenso + ' e ' + unidades[int(str(cnum2[2]))]
        vextenso = vextenso
    elif cnum2[1] == "1":
        vextenso = vextenso + unidonze[int(cnum2[2])]

    elif cnum2[1:3] == "00":
        if cnum2[0] == "1":
            vextenso = "cem"
    elif cnum2[0:2] == '00':
         vextenso = vextenso + unidades[int(cnum2[2])]
    elif cnum2[2] > "0":
        vextenso = vextenso + unidades[int(cnum2[2])]
    return vextenso




unidades=["","um","doIs","tres","quaTro","cinCo","seIs","seTe","oiTo","noVe"]
unidonze=["dez","onZe","doZe","treZe","quaTorZe","quinZe","deZesSeIs","deZesSeTe","deZoiTo","deZeNoVe"]
decimais=["","","vinTe","trinTa","quaRenTa","cinQuenTa","sesSenTa","seTenTa","oiTenTa","noVenTa"]
centos=["","cenTo","duZenTos","treZenTos","quaTroCenTos","quiNhenTos","seIsCenTos","seTeCenTos","oiToCenTos","noVeCenTos"]


while True:
    numero = leiaFloat("Entre com um número:")
    cnum = str(int(numero))
    cnum1 = str(numero) + '0'
    cnumbrasil=""
    vextenso = ''
    vextenso1 = ''

    if len(cnum) < 3:
        vextenso=menorquetres(cnum)
        cnumbrasil=cnum
        #
    elif len(cnum) == 3:
       vextenso = ''
       cnum2 = cnum[0:3]
       vextenso=nurext(cnum2)
       vextenso = vextenso + ' Reais'
       cnumbrasil = cnum

    elif   4 <= len(cnum) <=6:
        cnum2 = ''
        vextenso1=''
        vextenso = ''
        if len(cnum) == 4:
            if cnum[0] == '1':
               vextenso = ' mil'
            else:
               vextenso = unidades[int(cnum[0])] + ' mil'
            if cnum[1:4]=='000':
               vextenso = vextenso + ' Reais'

            else:
                cnum2 = cnum[1:4]
                vextenso1 = nurext(cnum2)
                if cnum2[1:4] < '100':
                   vextenso = vextenso+' e ' + vextenso1 + " reais"
                else:
                   vextenso = vextenso +' e '+ vextenso1 + " reais"
            cnumbrasil = cnum[0]+'.'+cnum[1]+cnum[2]+cnum[3]
        elif len(cnum) == 5:
           if cnum[0] == '1':
              vextenso = vextenso + unidonze[int(cnum[1])] + ' mil '
           else:
              vextenso = vextenso + decimais[int(cnum[0])] + ' e '+  unidades[int(cnum[1])] + ' mil '
           cnum2 = cnum[2:5]
           vextenso1 = nurext(cnum2)
           vextenso = vextenso + vextenso1 + " reais"
           cnumbrasil = cnum[0] +cnum[1]+ '.' + cnum[2] + cnum[3] + cnum[4]
        elif len(cnum) ==6:
            cnum2 = cnum[0:3]
            vextenso = nurext(cnum2)
            vextenso = vextenso + ' Mil '
            cnum2 = cnum[3:6]
            vextenso1 = nurext(cnum2)
            vextenso = vextenso + vextenso1 + ' reais'
            cnumbrasil = cnum[0] + cnum[1] + cnum[2] +'.' + cnum[3] + cnum[4] + cnum[5]
    elif 7 <= len(cnum) <= 9:
        cnum2 = ''
        vextenso1 = ''
        vextenso = ''

        if len(cnum)==7:
          vextenso = vextenso + unidades[int(cnum[0])]
          if cnum[0] == '1':
             vextenso = vextenso + ' milhão'
          else:
            vextenso = vextenso + ' milhões'
          if cnum[1:7]=='000000':
              vextenso = vextenso + ' de Reais'
          else:
             if cnum[1:4] != '000':
                cnum2= cnum[1:4]
                vextenso1 = nurext(cnum2)
                if cnum[4:7] != '000':
                    vextenso=vextenso+ ' ' + vextenso1 +  ' mil'
                else:
                    vextenso = vextenso +' '+ vextenso1 + ' mil reais'
             if cnum[4:7] != '000':
                  cnum2=cnum[4:7]
                  vextenso1=nurext(cnum2)
                  vextenso=vextenso+' '+vextenso1+' Reais'
          cnumbrasil = cnum[0] +'.'+ cnum[1] + cnum[2] + cnum[3]+'.'+ cnum[4] + cnum[5] + cnum[6]
        elif len(cnum) == 8:
           if cnum[0] == '1':
              vextenso = vextenso + unidonze[int(cnum[1])] + ' milhões '
           else:
              vextenso = vextenso + decimais[int(cnum[0])] + ' e '+  unidades[int(cnum[1])] + ' milhões '
           if cnum[2:8] =='000000':
               vextenso = vextenso + ' de reais'
           else:
             if cnum[2:5] != '000':
               cnum2 = cnum[2:5]
               vextenso1 = nurext(cnum2)
             if cnum[5:8] != '000':
                vextenso = vextenso + vextenso1 + ' mil '
             else:
                vextenso = vextenso + vextenso1 + ' mil reais'
             if cnum[5:8] != '000':
                cnum2 = cnum[5:8]
                vextenso1 = nurext(cnum2)
                vextenso = vextenso + vextenso1 + " reais"
           cnumbrasil = cnum[0] + cnum[1] +'.' + cnum[2] + cnum[3] + cnum[4] + '.' + cnum[5] + cnum[6] + cnum[7]
        elif len(cnum)== 9:
            cnum2 = cnum[0:3]
            vextenso = nurext(cnum2)
            if cnum[3:9] == '000000':
              vextenso = vextenso + ' milhões de reais'
            else:
              vextenso = vextenso + ' Milhões '
              if cnum[3:6] != '000':
                  cnum2 = cnum[3:6]
                  vextenso1 = nurext(cnum2)
                  if cnum[6:9] != '000':
                      vextenso = vextenso + vextenso1 + ' mil '
                  else:
                      vextenso = vextenso + vextenso1 + ' mil reais'
              if cnum[6:9] != '000':
                  cnum2 = cnum[6:9]
                  vextenso1 = nurext(cnum2)
                  vextenso = vextenso + vextenso1 + " reais"
            cnumbrasil = cnum[0] + cnum[1] + cnum[2]+'.' + cnum[3] + cnum[4] + cnum[5] + '.' + cnum[6] + cnum[7] + cnum[8]
    centavo()
    if centavos != '':
       vextenso = vextenso + ' ' + centavos
       cnumbrasil = cnumbrasil + ','+cnum1[cnum1.find('.') + 1]+cnum1[cnum1.find('.')+2]
    else:
        cnumbrasil = cnumbrasil+','+'00'
    print(cnumbrasil)
    print(vextenso)
    resp = continua()
    if resp == "N":
        break





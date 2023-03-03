def soma(**ar):
   z=0
   for i in ar:
      z+= ar[i]
  
   return z


x=soma(n1=2,n2=5,n3=7,n4=9)
print(x)

def concatena(**nomes):
   z="" 
   for i in nomes:
      z+= nomes[i]
  
   return z

x = concatena(n1="Maria", n2="joao", n3="mario")
print(x)


def numeros(*num):
   z=0
   for i in num:
     z+=i
   return z   

x= numeros(1,4,10,20)
print (x)

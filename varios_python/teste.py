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

x = concatena(n1="Maria", n2="joao", n3="mario", n4="antonio")
print(x)


def numeros(*num):
   z=0
   for i in num:
     z+=i
   return z   

x= numeros(1,4,10,20)
print (x)

# trbalhando com geradores
'''def a():
   yield 20

for x in a():
   print(x)


def b():
   n=0
   while True:
      n+=1
      yield n

for i in b():
   print(i)
'''
def evens(limit=10):
   n=0
   while True:
      n+=2
      if n>limit:
        return
      yield n

def odds(limit=10):
   n=1
   while True:
      n+=2
      if n>limit:
        return
      yield n

def chain(g1, g2):
   '''for i in g1:
      yield i 
   for i in g2:
       yield i    dois for substituidos pelas linhas abaixo'''
   yield from g1
   yield from g2
#for i in chain(evens(), odds()):
#    print(i)

a= evens()
print(next(a))
print(next(a))
print(next(a))
 
  
   


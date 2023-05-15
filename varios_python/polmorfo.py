

# polimorfismo
class mae():
  def apresentacao(self):
    print("eu sou a pessoa mae")

class filha(mae):
  def apresentacao(self):
    print("eu sou a pessoa filha")

class neta(filha):
  pass
    

mae = mae()
#mae.apresentacao()
  
filha= filha()  
#filha.apresentacao()

neta = neta() 
#neta.apresentacao()

lista = [mae, filha, neta]
for x in lista:
  x.apresentacao()
   

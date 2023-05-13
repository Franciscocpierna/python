
# polimorfismo
class mae():
  def apresentacao(self):
    print("eu sou a pessoa mae")

class filha(mae):
  def apresentacao(self):
    print("eu sou a pessoa filha")

class neta(filha):
  pass
 

mae1 = mae()
mae1.apresentacao()
  
filha1= filha()  
filha1.apresentacao()

neta1 = neta() 
neta1.apresentacao()





'''class Pessoa():
  #def __init__(self,*nome):
  #    self.nome = nome
  #    self.idade = idade
  def show_data(self,nome):
    print(f"Hey meu nome é {nome}")
  

  def show_data(self,nome,idade):
    print(f"Hey meu nome é {nome} e tenho {idade} anos")
  

pessoa1 = Pessoa()
pessoa1.show_data("Victor Igor") 
#pessoa1.show_data1("Victor Igor", 18)  '''
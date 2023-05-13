# herança poo simples
#só focando a herança no exemplo
class pessoa():
    def __init__(self,nome,idade):
      self.nome = nome
      self.idade = idade
      self.classnome = self.__class__.__name__
    
    def comenta(self):
       print(f"{self.classnome} comentando ")

class aluno(pessoa): # herda da superclasse pessoa 
   def estudar(self):
      print(f"{self.classnome} estuda")
   
class professor(pessoa):# herda da superclasse pessoa 
   pass


pess = pessoa("Joana", 25)

print(pess.nome)
print(pess.idade)

alu= aluno("antonio",32)
print(alu.nome)
print(alu.idade)

prof = professor("alberto", 33)
print(prof.nome)
print(prof.idade)

alu.comenta()
prof.comenta()

alu.estudar()

# não posso fazer  pess.estudar() pessoa superclasse não herda da classe filha

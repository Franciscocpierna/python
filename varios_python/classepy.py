# exemplo simples de encapsulamento em poo
class teste():
    def __init__(self,valor):
        self.x = valor

    def get_valor(self):
        return self.x
    
    def set_valor(self,v):
        self.x = v


instteste = teste(10)
instteste1 = teste(15)

print(instteste.get_valor())
# este valor sempre sera 15 se não for alterado por set  nessa intância
print(instteste1.get_valor())
# o valor para esse objeto semppre sera 10, se não for alterado pelo set para essa instância
print(instteste.get_valor())

instteste.set_valor(5)


print(instteste.get_valor())

print(instteste1.get_valor()) # esse objeto o valor 15 




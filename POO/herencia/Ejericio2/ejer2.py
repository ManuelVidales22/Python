class Animal:
    def comer(self):
        print("El animal está comiendo.")
        
class Ave(Animal):
    def volar(self):
        print("El ave está volando.")

class Mamimero(Animal):
    def amamantar(self):
        print("El mamífero está amamantando.")

class Murcielago(Ave, Mamimero):
    pass

murcielago = Murcielago()
murcielago.comer()      # Método heredado de Animal
murcielago.volar()      # Método heredado de Ave
murcielago.amamantar()  # Método heredado de Mamimero

print(Murcielago.mro())
    
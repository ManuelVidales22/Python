class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        
    def moverse(self):
        return f"El {self.marca} se está moviendo."


class Carro(Vehiculo):
    def moverse(self):
        return f"El carro está conduciendo por la carretera es de maraca: {self.marca}."
    
class Moto(Vehiculo):
    def moverse(self):
        return f"La moto está conduciendo por la ciudad es de maraca: {self.marca}."
    

Carro = Carro("Toyota")
Moto = Moto("Honda")



Vehiculos = [Carro, Moto]

for vehiculo in Vehiculos:
    print(vehiculo.moverse())
    

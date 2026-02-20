#La abstracción se refiere a la capacidad de ocultar los detalles internos de un objeto 
# y mostrar solo la información relevante para el usuario. 
# Esto permite a los programadores centrarse en lo que un objeto hace en lugar de cómo lo hace. 

class auto:
    def __init__(self):
        self.estado = "apagado"
    
    def encender(self):
        self.estado = "encendido"
        print("El auto esta encendido")
    
    def conducir(self):
        if self.estado == "apagado":
            self.encender()
        print("El auto esta conduciendo")
    
mi_auto = auto()
mi_auto.conducir()
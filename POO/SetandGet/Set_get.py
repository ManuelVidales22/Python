class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre


manuel = Persona("Manuel", 30)

manuel.set_nombre("Manuel Gomez")
nombre = manuel.get_nombre()
print(nombre)
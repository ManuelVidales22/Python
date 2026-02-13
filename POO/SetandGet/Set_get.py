class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    "El Get y Set son metodos para obtener y modificar atributos, ya sean privados o publicos, se pueden usar para validar datos antes de asignarlos."
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
        
    def get_edad(self):
        return self._edad
    
    def set_edad(self, nueva_edad):
        self._edad = nueva_edad
        
    


manuel = Persona("Manuel", 30)

manuel.set_nombre("Manuel Gomez")
manuel.set_edad(31)
print(f"el nombre es {manuel.get_nombre()} y la edad es {manuel.get_edad()}")  
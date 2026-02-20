"""Una clase abstracta es una clase que no se puede instanciar, es decir, no se pueden crear objetos de esa clase.
Una clase abstracta se utiliza como base para otras clases, que heredan de ella y deben implementar los métodos abstractos definidos en la clase abstracta.
En Python, se puede crear una clase abstracta utilizando el módulo abc (Abstract Base Classes) y decorando la clase con @abstractmethod 
para indicar que es una clase abstracta y que los métodos decorados con @abstractmethod deben ser implementados por las clases que heredan de la clase abstracta."""

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    # El método hacer_actividad es un método abstracto, lo que significa que las clases que hereden de Persona deben implementarlo si o si 
    # al usar el decorador @abstractmethod lo que hace al metodo ser abstracto.
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")
        

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad, carrera):
        super().__init__(nombre, edad, sexo, actividad)
        self.carrera = carrera
    
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad} en la carrera de {self.carrera}")
              
manuel = Estudiante("Manuel", 20, "Masculino", "Programación", "Ingeniería en Sistemas")
manuel.hacer_actividad()
manuel.presentarse()   
    

class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.nacionalidad}")


    
#La clase empleado esta heredando todos los atributos de la clase persona        
"La palabra reservada 'pass' se utiliza en Python como un marcador de posición para indicar que no se va a agregar ningún código adicional en ese bloque." 
"En este caso, se usa para definir una clase vacía que hereda de otra clase sin agregar nuevos atributos o métodos."

class empleado(persona):
    def __init__ (self, nombre, edad, nacionalidad, trabajo, salario, horario):
        "Se utiliza super() para llamar al constructor de la clase padre (persona) y así inicializar los atributos heredados."
        super().__init__(nombre, edad, nacionalidad) 
        self.trabajo = trabajo
        self.salario = salario
        self.horario = horario

trabajador = empleado("Ana", 22, "Colombiana", "Ingeniera", 5000, "9am-5pm")
print(f"El nombre del empleado es: {trabajador.nombre} y su salario es de {trabajador.salario}" )

#trabajador.saludar()

"""Empleado esta heredando los atributos de  clase persona junto con sus metodos, se llama la clase empleado y se pasan los atributos de la clase persona.
luego se crea un objeto trabajador de la clase empleado y se imprime el nombre del empleado habiendo heredado el atributo nombre de la clase persona."""      

# Herencia jerarquica 
class estudiante(persona):  
    def __init__(self, nombre, edad, nacionalidad, carrera, semestre, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.carrera = carrera
        self.semestre = semestre
        self.universidad = universidad

alumno = estudiante("Luis", 20, "Venezonano", "Ingenieria de Sistemas", 4, "UCAB")
 
print(f"El nombre del alumno es : {alumno.nombre} y estudia {alumno.carrera}")

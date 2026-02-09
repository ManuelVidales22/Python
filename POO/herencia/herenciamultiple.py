

class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.nacionalidad}")
        
        

class artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")
        

# Herencia multiple

"""La herencia múltiple es un concepto en la programación orientada a objetos donde una clase puede heredar atributos y métodos de más de una clase padre. 
Esto permite que una clase hija combine funcionalidades de varias clases, lo que puede ser útil para modelar comportamientos complejos."""

class empleado_artista(persona, artista):
          def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
                persona.__init__(self, nombre, edad, nacionalidad)
                artista.__init__(self, habilidad)
                self.salario = salario
                self.empresa = empresa

trabajador_artista = empleado_artista("Carlos", 30, "Mexicano", "Pintura", 7000, "Arte S.A.")
trabajador_artista.mostrar_habilidad()
print(f"El nombre del empleado artista es: {trabajador_artista.nombre}, su habilidad es: {trabajador_artista.habilidad}, y su salario es de {trabajador_artista.salario} dolares al mes.")


"Consultar si una clase es subclase de otra clase"
#print(issubclass(empleado_artista, persona))  # True
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")

 
nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
grado = int(input("Ingrese el grado que esta cursando actualmente el estudiante: "))

estudiante = Estudiante(nombre,edad,grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n\n
      Nombre : {estudiante.nombre} \n 
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n
    
      """)
    
estudiante.estudiar() 

       


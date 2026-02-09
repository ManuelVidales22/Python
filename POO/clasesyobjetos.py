"""Una clase es la composicion de atributos (características)  que definen un objeto."""
#class Celular:
    # Atributos (características)
#    marca = "Samsung"
#    modelo = "Galaxy S21"
#    camara = "108 MP"
#    almacenamiento = "256 GB"
     
#Celular1 = Celular()
#Celular2 = Celular()
""" Esta clase s
""""Los objetos son instancias de una clase. Cada objeto puede tener valores diferentes para sus atributos."""

class Celular:
    def __init__(self, marca, modelo, camara, almacenamiento): # EL método __init__ es el constructor de la clase y self hace referencia al mismo objeto
        self.marca = marca
        self.modelo = modelo   
        self.camara = camara
        self.almacenamiento = almacenamiento

Celular1 = Celular("Samsung", "Galaxy S21", "108 MP", "256 GB")  
Celular2 = Celular("Apple", "iPhone 13", "12 MP", "128 GB")

""""De esta forma creamos dos objetos diferentes de la clase Celular, cada uno con sus propios atributos."""
print(Celular1.marca)          # Salida: Samsung

#Metodos son funciones definidas dentro de una clase que describen el comportamiento de los objetos de esa clase.
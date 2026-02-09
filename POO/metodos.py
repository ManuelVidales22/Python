#___________________________________________________________________________________________________________________________________________________________

#Metodos son funciones definidas dentro de una clase que describen el comportamiento de los objetos de esa clase.
class Celular:
    def __init__(self, marca, modelo, camara, almacenamiento): # EL método __init__ es el constructor de la clase y self hace referencia al mismo objeto
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        self.almacenamiento = almacenamiento
    
    #A estas funciones dentro de la clase se les llama METODOS
    def llamar(self):
        print(f"Llamando desde el {self.marca} {self.modelo}...")

    def colgar(self):
        print(f"Te estos Colgando la llamada en el {self.marca} {self.modelo}...")
        

Celular1 = Celular("Samsung", "Galaxy S21", "108 MP", "256 GB")
Celular2 = Celular("Apple", "iPhone 13", "12 MP", "128 GB")

""""De esta forma creamos dos objetos diferentes de la clase Celular, cada uno con sus propios atributos."""

Celular1.llamar()   # Salida: Llamando desde el Samsung Galaxy S21...
Celular2.colgar()   # Salida: Mi nombre es Juan y te estos Colgando la llamada en el Apple iPhone 13...
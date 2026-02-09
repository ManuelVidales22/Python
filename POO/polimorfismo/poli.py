"""
Polimorfismo es enviar un mensaje a diferentes tipos de objetos y cada uno responde de una manera diferente.
Entendendo que su atributos y metodos son diferenets, pero el mensaje es el mismo. 
Es decir, el mismo método puede tener diferentes comportamientos dependiendo del objeto que lo invoque.

"""

class Gato:
    def sonido(self):
        return "Miau"

class Perro: 
    def sonido(self):
        return "Guau"

gato = Gato()
perro = Perro()
  
def hacer_sonido(animal):
    print(animal.sonido())
    
hacer_sonido(gato)  # Salida: Miau

#______________________________________

def recorrer(elemento):
    for item in elemento:
        print(f"El elemento actual es: {item}")

lista = [1, 2, 3, 4, 5]
lista2 = "Hola Mundo"

recorrer(lista)  # Salida: El elemento actual es: 1, El elemento actual es: 2, ...
recorrer(lista2) # Salida: El elemento actual es: H, El elemento actual|

"""Esto tambien es polimorfismo, una misma funcion, se le envia un dato diferente y se comporta de manera diferente,
en este caso se le envia una lista y una cadena de texto, pero la funcion recorrer 
se adapta a ambos tipos de datos y los procesa correctamente."""
#Listas

lista = [1, 2, 3, 4, 5]  # Lista de enteros
nombres = ["Ana", "Luis", "Carlos"]  # Lista de cadenas
mezcla = [1, "Dos", 3.0, True]  # Lista con diferentes tipos de datos
#print(lista[1])
#print(nombres[2])  
#print(mezcla[3]) 
lista[3] = 10  # Modificar un elemento de la lista
print(lista)

#Tuplas

tupla = (10, 20, 30)  # Tupla de enteros
coordenadas = (40.7128, -74.0060)  # Tupla de flotantes
info = ("Ana", 25, 5.6)  # Tupla con diferentes
#print(tupla[0])
#print(coordenadas[1])
#print(info[2])

#Las tuplas no se pueden modificar directamente
#tupla[1] = 50  # Esto generará un error

#Conjuntos y con set()
conjunto = {1, 2, 3, 4, 5}  # Conjunto de enteros
frutas = {"manzana", "banana", "cereza"}  # Conjunto de cadenas

#print(conjunto)
#print(frutas)
# Los conjuntos no permiten elementos duplicados
conjunto.add(6)  # Agregar un elemento al conjunto
frutas.remove("banana")  # Eliminar un elemento del conjunto
#print(conjunto)
#print(frutas)

#Diccionarios
diccionario = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}  # Diccionario con claves y valores

print(diccionario["nombre"])
print(diccionario["edad"])
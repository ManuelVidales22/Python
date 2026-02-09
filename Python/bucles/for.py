def numero_par():
    for numero in range(1,100):
        if numero % 2 == 0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")

#numero_par()

def buscar_animal():
    animales = ["perro", "gato", "elefante", "tigre"]
    encontrado = False

    for _ in range(len(animales)):  # Máximo de intentos = cantidad de animales
        buscar = input("Ingrese el animal a buscar: ")
        
        if buscar in animales:  # ← ¡Compara con TODA la lista!
            print("Animal encontrado papacho")
            encontrado = True 
            break
        else:
            print("_____________________________________________")
            print("Sigue buscando el animal mi papacho")

    if not encontrado:
        print("No se encontró el animal después de revisar todos")
    

# Recorriendo una tupla
animales = ["perro", "gato", "elefante", "tigre", "Leon"]
colores = ("rojo", "verde", "azul", "amarillo","naranja")

#for color in colores:
#    print(f"El color es: {color}")
        
# Recorriendo dos listas al mismo tiempo
#for animal,color in zip(animales,colores):
#    print(f"El animal es:{animal}")
#    print(f"El color es:{color}")   
    

def mayore_menore():
    cont_mayores = 0
    cont_menores = 0
    
    num1 = [1,2,3,4,5,6,20,8,9,10,24,12,264,4,88]
    num2 = [16,17,18,19,7,21,22,23,11,25,13,27,28,29,30,31] 

    for n1,n2 in zip(num1,num2):
        if n1 > n2:
            cont_mayores += 1
        elif n1 < n2:
            cont_menores += 1

    print(f"Mayores: {cont_mayores}")
    print(f"Menores: {cont_menores}")
    
#mayore_menore()

#con = {"manuel": 25, "juan": 30, "luis": 28}

#for conjunto in con:
#    key = conjunto
#    value = con[conjunto]
#    print(f"Clave: {key}, Valor: {value}")

#Iterar una cadena de texto
cadena = "Manuel Antonio Vidales Duran"
for letra in cadena:
    print(letra)
    if letra == "V":
        print(f"La letra {letra} fue encontrada menor")
        break
    else:
        continue
    
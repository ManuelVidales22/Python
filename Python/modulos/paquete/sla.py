def saludo(nombre):
    return f"Hola Men, espero estes muy bien {nombre}!"

def despedida(nombre):
    return f"Adios {nombre}, que tengas un buen dia!"

def lis(lista):
    cont = 0
    val = int(input("Ingresa el número que deseas contar en la lista: "))
    for l in lista:
        if l == val:
           cont += 1
    return f"La cantidad de veces que aparece el número {val} en la lista es: {cont}"

        
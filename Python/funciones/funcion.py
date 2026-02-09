#Funcion simple 
def saludar():
    print("Hola Manuel")
    
#saludar()
def saludar(nombre, apellido):
    print(f"Hola {nombre} {apellido}")

#saludar("Manuel","Vidales")

def salud(nombre, sexo):
    sexo = sexo.lower()
    if(sexo == "hombre"):
        adjetivo = "Rey"
    elif(sexo == "mujer"):
        adjetivo = "Reina"
    else:
        adjetivo = "amor"
    
    print(f"Hola {nombre}, mi {adjetivo} ¿Como estas?")

def contraseña(num):
    char = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña =f"{char[c1]}{char[c2]}{char[c3]}{num*2}"
    return contraseña

cont = contraseña(3)
#print(f"Tu contraseña es: {cont}")

#Funcion que retorna y devulve valores 

def suma(a,b):
    return a + b

resultado = suma(10,12)
#print(f"La suma es: {resultado}")

# Recibe y retorna valores

num1 = [1,10,3,15,14,18,20,22]
num2 = [2,5,8,12,6,9,11,14]


def listas(list1, list2):
    num3 = []
    suma = 0
    for l1, l2 in zip(list1, list2):
        num3.append(l1 * l2)
        suma += l1 * l2
    print (f"La suma de los elementos multiplicados es: {suma}")    
    return num3

listass = []
listass= listas(num1, num2)
#print( f"La nueva lista de los elemntos multiuplicados es: {listass}")

#Ensayo de funcion con un datos ya definido
def pais(nombre, contontinente, ciudad = "Bogota"):
    return f"El nombre del pais es {nombre}, su capital es {ciudad} y esta ubicado en  {contontinente}"

ok = pais("Colombia", "Sur america")
#print(ok)

#Numeros primos 
def es_primo(num):
    for i in range(2,num-1):
        if num%i==0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(num):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos

resultado = primos_hasta(50)
print(f"Los numeros primos hasta el 50 son: {resultado}")

#__________________________________________________

lista = ["Manuel", "Ana", "Luis", "Carlos"]
num1, num2, num3, num4 = lista
#print(num3)







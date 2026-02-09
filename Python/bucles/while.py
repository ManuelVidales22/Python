contador = 0

#Mientras que la condicion se cumpla se ejecuta el codigo 
while contador < 10:
    contador += 1
    print(f"El contador es: {contador}")
    
def numero_par():
    numero = 1
    while numero < 100:
        if numero % 2 == 0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")
        numero += 1

numero_par()
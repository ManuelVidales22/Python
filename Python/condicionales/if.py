
#Condicional IF - else
contraseña_almcenada = "Manuel332212"

def contraseña():
    contra = str(input("Ingresa tu contraseña: "))
    if contra == contraseña_almcenada:
        print("Inicio de sesión exitoso.")
    else:
        print("Contraseña incorrecta.")

#contraseña()

#Condicional IF - elif - else
edad = int(input("Ingresa tu edad: "))
if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 65:
    print("Eres un adulto.")    
else:
    print("Eres un adulto mayor.")
    

#Condicional IF anidado
numero = int(input("Ingresa un número del 1 al 7: "))
if numero >= 1 and numero <= 7:
    if numero == 1:
        print("Lunes")
    elif numero == 2:
        print("Martes")
    elif numero == 3:
        print("Miércoles")
    elif numero == 4:
        print("Jueves")
    elif numero == 5:
        print("Viernes")
    elif numero == 6:
        print("Sábado")
    else:
        print("Domingo")

#Condiional simple IF
numero2 = int(input("Ingresa un número: "))
if numero2 % 2 == 0:
    print("El número es par.")



        
    

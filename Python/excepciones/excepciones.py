def sumar_dos():
    while True:
        a = input("Ingrese el primer número: ")
        b = input("Ingrese el segundo número: ")
        try:
            resultado = int(a) + int(b)
        except ValueError:
            print("Por favor ingrese números ")
        else:
             break  
        finally:
            print("Esto se ejecuta siempre")
            
    return resultado

print(sumar_dos())
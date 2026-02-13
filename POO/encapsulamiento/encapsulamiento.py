class Miclase:
     def __init__(self):
            self.__atributo_privado = "Valor privado"
            self.atributo_publico = "Valor público"
            
objeto = Miclase()
print(objeto.atributo_publico)  # Acceso permitido
#print(objeto.__atributo_privado)  # Error: AttributeError: 'Micl
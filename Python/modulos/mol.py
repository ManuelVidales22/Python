#from  sla import saludo, despedida, lis
#import saludo.saludar as sal
import sys
import paquete.men 

# Para importar de una clase a otra se agrega la palabra import y el nombre de la clase de la cual queremos traer los metodos
# Para importar un solo metodo se usa la palabra from seguido del nombre de la clase y la palabra import, seguida del nombre del modulo o metodo que se quiere importar
# as - se usa para darle un alias al nombre de la clase importada
#Importamos dos metodos de la clase sla.py y les damos un alias para usarlos
# con el * se importan todos los metodos de la clase sla.py

#Ejemplo:
# import sla
# import sla as salu
# from sla import saludo
# from  sla import saludo as salu, despedida as  desp 
# from  sla import *

#print(saludo("Manuel"))
#print(despedida("Jorge"))
#list = lis([1,2,3,4,5,1,2,1,1,4,5,1]) 
#print(list)

#________________________________________
#ENRUTAMIENTO DE carpetas
#Los paquetes son una forma de organizar los modulos en diferentes carpetas para tener un mejor
#Ejemplo: import saludo.saludar as sal

#print(sal.saludar_siempre("Carlos"))

#Enrutamiento entre paquetes fuera de modulos
#sys.path.append("c:\\Users\\manue\\OneDrive\\Escritorio\\Python\\funciones")
#from funcion import primos_hasta as pri

#print(pri(50))


#Enrutamiento entre paquetes dentro de modulos
#Ejemplo: import paquete.men 
#Se debe crear un archivo __init__.py dentro del paquete para que python lo reconozca como un paquete y pueda importar los modulos dentro de el
# y clases dentro de los modulos.


print(paquete.men.hola("MEn"))



 
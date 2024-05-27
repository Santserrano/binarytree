from engine.arbol import Arbol
from engine.colors import colors

cantidad = input(colors.YELLOW + "Ingresa la cantidad de elementos: ")

for i in range(int(cantidad)): 
    if (i==0): #Esto se ejecuta por unica vez para el elemento raiz
        nombre = input(colors.GREEN + "Ingresa el elemento raiz: ")
        arbol = Arbol(nombre)
    else:
        print(colors.GREEN + f'[Elemento {i}]') #Ingresa los elementos de derecha e izquierda
        nombre = input(colors.RED + "Ingresa el nombre: ")
        arbol.agregar(nombre)

print('...\n')
arbol.preorden()
arbol.inorden()
arbol.postorden()
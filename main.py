from engine.arbol import Arbol
from engine.colors import colors

cantidad = input(colors.YELLOW + "Ingresa la cantidad de elementos: " + colors.RESET)

for i in range(int(cantidad)):
    if (i==0):
        nombre = input(colors.GREEN + "Ingresa el elemento raiz: " + colors.RESET)
        arbol = Arbol(nombre)
    else:
        print(colors.GREEN + f'[Elemento {i}]'+ colors.RESET)
        nombre = input(colors.RED + "Ingresa el nombre: " + colors.RESET)
        arbol.agregar(nombre)

print('...\n')
arbol.preorden()
arbol.inorden()
arbol.postorden()
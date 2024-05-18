from engine.arbol import Arbol

cantidad = input("Ingresa la cantidad de elementos a ingresar: ")

for i in range(int(cantidad)):
    if (i==0):
        nombre = input("Ingresa el elemento raiz: ")
        arbol = Arbol(nombre)
    else:
        print(f'[Elemento {i}]')
        nombre = input("Ingresa el nombre: ")
        arbol.agregar(nombre)

print('...\n')
arbol.preorden()
arbol.inorden()
arbol.postorden()
from engine.arbol import Arbol
from engine.colors import colors

lista_nombres = ['emma', 'olivia', 'isabella', 'sofia', 'emily', 'talulah', 'candela']

arbol = Arbol("emma") #Construyo la clase con el elemento de raiz una unica vez
arbol.agregar("olivia")
arbol.agregar("isabella") #utilizo agregar para los elementos izquierdos y derechos
arbol.agregar("sofia")
arbol.agregar("emily")
arbol.agregar("talulah")
arbol.agregar("candela")

print(colors.GREEN + f'Nombres agregados: {lista_nombres}\n')
print(colors.GREEN + '...Corriendo test\n')
arbol.preorden()
arbol.inorden()
arbol.postorden()
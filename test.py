from engine.arbol import Arbol
from engine.colors import colors

lista_nombres = ['emma', 'olivia', 'isabella', 'sofia', 'emily', 'talulah', 'candela']

arbol = Arbol("emma")
arbol.agregar("olivia")
arbol.agregar("isabella")
arbol.agregar("sofia")
arbol.agregar("emily")
arbol.agregar("talulah")
arbol.agregar("candela")

print(colors.GREEN + f'Nombres agregados: {lista_nombres}\n' + colors.RESET)
print(colors.GREEN + '...Corriendo test\n' + colors.RESET)
arbol.preorden()
arbol.inorden()
arbol.postorden()
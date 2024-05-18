from engine.arbol import Arbol

lista_nombres = ['emma', 'olivia', 'isabella', 'sofia', 'emily', 'talulah', 'candela']

arbol = Arbol("emma")
arbol.agregar("olivia")
arbol.agregar("isabella")
arbol.agregar("sofia")
arbol.agregar("emily")
arbol.agregar("talulah")
arbol.agregar("candela")

print(f'Nombres agregados: {lista_nombres}\n')
print('...Corriendo test\n')
arbol.preorden()
arbol.inorden()
arbol.postorden()
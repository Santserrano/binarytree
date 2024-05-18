from engine.nodo import Nodo
from engine.colors import colors

class Arbol:
    
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izq is None:
                nodo.izq = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izq, dato)
        else:
            if nodo.der is None:
                nodo.der = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.der, dato)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izq)
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.der)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recursivo(nodo.izq)
            self.__preorden_recursivo(nodo.der)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izq)
            self.__postorden_recursivo(nodo.der)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izq, busqueda)
        else:
            return self.__buscar(nodo.der, busqueda)

    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print(colors.RED + "Imprimiendo árbol inorden: " + colors.RESET)
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print(colors.YELLOW +"Imprimiendo árbol preorden: " + colors.RESET)
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print(colors.CYAN +"Imprimiendo árbol postorden: " + colors.RESET)
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)
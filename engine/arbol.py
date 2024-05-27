from engine.nodo import Nodo #Importamos del paquete 'engine' la clase de Nodo
from engine.colors import colors #Importo el paquete de colores para las salidas en consola

#__init__.py se utiliza para que el interprete de python reconozca la carpeta como un paquete para poder importar
# el modulo en cualquier parte del codigo (reutilizar estas funciones)


class Arbol: #Clase principal
    
####################################### CONTRUIR EL ARBOL Y CARGAR DATOS ##########################
    def __init__(self, dato): #Self es la instancia de clase
        self.raiz = Nodo(dato) #Construye la clase de arbol y define la raiz con el primer nombre

    def __agregar_recursivo(self, nodo, dato): #Ingresa el nodo raiz con el dato (segundo nombre)
        if dato < nodo.dato: #Si es menor lo asigna a la izquierda (menor izquierda y mayor derecha)
            if nodo.izq is None: #Pregunta si el nodo izquierdo esta vacio
                nodo.izq = Nodo(dato) #Si esta vacio lo asigna
            else:
                self.__agregar_recursivo(nodo.izq, dato) #Caso contrario que no este vacio, 
                                                         # vuelve a llamar a la funcion (es decir, recursividad)
        else: #Es exactamente lo mismo pero pregunta por el lado derecho
            if nodo.der is None: #Pregunta si el lado derecho esta vacio
                nodo.der = Nodo(dato) #En caso de que este vacio lo asigna
            else:
                self.__agregar_recursivo(nodo.der, dato) #llama a la recursividad

##################################################################################################
#Salidas ordenadas
    def __inorden_recursivo(self, nodo): 
        if nodo is not None: #Pregunta si el nodo no esta vacio, (si esta cargado ejecuta)
            self.__inorden_recursivo(nodo.izq) #Pasa el nodo raiz como argumento
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.der)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ") #Imprime primero raiz
            self.__preorden_recursivo(nodo.izq)
            self.__preorden_recursivo(nodo.der)

    def __postorden_recursivo(self, nodo): #Prioridad al hijo izquierdo, luego al derecho y finaliza con raiz
        if nodo is not None:
            self.__postorden_recursivo(nodo.izq)
            self.__postorden_recursivo(nodo.der)
            print(nodo.dato, end=", ")

##################################################################################################
#Funcion para cargar datos
    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

############################################ SALIDAS ######################################################
    def inorden(self):
        print(colors.RED + "Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz) #Pasa como argumento la raiz 
        print("")

    def preorden(self):
        print(colors.YELLOW +"Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz) #Pasa como argumento la raiz 
        print("")

    def postorden(self):
        print(colors.CYAN +"Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz) #Pasa como argumento la raiz 
        print("")
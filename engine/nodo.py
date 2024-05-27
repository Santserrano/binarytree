class Nodo: #Se define el nodo raiz

    def __init__(self, dato): # init es el contructor de la clase
        self.dato = dato #Asigna como raiz el primer nombre, en este caso 'Emma'
        self.izq = None #Elementos vacios
        self.der = None #Elementos vacios, none es vacio
from Nodo import Nodo
class ListaDoble:
    def __init__(self):
        self.primero = None

    def insertar(self,data):
        if self.primero is None:
            self.primero = Nodo(data=data)
        else:
            actual = Nodo(data=data,anterior=self.primero)
            self.primero.siguiente = actual
            self.primero = actual


    def recorrer(self):
            if self.primero is None:
                return
            actual = self.primero
            print("nodo:", actual.data, "->")
            while actual.anterior:
                actual = actual.anterior
                print("nodo:", actual.data,"->")

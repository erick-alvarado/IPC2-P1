
from NodoSimple import NodoSimple
class ListaSimple:
    def __init__(self):
        self.primero = None

    def insertar(self,data):
        if self.primero is None:
            self.primero = NodoSimple(data=data)
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = NodoSimple(data=data)




    def buscar(self,nombre):
        actual = self.primero
        while actual and actual.data.nombre!=nombre :
          actual = actual.siguiente

        if actual is None:
          print('El nodo no existe en la lista')
        elif actual:
          print( "nombre:", actual.data.nombre)
          return actual.data

    def recorrer(self):
            if self.primero is None:
                return
            actual = self.primero
            print("nodo:", actual.data.nombre, "->")
            while actual.anterior:
                actual = actual.anterior
                print("nodo:", actual.data.nombre,"->")

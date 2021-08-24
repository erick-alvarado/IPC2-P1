import numpy as np
from Nodo import Nodo
class ListaDoble:
    def __init__(self):
        self.primero = None

    def insertar(self,data):
        if self.primero is None:
            self.primero = data
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = data


    def recorrerFinal(self):
        while self.primero.siguiente:
            self.primero = self.primero.siguiente

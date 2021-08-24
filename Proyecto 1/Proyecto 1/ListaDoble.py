import numpy as np
from Nodo import Nodo
class ListaDoble:
    def __init__(self):
        self.primero = None


    def sucesores(self,matriz, nodo):
        costototal = nodo.distanciatotal
        lista_sucesores=[]
        x = nodo.x
        y = nodo.y
        if  x+1<matriz[0].size:
           costo_derecha = matriz[y,x+1]
           lista_sucesores.append(Nodo(x+1,y,distanciatotal=costototal+costo_derecha));

        if x-1>=0:
           costo_izquierda = matriz[y,x-1]
           lista_sucesores.append(Nodo(x-1,y,distanciatotal=costototal+costo_izquierda));
        
        if y+1<matriz.size:
            costo_abajo = matriz[y+1,x]
            lista_sucesores.append(Nodo(x,y+1,distanciatotal=costototal+costo_abajo));

        if y-1<=0:
           costo_arriba = matriz[y-1,x] 
           lista_sucesores.append(Nodo(x,y-1,distanciatotal=costototal+costo_arriba));

        

        for i in range(len(lista_sucesores)):
           nodo = lista_sucesores[i]
           if(i+1<= len(lista_sucesores)):
               nodoSig = lista_sucesores[i+1]
               nodo.siguiente= nodoSig
               nodoSig.anterior= nodo

        # burbuja a lista_sucesores y retorna el nodo inicial para meterlo en la general

        return lista_sucesores[0]

    def insertar(self,data):
        if self.primero is None:
            self.primero = Nodo(data=data)
        else:
            actual = Nodo(data=data,anterior=self.primero)
            self.primero.siguiente = actual
            self.primero = actual

    def buscar(self, x,y):
        actual = self.primero
        while actual and actual.x != x and actual.y != y:
          actual = actual.siguiente
        if actual is None:
          print('El nodo no existe en la lista')
        elif actual:
          print( "nombre:", actual.nombre)
          return actual

    def recorrer(self):
            if self.primero is None:
                return
            actual = self.primero
            print("nodo:", actual.data, "->")
            while actual.anterior:
                actual = actual.anterior
                print("nodo:", actual.data,"->")

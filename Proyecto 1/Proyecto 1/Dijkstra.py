import numpy as np
from Nodo import Nodo
from ListaDoble import ListaDoble
class Dijkstra:
    def __init__(self):
        self.primero = None
    
    #def obtenerRuta(self,matriz,x_final,y_final):



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

        
        # burbuja a lista_sucesores y retorna el nodo inicial para meterlo en la general
        lista_ret = ListaDoble()

        for node in lista_sucesores:
            lista_ret.insertar(node)

        return lista_sucesores[0]

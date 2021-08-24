import numpy as np
from Nodo import Nodo
from ListaDoble import ListaDoble
class Dijkstra:
    def __init__(self):
        self.primero = None
        self.matriz = None
    
    def obtenerRuta(self,x_final,y_final):
        nodo = Nodo(x=0,y=0,distanciatotal=self.matriz[0,0])
        lista_doble = ListaDoble();
        lista_doble.insertar(nodo);

        while True:
            cabeza = lista_doble.primero
            if cabeza.x==x_final and cabeza.y==y_final:
                return cabeza
            lista_sucesores = []

            aux = cabeza
            while aux:
                lista_sucesores.append(self.sucesores(cabeza))
                aux = aux.siguiente
                
                
            self.ascendente(lista_sucesores);
            # burbuja a lista_sucesores y retorna el nodo inicial para meterlo en la general
            lista_doble.recorrerFinal()
            for node in lista_sucesores[0]:
                lista_doble.insertar(node)
            
            cabeza = cabeza.siguiente    
        print("no existe el punto");



    def ascendente(self,lista):
        
        for i in range(1,len(lista)):
            for j in range(0,len(lista)-i):
                if(lista[j+1].distanciatotal < lista[j].distanciatotal):
                    aux=lista[j];
                    lista[j]=lista[j+1];
                    lista[j+1]=aux;

    def sucesores(self, nodo):
        costototal = nodo.distanciatotal
        lista_sucesores=[]
        x = nodo.x
        y = nodo.y
        if  x+1<self.matriz[0].size:
           costo_derecha = self.matriz[y,x+1]
           lista_sucesores.append(Nodo(x+1,y,distanciatotal=costototal+costo_derecha));

        if x-1>=0:
           costo_izquierda = self.matriz[y,x-1]
           lista_sucesores.append(Nodo(x-1,y,distanciatotal=costototal+costo_izquierda));
        
        if y+1<self.matriz.size:
            costo_abajo = self.matriz[y+1,x]
            lista_sucesores.append(Nodo(x,y+1,distanciatotal=costototal+costo_abajo));

        if y-1>=0:
           costo_arriba = self.matriz[y-1,x] 
           lista_sucesores.append(Nodo(x,y-1,distanciatotal=costototal+costo_arriba));

        return lista_sucesores

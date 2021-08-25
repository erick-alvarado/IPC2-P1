import numpy as np
from Nodo import Nodo
from ListaDoble import ListaDoble
class Dijkstra:
    def __init__(self):
        self.primero = None
        self.matriz = None
    
    def obtenerRuta(self,x_inicial,y_inicial,x_final,y_final):
        nodo = Nodo(x=x_inicial,y=y_inicial,distanciatotal=self.matriz[x_inicial,y_inicial],costo= self.matriz[x_inicial,y_inicial])
        lista_doble = ListaDoble();
        lista_doble.insertar(nodo);
        cabeza = lista_doble.primero

        while cabeza:
            
            lista_sucesores = []
            aux = cabeza
            while aux:
                if aux.x==x_final and aux.y==y_final:
                    return aux
                lista_sucesores.extend(self.sucesores(aux,aux)) #no era append si no que extend
                aux = aux.siguiente
                
                
            self.ascendente(lista_sucesores);
            # burbuja a lista_sucesores y retorna el nodo inicial para meterlo en la general
            lista_doble.recorrerFinal()
            for node in lista_sucesores:
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

    def sucesores(self, nodo , nodo_anterior):
        costototal = nodo.distanciatotal
        lista_sucesores=[]
        x = nodo.x
        y = nodo.y
        if  x+1<self.matriz.shape[1] and nodo_anterior.x!=x+1:
           costo_derecha = self.matriz[y,x+1]
           lista_sucesores.append(Nodo(x+1,y,distanciatotal=costototal+costo_derecha,anterior=nodo_anterior,costo=costo_derecha));

        if x-1>=0 and nodo_anterior.x!=x-1:
           costo_izquierda = self.matriz[y,x-1]
           lista_sucesores.append(Nodo(x-1,y,distanciatotal=costototal+costo_izquierda,anterior=nodo_anterior,costo=costo_izquierda));
        
        if y+1<self.matriz.shape[0] and nodo_anterior.y!=y+1:
            costo_abajo = self.matriz[y+1,x]
            lista_sucesores.append(Nodo(x,y+1,distanciatotal=costototal+costo_abajo,anterior=nodo_anterior,costo=costo_abajo));

        if y-1>=0 and nodo_anterior.y!=y-1:
           costo_arriba = self.matriz[y-1,x] 
           lista_sucesores.append(Nodo(x,y-1,distanciatotal=costototal+costo_arriba,anterior=nodo_anterior,costo=costo_arriba));

        return lista_sucesores

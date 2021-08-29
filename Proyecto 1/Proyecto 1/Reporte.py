import numpy as np
class Reporte:
    def __init__(self,n,m):
        self.matrix = np.full((m, n), 0) 

    def getMatrix (self,nodo):
        print("Costo total:"+str(nodo.distanciatotal))
        while(nodo):
            self.matrix[nodo.y,nodo.x] = 1
            nodo = nodo.anterior
        print(self.matrix)

    
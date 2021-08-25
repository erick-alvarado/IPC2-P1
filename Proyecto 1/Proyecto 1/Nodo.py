class Nodo:
    def __init__(self,x=None,y=None,siguiente=None,anterior=None,distanciatotal=0, costo=0):
        
        self.siguiente = siguiente
        self.anterior = anterior
        self.distanciatotal=distanciatotal
        self.costo = costo
        self.x = x 
        self.y = y
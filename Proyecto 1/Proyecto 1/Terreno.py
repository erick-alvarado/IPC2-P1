import numpy as np
class Terreno:
    def __init__(self):
        self.nombre =''
        self.inicio_x =0
        self.inicio_y = 0
        self.final_x = 0
        self.final_y = 0
        self.lista_posiciones=[]

    def llenarTerrenos(self,lista):
        terreno = ''
        self.lista_posiciones = []
        i = 0
        end = len(lista)
        while i< end:
            x=lista[i];
            if(x=='terreno'):
                if(terreno==''):
                    terreno = Terreno()
                else:
                    self.terrenos.append(terreno)
                    terreno=''

            elif(x=='nombre'):
                i+=1
                terreno.nombre = lista[i]
            elif(x=='posicioninicio'):
                if(terreno.inicio_x==0):
                    i+=2
                    terreno.inicio_x = lista[i]
                    i+=3
                    terreno.inicio_y = lista[i]
            elif(x=='posicionfin'):
                if(terreno.final_x==0):
                    i+=2
                    terreno.final_x = lista[i]
                    num_rows = lista[i]
                    i+=3
                    terreno.final_y = lista[i]
                    num_cols = lista[i]

                    row = [0 for i in range(int(num_cols))]
                    self.lista_posiciones = [list(row) for i in range(int(num_rows))]


            elif(x=='posicion'):
                i+=2
                x = lista[i]

                i+=2
                y = lista[i]
                i +=1
                row = [0 for i in range(num_cols)]
                self.lista_posiciones = [list(row) for i in range(num_rows)]

            else:
                pass
            i+=1




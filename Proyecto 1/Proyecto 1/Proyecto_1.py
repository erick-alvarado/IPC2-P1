import numpy as np

from tkinter import filedialog, Tk
from Parser import Parser
from Terreno import Terreno
from ListaSimple import ListaSimple
from Dijkstra import Dijkstra
from ListaDoble import ListaDoble
from Nodo import Nodo
from Graphviz import Graphviz
from Reporte import Reporte


g = Graphviz()
p = Parser()
data = ''
terrenos =ListaSimple()
dk = Dijkstra()

def abrir():
    print("En el metodo abrir")
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo XML",
        initialdir = "./",
        filetypes = (
            ("archivos XML", "*.xml"),
            ("todos los archivos",  "*.*")
        )
    )
    if archivo is None:
        print('No se seleccionó ningun archivo\n')
        return None
    else:
        texto = archivo.read()
        archivo.close()
        print('Lectura exitosa\n')
        return texto

def prueba ():
    txt = abrir()
    if txt is not None:
        data = txt
        p.obtenerData(data.lower())
    else:
        print("Error lectura")


def llenarTerrenos(lista):
        terreno = ''
        i = 0
        end = len(lista)
        num_rows=0
        num_cols=0
        while i< end:
            x=lista[i];
            if(x=='terreno'):
                if(terreno==''):
                    terreno = Terreno()
                else:
                    terrenos.insertar(terreno)
                    terreno=''

            elif(x=='nombre'):
                i+=1
                terreno.nombre = lista[i]
            elif(x=='posicioninicio'):
                if(terreno.inicio_x==0):
                    i+=2
                    terreno.inicio_x = int(lista[i])
                    i+=3
                    terreno.inicio_y = int(lista[i])
            elif(x=='posicionfin'):
                if(terreno.final_x==0):
                    i+=2
                    terreno.final_x = int(lista[i])
                    #num_rows = abs(int(terreno.inicio_x)-int(terreno.final_x))+1
                    i+=3
                    terreno.final_y = int(lista[i])
                    #num_cols = abs(int(terreno.inicio_y)-int(terreno.final_y))+1
                    #lo bueno aqui es que en vez del 0 podes meter una clase y te mete una matrix de objetos
                    terreno.lista_posiciones = np.full((num_cols, num_rows), 0) 
                    terreno.n = num_cols
                    terreno.m = num_rows
                    num_rows = 0

            elif(x=='posicion'):
                i+=2
                x = int(lista[i])-1

                i+=2
                y = int(lista[i])-1
                i +=1

                terreno.lista_posiciones[x,y]= int(lista[i])
                i+=1
            elif(x=='dimension'):
                if num_rows==0:
                    i+=2
                    num_rows = int(lista[i])
                    i+=3
                    num_cols= int(lista[i])
            else:
                pass
            i+=1

if __name__ == "__main__":
  
    print("Bienvenido")
    opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Procesar archivos \n 3.Escribir archivo de salida \n 4.Mostrar datos del estudiante \n 5.Generar Grafica \n 6.Salir \n"))

    

    while opcion != 6:

        if opcion == 1:
            print("Opcion 1")
            prueba()
            llenarTerrenos(p.tokens)

            #Jala terreno aca hay que pedirle al usuario al terreno
            k  = terrenos.buscar("terreno1")
            

            #Setea matriz            
            dk.matriz= k.lista_posiciones
            print(dk.matriz)

            g.generarGraphviz(dk.matriz)
            ruta = dk.obtenerRuta(x_inicial=k.inicio_x-1,y_inicial=k.inicio_y-1,x_final=k.final_x-1,y_final= k.final_y-1)
            
            reporte = Reporte(k.n,k.m)
            reporte.getMatrix(ruta)

            print(terrenos[0].lista_posiciones)

            l = ListaDoble()
            node = Nodo(x=1,y=1,distanciatotal=0)
            l.sucesores(terrenos[0].lista_posiciones,node)

        elif opcion == 2: #Procesar Archivo
            pass
        elif opcion==3: #Escribir archivo de salida
            
            pass
        elif opcion==4: #Datos del estudiante
            pass
        elif opcion==5: #Generar grafica
            g.generarGraphviz()
            
            
        else:
            print("Ingrese una opcion valida")
        opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Procesar archivos \n 3.Escribir archivo de salida \n 4.Mostrar datos del estudiante \n 5.Generar Grafica \n 6.Salir \n"))


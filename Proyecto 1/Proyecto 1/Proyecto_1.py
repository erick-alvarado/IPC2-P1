import numpy as np

from tkinter import filedialog, Tk
from Parser import Parser
from Terreno import Terreno
from ListaDoble import ListaDoble

p = Parser()
data = ''
terrenos =[]

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
        p.obtenerData(data)
    else:
        print("Error lectura")


def llenarTerrenos(lista):
        terreno = ''
        i = 0
        end = len(lista)
        while i< end:
            x=lista[i];
            if(x=='terreno'):
                if(terreno==''):
                    terreno = Terreno()
                else:
                    terrenos.append(terreno)
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
                    num_rows = abs(int(terreno.inicio_x)-int(terreno.final_x))+1
                    i+=3
                    terreno.final_y = lista[i]
                    num_cols = abs(int(terreno.inicio_y)-int(terreno.final_y))+1
                    
                    #lo bueno aqui es que en vez del 0 podes meter una clase y te mete una matrix de objetos
                    terreno.lista_posiciones = np.full((num_rows, num_cols), 0) 

            elif(x=='posicion'):
                i+=2
                x = int(lista[i])-1

                i+=2
                y = int(lista[i])-1
                i +=1

                terreno.lista_posiciones[x,y]= int(lista[i])
                i+=1

            else:
                pass
            i+=1

if __name__ == "__main__":
  
    print("Bienvenido")
    opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Procesar archivos \n 3.Escribir archivo de salida \n 4.Salir \n"))

    

    while opcion != 4:

        if opcion == 1:
            print("Opcion 1")
            prueba()
            llenarTerrenos(p.tokens)
            print(terrenos[0].lista_posiciones)
        if opcion == 2:
            l = ListaDoble()
            l.insertar("1")
            l.insertar("2")
            l.insertar("3")
            l.insertar("4")
            l.insertar("5")
            l.insertar("6")

            l.recorrer();
            
        else:
            print("Ingrese una opcion valida")
        opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Reporte en consola \n 3.Exportar reporte \n 4.Salir \n"))



from tkinter import filedialog, Tk
from Parser import Parser
from Terreno import Terreno

terreno = Terreno()
p = Parser()
data = ''
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




if __name__ == "__main__":
  
    print("Bienvenido")
    opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Procesar archivos \n 3.Escribir archivo de salida \n 4.Salir \n"))

    

    while opcion != 4:

        if opcion == 1:
            print("Opcion 1")
            prueba()
            
            print(p.tokens)
            terreno.llenarTerrenos(p.tokens)
            print(terreno.lista_posiciones)

            
        else:
            print("Ingrese una opcion valida")
        opcion = int(input("Elije una opcion: \n 1.Cargar Archivo \n 2.Reporte en consola \n 3.Exportar reporte \n 4.Salir \n"))


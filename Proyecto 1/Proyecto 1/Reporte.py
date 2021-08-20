class Reporte:
    def __init__(self):
        var = 0
        valor_minimo=0

    def valor_minimo (self,lista):
        valor_max = None
        
        for x in lista:
            if (valor_max is None or x.nota < valor_max):
                valor_max = x.nota
                nom = x.nombre

        print("Nota Minima\n","El estudiante ",nom," tiene una nota de: ",valor_max)
        self.valor_minimo= valor_max
    
    def valor_maximo (self,lista):
        valor_max = None
        for x in lista:
            if (valor_max is None or x.nota > valor_max):
                valor_max = x.nota
                nom = x.nombre

        print("Nota Maxima\n","El estudiante ",nom," tiene una nota de: ",valor_max)
    
        
    def promedio(self,lista):
        promedio=0
        total=0
        for i in range (len(lista)):
            total+=float(lista[i].nota.strip())
        
        promedio=total/float(len(lista))
        print ("el promedio de notas es de:",promedio)

    
    def descendente(self,lista):

        for i in range(1,len(lista)):
            for j in range(0,len(lista)-i):
                if(lista[j+1].nota > lista[j].nota):
                    aux=lista[j].nota;
                    aux_nombre = lista[j].nombre;


                    lista[j].nota=lista[j+1].nota;
                    lista[j].nombre=lista[j+1].nombre;

                    lista[j+1].nota=aux;
                    lista[j+1].nombre=aux_nombre;

        self.printUser (lista)
        return(lista)

    def ascendente(self,lista):
        for i in range(1,len(lista)):
            for j in range(0,len(lista)-i):
                if(lista[j+1].nota < lista[j].nota):
                    aux=lista[j].nota;
                    aux_nombre = lista[j].nombre;


                    lista[j].nota=lista[j+1].nota;
                    lista[j].nombre=lista[j+1].nombre;

                    lista[j+1].nota=aux;
                    lista[j+1].nombre=aux_nombre;

        self.printUser (lista)
        return(lista)

    def printUser(self,lista):
        for x in lista:
            print(x.nombre+' '+x.nota)

    def reporte(self):
        #mandar lista de usuarios y lista de parametros

        f = open('reporte.html','w')

        mensaje = """<html>
        <head></head>
        <body><p>Reporte</p></body> ssd
        </html>"""
        mensaje = mensaje.replace("ssd",str(self.valor_minimo))
        print(mensaje);
        f.write(mensaje)
        f.close()
        print("Reporte creado con Exito")
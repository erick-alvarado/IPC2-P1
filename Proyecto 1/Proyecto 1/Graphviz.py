from os import startfile, system
import sys
import numpy as np
class Graphviz:
    def __init__(self):
        var=0

    def getNodes(self,matrix):
        txt = ""
        rank= ""
        fila = ""
        label =""

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                    label+=" A"+str(j)+"_"+str(i) + '[ label = "'+str(matrix[i][j])+'"]'
                    label+=' \n '


        for i in range(len(matrix)):
            rank+= " rank=same {"
            for j in range(len(matrix[i])):
                if(j== len(matrix[0])-1):
                        rank+="A"+str(j)+"_"+str(i)
                else:
                        rank+="A"+str(j)+"_"+str(i) + " -- "
            rank+="} \n"


        for j in range(len(matrix[i])):
            
            for i in range(len(matrix)):
                    if(i==len(matrix)-1):
                        fila+=" A"+str(j)+"_"+str(i)
                    else:
                        fila+=" A"+str(j)+"_"+str(i) + " -- "
            fila+=' \n '

        

        txt = label+fila+rank

        return txt 
    def generarGraphviz(self,matrix):
        graphviz='''
        graph grid
        {
	        layout=dot
	        label="Terreno"
	        labelloc = "t"
	        node [shape=plaintext]

	        edge [weight=1000 style=dashed color=dimgrey]
            
        '''

        graphviz+=self.getNodes(matrix)
        graphviz+="}"

        miArchivo = open('graphviz.dot','w')
        miArchivo.write(graphviz)
        miArchivo.close()

        system('dot -Tpng graphviz.dot -o graphviz.png')
        system('cd ./graphviz.png')
        startfile('graphviz.png')
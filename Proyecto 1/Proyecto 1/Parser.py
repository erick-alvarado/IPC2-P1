from Terreno import Terreno


class Parser:
    def __init__(self):
        self.tokens = []
        self.terrenos = []


    def obtenerData(self,data):
        estado = 0 #curso
        aux = ''
        for x in data:
            if(estado==0):
                if(x == '=' or x == ' ' or x == '<'or x == '>' or x == '/' or x == '\r' or x == '\t' or x == '\n'): #Ignorar
                    pass   
                elif(x.isalpha()):
                    aux +=x
                    estado = 1
                elif(x.isdigit()):
                    aux +=x
                    estado = 3
                elif(x == '"'):
                    estado = 2
                elif(x =='<'):
                    estado = 1
                else:
                    #habia codigo de mas aqui
                    pass
            elif (estado ==1):
                if(x.isalpha()):
                    aux+=x
                else:
                    self.tokens.append(aux);
                    aux = '' 
                    estado = 0 
                    
            elif(estado ==2):
                if(x!='"'):
                    aux+=x
                else:
                    self.tokens.append(aux);
                    aux = ''  
                    estado = 0
            elif(estado==3):
                if(x.isdigit()):
                    aux+=x
                else:
                    self.tokens.append(aux);
                    aux = ''  
                    estado = 0
                


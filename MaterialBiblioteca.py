

#Clase materialbilbioteca
#atributos
#-titulo,autor,ID,estado
#Metodos
#Prestarmaterial()
#devolverlo()
#Mostrar su informacion()

import random

class MatBiblioteca():

    def nuevoID(self):
        #8 digitos
        #primeros digitos 
        digitos =  hex(random.randint(10000000,90000000))[2:9]
        #ultimos 2 digitos
        Lista = ["A", "B", "C", "D", "E", "F"]
        digitos2 = random.choice(Lista) + random.choice(Lista)
        newID = digitos + digitos2
        return newID[-8:]
        

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.ID = self.nuevoID()
        self.estado = "Disponible"

    

    def gettitulo (self):
        return self.titulo

    def getautor (self)  :
        return self.autor
    
    def getID (self):
        return self.ID
    
    def getestado (self):
        return self.estado
    
    def settitulo (self, txttitulo):
        self.titulo = txttitulo
        return True

    def setmodelo (self, txtmodelo):
        self.modelo = txtmodelo
        return True
    
    def setestado (self, txtestado):
        self.estado = txtestado
        return True


    def prestar(self):
        if self.estado == "Disponible":
            self.estado = "Prestado"
            return True
        else:
            return False
        
    def devolver(self):
        if self.estado == "Prestado":
            self.estado = "Disponible"
            return True
        else:
            return False

    def mostrarinfo():
        print("mostrar info")
        pass
    

    def contardias(self,fechaP, mesD,diaD):
        mesP = fechaP[0]
        diaP = fechaP[1]
        diastotal = 0

        if (mesD - mesP) == 0:
            #Contar dias
            diastotal = diaD - diaP
        elif (mesD - mesP) == 1:
            #Contar dias para terminar mes (31 dias)
            diastotal = 31-diaP
            #Contar dias del mes siguiente
            diastotal += diaD
        else:
            diastotal=999
        
        return diastotal
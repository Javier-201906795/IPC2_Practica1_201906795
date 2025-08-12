

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
        

    def __init__(self, titulo, autor, estado):
        self.titulo = titulo
        self.modelo = autor
        self.ID = self.nuevoID()
        self.estado = estado

    

    def gettitulo (self):
        return self.titulo

    def getmodelo (self)  :
        return self.modelo
    
    def getID (self):
        return self.ID
    
    def getestado (self):
        return self.estado



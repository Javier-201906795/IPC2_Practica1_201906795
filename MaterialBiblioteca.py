

#Clase materialbilbioteca
#atributos
#-titulo,autor,ID,estado
#Metodos
#Prestarmaterial()
#devolverlo()
#Mostrar su informacion()

import random

class MatBiblioteca():

    def __init__(self, titulo, autor, estado):
        self.titulo = titulo
        self.modelo = autor
        self.ID = random.randint(1000,90000)
        self.estado = estado

    def gettitulo (self):
        return self.titulo

    def getmodelo (self)  :
        return self.modelo
    
    def getID (self):
        return self.ID
    
    def getestado (self):
        return self.estado



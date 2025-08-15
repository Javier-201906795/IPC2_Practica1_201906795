

#Clase libro digital hijo de materialbibloteca
#atributos
#-tamaño del archivo
#Metodos
#Prestar < 3 dias ()

from MaterialBiblioteca import MatBiblioteca

class LibDigital(MatBiblioteca):
    def __init__(self, titulo, autor, tamanoarchivo):
        super().__init__(titulo, autor)
        self.tamanoarchivo = tamanoarchivo
        self.fechaprestamo = None

    
    def mostrarinfo(self):
        return f"Titulo: {self.gettitulo()}, Autor: {self.getmodelo()}, ID: {self.getID()}, Estado: {self.getestado()}, Tamaño Archivo: {self.tamanoarchivo} MB, Libro: Digital."
    
    def prestarLibro(self, mes, dia):
        if self.estado == "Disponible":
            #Clase madre
            self.prestar()
            #Almacenar fecha
            self.fechaprestamo = [mes, dia]
            return True
        else:
            return False

    
    def devolverLibro(self, mes, dia):
        if self.estado == "Prestado":
            #-Contar Dias
            diasprestado = self.contardias(self.fechaprestamo, mes, dia)
            print(f"Dias Prestado:{diasprestado}")
            #Validar fecha de entrega
            if diasprestado <= 3:
                #Clase madre
                self.devolver()
                return True
            else:
                #Clase madre
                self.devolver()
                return False
            
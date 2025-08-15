from MaterialBiblioteca import MatBiblioteca

#Clase libro fisico hijo de materialbibloteca
#atributos
#-Numero de ejemplar
#Metodos
#Prestar < 7 dias ()


class LibFisico(MatBiblioteca):
    def __init__(self, titulo, autor, numejemplar):
        super().__init__(titulo, autor)
        self.numejemplar = numejemplar
        self.fechaprestamo = [0,0]

    def gettitulolibro(self):
        return self.gettitulo()

    def getfechaprestamo(self):
        return f"Fecha Prestamo: mes:{self.fechaprestamo[0]} - dia:{self.fechaprestamo[1]}"

    def getnumeroejemplar(self):
        return self.numejemplar

    def getTipo(self):
        return "Fisico"

    def mostrarinfo(self):
        return f"ID: {self.getID()}, Titulo: {self.gettitulo()}, Autor: {self.getautor()}, Estado: {self.getestado()}, Ejemplar: {self.numejemplar}, Libro: Fisico, Fecha Prestamo: mes:{self.fechaprestamo[0]} - dia:{self.fechaprestamo[1]}"

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
            if diasprestado <= 7:
                #Clase madre
                self.devolver()
                self.fechaprestamo = [0,0]  # Reset the loan date
                return True
            else:
                #Clase madre
                self.devolver()
                self.fechaprestamo = [0,0]  # Reset the loan date
                return False
            
            


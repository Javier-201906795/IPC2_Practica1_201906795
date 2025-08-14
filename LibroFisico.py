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
        self.fechaprestamo = None

    def gettitulolibro(self):
        return self.gettitulo()
    
    def mostrarinfo(self):
        return f"Titulo: {self.gettitulo()}, Autor: {self.getmodelo()}, ID: {self.getID()}, Estado: {self.getestado()}, Ejemplar: {self.numejemplar}, Libro: Fisico."
    
    def prestarLibro(self, mes, dia):
        if self.estado == "Disponible":
            #Clase madre
            self.prestar()
            #Almacenar fecha
            self.fechaprestamo = [mes, dia]
            return True
        else:
            return False
        
    
    def contardias(self,mesD,diaD):
        mesP = self.fechaprestamo[0]
        diaP = self.fechaprestamo[1]
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

    
    def devolverLibro(self, mes, dia):
        if self.estado == "Prestado":
            
            #-Contar Dias
            diasprestado = self.contardias(mes,dia)
            print(f"Dias Prestado:{diasprestado}")
            #Validar fecha de entrega
            if diasprestado <= 7:
                #Clase madre
                self.devolver()
                return True
            else:
                return False
            
            


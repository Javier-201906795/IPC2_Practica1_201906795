from MaterialBiblioteca import MatBiblioteca

#Clase libro fisico hijo de materialbibloteca
#atributos
#-Numero de ejemplar
#Metodos
#Prestar < 7 dias ()


class LibFisico(MatBiblioteca):
    def __init__(self, titulo, autor, ID, estado, numejemplar):
        super().__init__(titulo, autor, ID, estado)
        self.numejemplar = numejemplar

    def gettitulolibro(self):
        return self.gettitulo()
        
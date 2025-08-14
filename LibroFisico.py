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

    def gettitulolibro(self):
        return self.gettitulo()
        
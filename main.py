from LibroFisico import LibFisico
from LibroDigital import LibDigital
import random
#Base de datos
DB = []

#Registra nuevo material ()
#Prestar ()
#Devolver()
#Consultarinfo()


print("Practica 1")
print("nuevo libro")
Libro1 = LibFisico("El principito", "Desconocido",  1)
Libro2 = LibDigital("El hombre araña", "marvel",  15)


def consultarLibros():
    for libro in DB:
        print(libro.mostrarinfo())


def LibroTituloAutor():
    titulo = str(input("Titulo: "))
    autor = str(input("Autor: "))
    return titulo, autor



def Verificarsiexiste(ID):
    for libro in DB:
        if libro.getID() == ID:
            return True
    return False


def Gestionar():
    opcion = 0
    try:
        while opcion != 9:
            print("*"*25)
            print("*"+" "*4+"MENU GESTIONAR"+" "*5+"*")
            print("*"*25)
            print("*"+" 1). Ver Libros"+" "*8+"*")
            print("*"+" 2). Prestar Libro"+" "*5+"*")
            print("*"+" 3). Devolver Libro"+" "*4+"*")
            print("*"+" 9). Regresar"+" "*10+"*")
            print("*"*25)
            opcion = int(input("> "))
            match opcion:
                case 1:
                    print(">Ver Libro Disponibles")
                    consultarLibros()
                case 2:
                    print(">Prestar Libro")
                    idlibro = str(input("ID del libro a prestar: "))
                    # Verificar si el libro existe
                    existelibro = Verificarsiexiste(idlibro)
                    
                            
                    if existelibro == False:
                        print("El libro no existe.")   
                    else:
                        #Si existe, Preguntar Fecha Actual
                        mes = int(input("Mes Actual: "))
                        #Validar mes
                        if mes < 1 or mes > 12:
                            print("Mes no válido. Debe ser entre 1 y 12.")
                            mes = int(input("Mes Actual: "))
                        dia = int(input("Día Actual: "))
                        #Validar dia
                        if dia < 1 or dia > 31:
                            print("Día no válido. Debe ser entre 1 y 31.")
                            dia = int(input("Día Actual: "))
                        #Buscar y prestar libro
                        for libro in DB:
                            if libro.getID() == idlibro:
                                libro.prestarLibro(mes,dia)
                                break
                    

                case 3:
                    print(">Devolver Libro")
                    idlibro = str(input("ID del libro a devolver: "))
                    # Verificar si el libro existe
                    existelibro = Verificarsiexiste(idlibro)

                case 9:
                    print(">Regresar")
                    break
    except:
        print("Opción no válida.")


def Registrar():
    opcion = 0
    try:
        while opcion != 9:
            print("*"*31)
            print("*"+" "*8+"MENU REGISTRAR"+" "*7+"*")
            print("*"*31)
            print("*"+" 1). Registrar Libro FISICO"+" "*2+"*")
            print("*"+" 2). Registrar Libro DIGITAL"+" "*1+"*")
            print("*"+" 9). Regresar"+" "*16+"*")
            print("*"*31)
            opcion = int(input("> "))
            match opcion:
                case 1:
                    print(">Registrar Libro FISICO")
                    titulo, autor = LibroTituloAutor()
                    numejemplar = int(input("Numero de ejemplar: "))
                    DB.append(LibFisico(titulo, autor,  numejemplar))
                    print(DB[-1].mostrarinfo())
                case 2:
                    print(">Registrar Libro DIGITAL")
                    print(">Registrar Libro FISICO")
                    titulo, autor = LibroTituloAutor()
                    tamaño = int(input("Tamaño archivo (MB): "))
                    DB.append(LibDigital(titulo, autor,  tamaño))
                    print(DB[-1].mostrarinfo())
                case 9:
                    print("Fin")
                    break
    except:
        print("Opción no válida.")



def Menu():
    opcion = 0
    try:
        while opcion != 9:
            print("*"*25)
            print("*"+" "*9+"MENU"+" "*9+"*")
            print("*"*25)
            print("*"+" 1). Registrar Libro"+" "*2+"*")
            print("*"+" 2). Gestionar Libro"+" "*2+"*")
            print("*"+" 9). Salir"+" "*12+"*")
            print("*"*25)
            opcion = int(input("> "))
            match opcion:
                case 1:
                    print(">Registrar Libro")
                    Registrar()
                case 2:
                    print(">Gestionar Libro")
                    Gestionar()
                case 9:
                    print("Fin")
                    break
    except:
        print("Opción no válida.")

    


if __name__ == "__main__":  
    Menu()






#####################################################

# print(Libro2.gettitulo())
# print(Libro2.getID())


# print(Libro2.getestado())

# print(Libro2.prestar())

# print(Libro2.getestado())
# print(Libro2.prestar())

# print(Libro2.devolver())

# print(Libro2.getestado())

# print(Libro2.devolver())

# print(Libro2.mostrarinfo())

# print(Libro2.prestarLibro(1,5))
# print(Libro2.getestado())
# print(Libro2.devolverLibro(1,7))
# print(Libro2.mostrarinfo())

# print(Libro2.prestarLibro(1,29))
# print(Libro2.getestado())
# print(Libro2.devolverLibro(2,1))


# print(Libro2.prestarLibro(1,30))
# print(Libro2.getestado())
# print(Libro2.devolverLibro(2,15))


#####################################################

# print(Libro1.gettitulolibro())
# print(Libro1.gettitulo())
# print(Libro1.getID())


# print(Libro1.getestado())

# print(Libro1.prestar())

# print(Libro1.getestado())
# print(Libro1.prestar())

# print(Libro1.devolver())

# print(Libro1.getestado())

# print(Libro1.devolver())

# print(Libro1.mostrarinfo())

# print(Libro1.prestarLibro(1,5))
# print(Libro1.getestado())
# print(Libro1.devolverLibro(1,10))

# print(Libro1.prestarLibro(1,29))
# print(Libro1.getestado())
# print(Libro1.devolverLibro(2,1))


# print(Libro1.prestarLibro(1,30))
# print(Libro1.getestado())
# print(Libro1.devolverLibro(2,15))




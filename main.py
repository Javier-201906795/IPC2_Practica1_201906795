from LibroFisico import LibFisico
from LibroDigital import LibDigital
import random
#Base de datos


#Registra nuevo material ()
#Prestar ()
#Devolver()
#Consultarinfo()


print("Practica 1")
print("nuevo libro")
Libro1 = LibFisico("El principito", "Desconocido",  1)
Libro2 = LibDigital("El hombre araña", "marvel",  15)




def Registrar():
    opcion = 0
    try:
        while opcion != 9:
            print("*"*25)
            print("*"+" "*4+"MENU REGISTRAR"+" "*4+"*")
            print("*"*25)
            print("*"+" 1). Registrar Libro"+" "*2+"*")
            print("*"+" 2). Gestionar Libro"+" "*2+"*")
            print("*"+" 9). Regresar"+" "*9+"*")
            print("*"*25)
            opcion = int(input("> "))
            match opcion:
                case 1:
                    print("Registrar Libro")
                case 2:
                    print("Gestionar Libro")
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
                    print("Registrar Libro")
                    Registrar()
                case 2:
                    print("Gestionar Libro")
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




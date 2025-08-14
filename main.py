from LibroFisico import LibFisico
import random
#Base de datos


#Registra nuevo material ()
#Prestar ()
#Devolver()
#Consultarinfo()


print("Practica 1")
print("nuevo libro")
Libro1 = LibFisico("El principito", "Desconocido",  1)
print(Libro1.gettitulolibro())
print(Libro1.gettitulo())
print(Libro1.getID())

print(Libro1.setestado("Prestado"))
print(Libro1.getestado())





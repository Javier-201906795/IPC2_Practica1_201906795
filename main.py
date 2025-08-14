from LibroFisico import LibFisico
import random
#Base de datos


#Registra nuevo material ()
#Prestar ()
#Devolver()
#Consultarinfo()


print("Practica 1")
print("nuevo libro")
Libro1 = LibFisico("El principito", "Desconocido", "Libre", 1)
print(Libro1.gettitulolibro())
print(Libro1.gettitulo())
print(Libro1.getID())

print(Libro1.setestado(False))
print(Libro1.getestado())





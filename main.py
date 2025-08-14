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


print(Libro1.getestado())

print(Libro1.prestar())

print(Libro1.getestado())
print(Libro1.prestar())

print(Libro1.devolver())

print(Libro1.getestado())

print(Libro1.devolver())

print(Libro1.mostrarinfo())

print(Libro1.prestarLibro(1,5))
print(Libro1.getestado())
print(Libro1.devolverLibro(1,10))

print(Libro1.prestarLibro(1,29))
print(Libro1.getestado())
print(Libro1.devolverLibro(2,1))


print(Libro1.prestarLibro(1,30))
print(Libro1.getestado())
print(Libro1.devolverLibro(2,15))




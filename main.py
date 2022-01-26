#INSTANCIAS OBJETOS? O CREAR LOS OBJETOS Y GUARDARLOS EN UNA LISTA
from Archivero import *
from Cajon import *
from Carpeta import *
from Documento import *


ArchiveroUno = Archivero(1, "Universidad Tecnologica de Torreon")
print(type(ArchiveroUno))

Cajon1 = Cajon(1, "A")
Cajon2 = Cajon(2, "B")
print(type(Cajon1))
print(type(Cajon2))

# Cajon3 = Cajon(3, "C")

Carpeta1 = Carpeta(1, "Carpeta Uno")
Carpeta2 = Carpeta(2, "Carpeta Dos")
Carpeta3 = Carpeta(3, "Carpeta Tres")
print(type(Carpeta1))
print(type(Carpeta2))
print(type(Carpeta3))

# Carpeta4 = Carpeta(4, "Carpeta Cuatro")
# Carpeta5 = Carpeta(5, "Carpeta Cinco")
# Carpeta6 = Carpeta(6, "Carpeta Seis")

Archivo1 = Documento(1, "Documento Uno", "Texto" )
Archivo2 = Documento(2, "Documento Uno", "Texto" )
Archivo3 = Documento(3, "Documento Uno", "Texto" )
Archivo4 = Documento(4, "Documento Uno", "Texto" )
print(type(Archivo1))
print(type(Archivo2))
print(type(Archivo3))
print(type(Archivo4))
# Archivo5 = Documento(5, "Documento Uno", "Texto" )
# Archivo6 = Documento(6, "Documento Uno", "Texto" )
# Archivo7 = Documento(7, "Documento Uno", "Texto" )
# Archivo8 = Documento(8, "Documento Uno", "Texto" )
# Archivo9 = Documento(9, "Documento Uno", "Texto" )
# Archivo10 = Documento(10, "Documento Uno", "Texto" )
# Archivo11 = Documento(11, "Documento Uno", "Texto" )
# Archivo12 = Documento(12, "Documento Uno", "Texto" )

ArchiveroUno.CreateAddCajones(Cajon1, Cajon2)
# print("Cajones De Archivero: ",ArchiveroUno.ListaCajones[:])

Cajon1.CreteAddCarpetas(Carpeta1)
Cajon2.CreteAddCarpetas(Carpeta2, Carpeta3)
# print("Carpetas Del Cajon Uno",Cajon1.ListaCarpetas[:])
# print("Carpetas Del Cajon Dos",Cajon2.ListaCarpetas[:])
# Cajon3.CreteAddCarpetas(Carpeta4, Carpeta5, Carpeta6)

Carpeta1.CreteAddDocumentos(Archivo1)
Carpeta2.CreteAddDocumentos(Archivo2, Archivo4)
# print("Documentos De La Carpeta Uno",Carpeta1.ListaDocumento[:])
# print("Documentos De La Carpeta Uno",Carpeta2.ListaDocumento[:])
# Carpeta3.CreteAddDocumentos(Archivo2, Archivo4)
# Carpeta4.CreteAddDocumentos(Archivo5, Archivo6)
# Carpeta5.CreteAddDocumentos(Archivo7, Archivo8, Archivo9)
# Carpeta6.CreteAddDocumentos(Archivo10, Archivo11, Archivo12)

ArchiveroUno.ReadArciveroAll()
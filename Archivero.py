from Cajon import *

class Archivero: 
     
    #PROPIEDADES DE INSTANCIA
    idArchivero = 0
    NombreArchivero = ""
    ListaCajones = []

    #PROPIEDAD STATIC
    ArchiverosLista = []

    #CONSTRUCTOR
    def __init__(self, ida, Nombre):
        self.idArchivero = ida
        self.NombreArchivero = Nombre
        self.ListaCajones = []

    #METODOS - CRUD
    ####################################################CRETE##############################################################
    
    def CreateAddCajones(self, *Cajones):
        for i in Cajones:
            self.ListaCajones.append(i)

    ####################################################READ##############################################################

    #METODO READ STATICO BY ID
    @classmethod
    def ReadArchiverosById(cls, idA):
        Contador = 0
        idA = int(idA)

        for i in cls.ArchiverosLista:
            if i.idArchivero == idA:
                return Contador
            else:
                Contador = Contador + 1
        
        Contador = -1
        return Contador
        
        
    #METODO DE INSTANCIA MUESTRA TODO
    def ReadArciveroAll(self):
        print("\"id\": "+str(self.idArchivero)+",")
        print("\"Nombre Archivero\": \""+str(self.NombreArchivero)+"\",")

        print("\"Cajones\": [", )

        for i in self.ListaCajones:

            i.ReadCajonAll()
           
            print("     ]")

            print("     },")

        print("     ]")

    def ReadOnlyArchiveroById(self):
        print("             {")
        print("             \"id\": "+str(self.idArchivero)+"")
        print("             \"Nombre Archivero\": \""+str(self.NombreArchivero)+"\",")
        print("             \"Cajones\": []", )
        print("             }")


    ####################################################UPDATE##############################################################

    def UpdateArchivero(self, Nombre): 
        # print("Modificar Nombre Del Archivero")
        # Nombrex = input("Nuevo Nombre: ") 
        self.NombreArchivero = Nombre

    ####################################################DELETE##############################################################

    def DeleteArchivero(self):
        del(self) 

    def Eliminar(self,NombreCajon):  
        self.ListaCajones.remove(NombreCajon)
        print(self.ListaCajones[:])

    @classmethod
    def DeleteDocumento(cls, idA):
        ObjetoArchivero = cls.ReadDocumentosById(idA)
        if ObjetoArchivero > -1:
            cls.DocumentosLista[ObjetoArchivero].ReadOnlyArchiveroById()
            cls.DocumentosLista.pop(ObjetoArchivero)
        else:
            print(f"No Exite el Archivero con Id: {idA}")  

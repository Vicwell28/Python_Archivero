from Cajon import *

class Archivero: 
    pass 
    #PROPIEDADES
    idArchivero = ""
    NombreArchivero = ""
    ListaCajones = []

    #Propiedad Static
    ArchiverosLista = []

    #CONSTRUCTOR
    def __init__(self, id, Nombre):
        self.idArchivero = id
        self.NombreArchivero = Nombre
        self.ListaCajones = []

    #METODOS - CRUD
    ####################################################CRETE##############################################################
    
    def CreateAddCajones(self, *Cajones):
        for i in Cajones:
            self.ListaCajones.append(i)

    ####################################################READ##############################################################
    def ReadCajonById(self, id):
        Contador = 0

        for i in self.ListaCajones:
            if i.idCajon == id:
                return Contador
                
            else:
                Contador = Contador + 1
        
        Contador = -1
        return Contador
        
        
    
    def ReadArciveroAll(self):
        print("\"id\": "+str(self.idArchivero)+",")
        print("\"Nombre\": \""+str(self.NombreArchivero)+"\",")

        print("\"Cajones\": [", )

        for i in self.ListaCajones:

            i.ReadCajonAll()
           
            print("     ]")

            print("     },")

        print("     ]")

    ####################################################UPDATE##############################################################

    def UpdateArchivero(self, Nombre): 
        # print("Modificar Nombre Del Archivero")
        # Nombrex = input("Nuevo Nombre: ") 
        self.NombreArchivero = Nombre

    ####################################################DELETE##############################################################

    def DeleteArchivero(self):
        del(self) 


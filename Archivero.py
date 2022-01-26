from Cajon import *

class Archivero: 
    pass 
    #PROPIEDADES
    idArchivero = ""
    NombreArchivero = ""
    ListaCajones = []

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

    def UpdateArchivero(): 
        pass


    ####################################################DELETE##############################################################

    def DeleteArchivero(id):
        pass


from Documento import *

class Carpeta: 
    #PROPIEDADES
    idCarpeta = 0
    NombreCarpeta = ""
    ListaDocumento = []

    #CONSTRUCTOR
    def __init__(self, id, Nombre):
        self.idCarpeta = id
        self.NombreCarpeta = Nombre
        self.ListaDocumento = []


    #METODOS - CRUD
    ####################################################CRETE##############################################################
    
    def CreteAddDocumentos(self, *Documentos):
        for i in Documentos:
            self.ListaDocumento.append(i)

    ####################################################READ##############################################################
    
    def ReadArciveroId(id):
        pass

    def ReadCarpetaAll(self):

        print("         {")
        print("         \"id\":",self.idCarpeta,",")
        print("         \"Nombre\": \"",self.NombreCarpeta,"\",")
        print("         \"Documentos\": [")

        for y in self.ListaDocumento:
            
            y.ReadDocumentoAll()

        print("         ]")

        print("         },")

    ####################################################UPDATE##############################################################

    def UpdateCarpeta(): 
        pass


    ####################################################DELETE##############################################################

    def DeleteCarpeta(id):
        pass


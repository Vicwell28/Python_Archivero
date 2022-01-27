from Documento import *

class Carpeta: 
    #PROPIEDADES DE INSTANCIA
    idCarpeta = 0
    NombreCarpeta = ""
    ListaDocumento = []

    #PROPIEDAD STATIC
    CarpetasLista = []

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
    
    @classmethod
    def ReadCarpetasById(cls, id):
        Contador = 0

        for i in cls.CarpetasLista:
            if i.idCarpeta == id:
                return Contador
            else:
                Contador = Contador + 1
        
        Contador = -1
        return Contador

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

    def UpdateCarpeta(self, Nombre):
        self.NombreCarpeta = Nombre 

    ####################################################DELETE##############################################################

    def DeleteCarpeta(id):
        pass


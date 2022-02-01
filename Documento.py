
from typing import Text

class Documento:
    #PROPIEDADES DE INSTANCIA
    idDocumento = 0
    NombreDocumento = ""
    TextDocumento = ""

    #PROPIEDAD STATIC
    DocumentosLista = []

    #CONSTRUCTOR
    def __init__(self, id, Nombre, Texto):
        self.idDocumento = id 
        self.NombreDocumento = Nombre
        self.TextDocumento = Texto

    #METODOS - CRUD
    ####################################################CRETE##############################################################

    ####################################################READ##############################################################
    @classmethod
    def ReadDocumentosById(cls, id):
        Contador = 0

        for i in cls.DocumentosLista:
            if i.idDocumento == id:
                return Contador
            else:
                Contador = Contador + 1
        
        Contador = -1
        return Contador

    def ReadDocumentoAll(self):
        print("             {")
        print("             \"id\": "+str(self.idDocumento)+"")
        print("             \"Nombre\": \""+str(self.NombreDocumento)+"\",")
        print("             \"Texto\": \""+str(self.TextDocumento)+"\"")
        print("             },")

    
    def ReadOnlyDocumentoById(self):
        print("             {")
        print("             \"id\": "+str(self.idDocumento)+"")
        print("             \"Nombre\": \""+str(self.NombreDocumento)+"\",")
        print("             \"Texto\": \""+str(self.TextDocumento)+"\"")
        print("             }")

    ####################################################UPDATE##############################################################

    def UpdateDocumento(self, Nombre, Texto): 
        self.NombreDocumento = Nombre
        self.TextDocumento = Texto

    ####################################################DELETE##############################################################

    @classmethod
    def DeleteDocumento(cls, idA):
        ObjetoArchivero = cls.ReadDocumentosById(idA)
        if ObjetoArchivero > -1:
            cls.DocumentosLista[ObjetoArchivero].ReadOnlyArchiveroById()
            cls.DocumentosLista.pop(ObjetoArchivero)
        else:
            print(f"No Exite el Archivero con Id: {idA}")  
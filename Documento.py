
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
        print("             \"id\": \"", self.idDocumento,"\",")
        print("             \"Nombre\": \"", self.NombreDocumento,"\",")
        print("             \"Texto\": \"", self.TextDocumento,"\"")
        print("             },")

    ####################################################UPDATE##############################################################

    def UpdateDocumento(self, Nombre, Texto): 
        self.NombreDocumento = Nombre
        self.TextDocumento = Texto


    ####################################################DELETE##############################################################

    def DeleteDocumento(self):
        del self


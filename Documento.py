
from typing import Text


class Documento:
    #PROPIEDADES
    idDocumento = 0
    NombreDocumento = ""
    TextDocumento = ""

    #Propiedad Static
    DocumentosLista = []

    #CONSTRUCTOR
    def __init__(self, id, Nombre, Texto):
        self.idDocumento = id 
        self.NombreDocumento = Nombre
        self.TextDocumento = Texto

    #METODOS - CRUD
    ####################################################CRETE##############################################################

    ####################################################READ##############################################################

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


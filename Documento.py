
from typing import Text


class Documento:
    #PROPIEDADES
    idDocumento = 0
    NombreDocumento = ""
    TextDocumento = ""

    #CONSTRUCTOR
    def __init__(self, id, Nombre, Texto):
        self.idDocumento = id 
        self.NombreDocumento = Nombre
        self.TextDocumento = Texto

    #METODOS - CRUD
    ####################################################CRETE##############################################################
    
    # def CreteDocumento(self, *Cajones):
    #     for i in Cajones:
    #         self.ListaCajones.append(i)

    ####################################################READ##############################################################
    
    def ReadArciveroId(id):
        pass

    def ReadDocumentoAll(self):
        print("             {")
        print("             \"id\": \"", self.idDocumento,"\",")
        print("             \"Nombre\": \"", self.NombreDocumento,"\",")
        print("             \"Texto\": \"", self.TextDocumento,"\"")
        print("             },")

    ####################################################UPDATE##############################################################

    def UpdateDocumento(): 
        pass


    ####################################################DELETE##############################################################

    def DeleteDocumento(id):
        pass


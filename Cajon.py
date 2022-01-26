from Carpeta import *

class Cajon: 
    #PROPIEDADES
    idCajon = 0
    SeccionCajon = ""
    ListaCarpetas = []

    #CONSTRUCTOR
    def __init__(self, id, Seccion):
        self.idCajon = id
        self.SeccionCajon = Seccion
        self.ListaCarpetas = []

    #METODOS - CRUD
    ####################################################CRETE##############################################################
    
    def CreteAddCarpetas(self, *Carpetas):
        for i in Carpetas:
            self.ListaCarpetas.append(i)

    ####################################################READ##############################################################
    
    def ReadCajonId(id):
        pass

    def ReadCajonAll(self):
        print("     {")
        print("     \"id\": ", self.idCajon,",")
        print("     \"Seccion\": \"", self.SeccionCajon,"\",")
        print("     \"Carpetas\": [", )

        for j in self.ListaCarpetas:
            
            j.ReadCarpetaAll()

    ####################################################UPDATE##############################################################

    def UpdateCajon(): 
        pass


    ####################################################DELETE##############################################################

    def DeleteCajon(id):
        pass


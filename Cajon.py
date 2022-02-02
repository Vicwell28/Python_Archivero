from Carpeta import *

class Cajon: 
    #PROPIEDADES DE INSTANCIA 
    idCajon = 0
    SeccionCajon = ""
    ListaCarpetas = []

    #PROPIEDAD STATIC
    CajonesLista = []

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
    
    #METODO STATICO READ BY ID
    @classmethod
    def ReadCajonById(cls, id):
        Contador = 0

        for i in cls.CajonesLista:
            if i.idCajon == id:
                return Contador
            else:
                Contador = Contador + 1
        
        Contador = -1
        return Contador

    #METODO DE INSTANCIA READ ALL
    def ReadCajonAll(self):
        print("     {")
        print("     \"id\": "+str(self.idCajon)+"")
        print("     \"Seccion Caja\": \""+str(self.SeccionCajon)+"\",")
        print("     \"Carpetas\": [", )

        for j in self.ListaCarpetas:
            
            j.ReadCarpetaAll()

    def ReadOnlyCajonById(self):
        print("             {")
        print("             \"id\": "+str(self.idCajon)+"")
        print("             \"Seccion Cajon\": \""+str(self.SeccionCajon)+"\",")
        print("             \"Carpetas\": []", )
        print("             }")

    ####################################################UPDATE##############################################################

    def UpdateCajon(self, Seccion): 
        self.SeccionCajon = Seccion

    ####################################################DELETE##############################################################

    def DeleteCajon(self):
        pass


from Carpeta import *

class Cajon: 
    #PROPIEDADES
    idCajon = 0
    SeccionCajon = ""
    ListaCarpetas = []

    #Propiedad Static
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
    
    def ReadCarpetasById(self ,id):
        fContador = 0

        for i in self.ListaCarpetas:
            if i.idCarpeta == id:
                return Contador
                
            else:
                Contador = Contador + 1
        
        Contador = -1
        return Contador

    def ReadCajonAll(self):
        print("     {")
        print("     \"id\": ", self.idCajon,",")
        print("     \"Seccion\": \"", self.SeccionCajon,"\",")
        print("     \"Carpetas\": [", )

        for j in self.ListaCarpetas:
            
            j.ReadCarpetaAll()

    ####################################################UPDATE##############################################################

    def UpdateCajon(self, Seccion): 
        self.SeccionCajon = Seccion


    ####################################################DELETE##############################################################

    def DeleteCajon(self):
        pass


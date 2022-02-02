from Carpeta import *

class Cajon: 
    #PROPIEDADES DE INSTANCIA 
    idCajon = 0
    SeccionCajon = ""
    ListaCarpetas = []

    #PROPIEDAD STATIC
    TablaCajones = []

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

    @classmethod
    def CreateCajon(cls, idCajon, Seccion):
        if idCajon > 0 and Seccion != "":
            Seccion = cls(idCajon, Seccion)
            cls.TablaCajones.append(Seccion)
            print(cls.TablaCajones[len(cls.TablaCajones)-1].ReadOnlyCajonById())
        else: 
            print("Haz introducido el id o nombre incorrectamente")

    @classmethod
    def CrateAddCarpetas(cls, idCajon):
        if idCajon > -1:
            ObjetoCajon = cls.BuscarCajonById(idCajon)
            if ObjetoCajon > -1:
                print("¿Que Carpetas Quieres Agregar?")
                ArrayCarpetas = input("Respuesta: ")
                for i in ArrayCarpetas:
                    ObjetoCarpeta = Carpeta.BuscarCarpetaById(int(i))
                    if ObjetoCarpeta > -1: 
                        cls.TablaCajones[ObjetoCajon].ListaCarpetas.append(int(Carpeta.TablaCarpeta[ObjetoCarpeta].idCarpeta))
                        print(f"Se Agrego La Carpeta Con Id: {i}")
                    else: 
                        print(f"No Se Agrego La Carpeta Con Id: {i} Por Que No Exite")
            else:
                print(f"No Exite El Cajon con Id: {idCajon}")
        else:   
            print(f"No Se Puede Buscar Un Cajon Con id: {idCajon} Negativa")

    ####################################################READ##############################################################
    #METODO STATICO READ BY ID
    @classmethod
    def BuscarCajonById(cls, idCajon):
        Contador = 0
        idCajon = int(idCajon)
        for i in cls.TablaCajones:
            if i.idCajon == idCajon:
                return Contador
            else:
                Contador = Contador + 1
        
        Contador = -1
        return Contador

    #METODO DE INSTANCIA MUESTRA TODO
    def ReadCajonAll(self):
        print("\"id\" : "+str(self.idCajon)+",")
        print("\"Seccion Cajon\" : \""+str(self.SeccionCajon)+"\",")
        print("\"Cajones\" : [", )

        for i in self.ListaCarpetas:
            POS = Carpeta.BuscarCarpetaById(int(i))
            if POS > -1: 
                Carpeta.TablaCarpeta[POS].ReadCarpetaAll()
                print("               ]")
                print("     },")
                print("     ]")

    def ReadOnlyCajonById(self):
        print("             {")
        print("             \"id\": "+str(self.idCajon)+"")
        print("             \"Seccion Cajon\": \""+str(self.SeccionCajon)+"\",")
        print("             \"Carpetas\": []", )
        print("             }")

    @classmethod
    def MostrarTodasLosCajones(cls):
        for i in cls.TablaCajones:
            print("{")
            print("\"id\": "+str(i.idCajon)+"")
            print("\"Seccion Cajon\": \""+str(i.SeccionCajon)+"\",")
            print("\"Carpetas\": []", )
            print("}")


    ####################################################UPDATE##############################################################
    def UpdateCajon(self, Seccion): 
        self.SeccionCajon = Seccion

    @classmethod
    def UpdateCajonById(cls, idCajon):
        if idCajon > -1:
            ObjetoCajon = cls.ReadOnlyCajonById(idCajon)
            if ObjetoCajon > -1:
                newNombre = input("Agregar Nuevo Nombre: ")
                cls.TablaCajones[ObjetoCajon].UpdateCajon(newNombre)
                cls.TablaCajones[ObjetoCajon].ReadOnlyCajonById() 
            else:
                print(f"No Exite El Cajon Con Id: {idCajon}")  
        else:
            print("No Se Puede Actualizar Un Cajon Con Id Negativo")

    ####################################################DELETE##############################################################
    @classmethod
    def DeleteArchivero(cls, idCajon):
        if idCajon > -1: 
            ObjetoCajon = cls.ReadOnlyCajonById(idCajon)
            if ObjetoCajon > -1:
                cls.TablaCajones[ObjetoCajon].ReadOnlyArchiveroById()
                cls.TablaCajones.pop(ObjetoCajon)
                print(f"Se Ha Eliminado Correctamente El Cajon Con id: {idCajon}")
            else:
                print(f"No Exite El Cajon con Id: {idCajon}")  
        else:
            print("No Se Puede Actualizar Un Cajon Con Id Negativo")
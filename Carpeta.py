from Documento import *

class Carpeta: 
    #PROPIEDADES DE INSTANCIA
    idCarpeta = 0
    NombreCarpeta = ""
    ListaDocumento = []

    #PROPIEDAD STATIC
    TablaCarpeta = []

    #CONSTRUCTOR
    def __init__(self, idCarpeta, Nombre):
        self.idCarpeta = idCarpeta
        self.NombreCarpeta = Nombre
        self.ListaDocumento = []

    #METODOS - CRUD
    ####################################################CRETE##############################################################
    
    def CreteAddDocumentos(self, *Documentos):
        for i in Documentos:
            self.ListaDocumento.append(i)

    @classmethod
    def CreateCarpeta(cls, idCarpeta, Nombre):
        if idCarpeta > 0 and Nombre != "":
            Nombre = cls(idCarpeta, Nombre)
            cls.TablaCarpeta.append(Nombre)
            print(cls.TablaCarpeta[len(cls.TablaCarpeta)-1].ReadOnlyCarpetaById())
        else: 
            print("Haz introducido el id o nombre incorrectamente")

    def AddCajones(self, *Cajones):
        for i in Cajones:
            self.ListaCajones.append(i)

    @classmethod
    def CrateAddDocumentos(cls, idCarpeta):
        if idCarpeta > -1:
            ObjetoCarpeta = cls.BuscarCarpetaById(idCarpeta)
            if ObjetoCarpeta > -1:
                print("¿Que Documentos Quieres Agregar?")
                ArrayDocumentos = input("Respuesta: ")
                for i in ArrayDocumentos:
                    ObjetoDocumento = Documento.BuscarDocumentoById(int(i))
                    if ObjetoDocumento > -1: 
                        cls.TablaCarpeta[ObjetoCarpeta].ListaCajones.append(int(Documento.TablaDocumento[ObjetoDocumento].idDocumento))
                        print(f"Se Agrego El Documento Con Id: {i}")
                    else: 
                        print(f"No Se Agrego El Cajon Con Id: {i} Por Que No Exite")
            else:
                print(f"No Exite el Carpeta con Id: {idCarpeta} {ObjetoCarpeta}")
        else:   
            print(f"No Se Puede Buscar Un Carpeta Con id: {idCarpeta} Negativa")

    ####################################################READ##############################################################
    
    @classmethod
    def BuscarCarpetaById(cls, idCarpeta):
        Contador = 0
        idCarpeta = int(idCarpeta)
        for i in cls.TablaCarpeta:
            if i.idCarpeta == idCarpeta:
                return Contador
            else:
                Contador = Contador + 1
        
        Contador = -1
        return Contador

    def ReadCarpetaAll(self):
        print("         {")
        print("         \"id\": "+str(self.idCarpeta)+"")
        print("         \"Seccion Caja\": \""+str(self.NombreCarpeta)+"\",")
        print("         \"Documentos\": [")

        for y in self.ListaDocumento:
            POS = Carpeta.BuscarCarpetaById(int(y))
            if POS > -1: 
                Documento.TablaDocumento[POS].ReadDocumentoAll()
                print("                  ]")
                print("                  },")

    def ReadOnlyCarpetaById(self):
        print("             {")
        print("             \"id\": "+str(self.idCarpeta)+"")
        print("             \"Nombre Carpeta\": \""+str(self.NombreCarpeta)+"\",")
        print("             \"Cajones\": []", )
        print("             }")

    @classmethod
    def MostrarTodasLasCarpetas(cls):
        for i in cls.TablaCarpeta:
            print("{")
            print("\"id\": "+str(i.idCarpeta)+"")
            print("\"Nombre Carpeta\": \""+str(i.NombreCarpeta)+"\",")
            print("\"Cajones\": []", )
            print("}")

        
    ####################################################UPDATE##############################################################

    def UpdateCarpeta(self, Nombre):
        self.NombreCarpeta = Nombre 

    @classmethod
    def UpdateCarpetaById(cls, idCarpeta):
        if idCarpeta > -1:
            ObjetoCarpeta = cls.BuscarCarpetaById(idCarpeta)
            if ObjetoCarpeta > -1:
                newNombre = input("Agregar Nuevo Nombre: ")
                cls.TablaCarpeta[ObjetoCarpeta].UpdateCarpeta(newNombre)
                cls.TablaCarpeta[ObjetoCarpeta].ReadOnlyCarpetaById() 
            else:
                print(f"No Exite el Carpeta con Id: {idCarpeta}")  
        else:
            print("No Se Puede Actualizar Un Carpeta Con Id Negativo")

    ####################################################DELETE##############################################################

    @classmethod
    def DeleteCarpeta(cls, idCarpeta):
        if idCarpeta > -1: 
            ObjetoCarpeta = cls.BuscarCarpetaById(idCarpeta)
            if ObjetoCarpeta > -1:
                cls.TablaCarpeta[ObjetoCarpeta].ReadOnlyCarpetaById()
                cls.TablaCarpeta.pop(ObjetoCarpeta)
                print(f"Se Elimino La Carpeta Con id: {idCarpeta}")
            else:
                print(f"No Exite el Carpeta con Id: {idCarpeta}")  
        else:
            print("No Se Puede Actualizar Un Carpeta Con Id Negativo")
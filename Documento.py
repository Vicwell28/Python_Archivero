from typing import Text

class Documento:
    #PROPIEDADES DE INSTANCIA
    idDocumento = 0
    NombreDocumento = ""
    TextDocumento = ""

    #PROPIEDAD STATIC
    TablaDocumento = []

    #CONSTRUCTOR
    def __init__(self, id, Nombre, Texto):
        self.idDocumento = id 
        self.NombreDocumento = Nombre
        self.TextDocumento = Texto

    #METODOS - CRUD
    ####################################################CRETE##############################################################
    @classmethod
    def CreateDocumento(cls, idDocumento, Nombre, Texto):
        if idDocumento > 0 and Nombre != "" and Texto != "":
            Nombre = cls(idDocumento, Nombre, Texto)
            cls.TablaDocumento.append(Nombre)
            print(cls.TablaDocumento[len(cls.TablaDocumento)-1].ReadOnlyDocumentoById())
        else: 
            print("Haz introducido el id o nombre incorrectamente")

    ####################################################READ##############################################################
    @classmethod
    def BuscarDocumentoById(cls, idDocumento):
        Contador = 0
        int(idDocumento) 
        for i in cls.DocumentosLista:
            if i.idDocumento == idDocumento:
                return Contador
            else:
                Contador = Contador + 1
        
        Contador = -1
        return Contador

    @classmethod
    def ReadDocumento(cls, IdDocumento, Opcion): 
        if  IdDocumento > -1:
            if Opcion == 2: 
                POS = cls.BuscarDocumentoById(IdDocumento)
                if  POS > -1: 
                    cls.TablaDocumento[POS].ReadDocumentoAll()
                else: 
                    print("No Se Encontro El Documento Con Id: {IdDocumento}")
            elif Opcion == 1:
                POS = cls.BuscarCarpetaById(IdDocumento)
                if  POS > -1: 
                    cls.TablaDocumento[POS].ReadOnlyDocumentoById()
                else: 
                    print("No Se Encontro EL Documento Con Id: {IdDocumento}")
        else: 
            print("No Se Puede Leer Carpeta Con Un id Negativo")



    def ReadDocumentoAll(self):
        print("             {")
        print("             \"id\": "+str(self.idDocumento)+"")
        print("             \"Nombre Documento\": \""+str(self.NombreDocumento)+"\",")
        print("             \"Texto\": \""+str(self.TextDocumento)+"\"")
        print("             },")

    #METODO DE INSTANCIA MUESTRA SOLO PROPIEDADES DEL OBJETO
    def ReadOnlyDocumentoById(self):
        print("             {")
        print("             \"id\": "+str(self.idDocumento)+"")
        print("             \"Nombre Documento\": \""+str(self.NombreDocumento)+"\",")
        print("             \"Texto\": \""+str(self.TextDocumento)+"\"")
        print("             }")

    @classmethod
    def MostrarTodosLosDocumentos(cls):
        for i in cls.TablaDocumento:
            print("{")
            print("\"id\": "+str(i.idDocumento)+"")
            print("\"Nombre Documento\": \""+str(i.NombreDocumento)+"\",")
            print("\"Texto\": \""+str(i.TextDocumento)+"\"")
            print("}")
            
    ####################################################UPDATE##############################################################

    def UpdateDocumento(self, Nombre, Texto): 
        self.NombreDocumento = Nombre
        self.TextDocumento = Texto

    @classmethod
    def UpdateDocumentoById(cls, idDocumento):
        if idDocumento > -1:
            ObjetoDocumento = Documento.BuscarDocumentoById(idDocumento)
            if ObjetoDocumento > -1:
                newNombre = input("Agregar Nuevo Nombre: ")
                newTexto = input("Agregar Nuevo Texto: ")
                cls.TablaDocumento[ObjetoDocumento].UpdateDocumento(newNombre, newTexto)
                cls.TablaDocumento[ObjetoDocumento].ReadOnlyDocumentoById() 
            else:
                print(f"No Exite el Archivero con Id: {idDocumento}")  
        else:
            print("No Se Puede Actualizar Un Archivero Con Id Negativo")

    ####################################################DELETE##############################################################
    @classmethod
    def DeleteDocumento(cls, idDocumento):
        if idDocumento > -1:
            ObjetoDocumento = cls.BuscarDocumentoById(idDocumento)
            if ObjetoDocumento > -1:
                print("Se Elimino El Siguiente Documento")
                cls.DocumentosLista[ObjetoDocumento].ReadOnlyArchiveroById()
                cls.DocumentosLista.pop(ObjetoDocumento)
                print("Se Elimino El Documento Con Id {idDocumento}")
            else:
                print(f"No Exite el Archivero con Id: {idDocumento}")  
        else: 
            print("No Se Puede Actualizar Un Archivero Con Id Negativo")
from Cajon import *

class Archivero: 
    #PROPIEDADES DE INSTANCIA
    idArchivero = 0
    NombreArchivero = ""
    ListaCajones = []

    #PROPIEDAD STATIC
    TablaArchivero = []

    #CONSTRUCTOR
    def __init__(self, ida, Nombre):
        self.idArchivero = ida
        self.NombreArchivero = Nombre
        self.ListaCajones = []

    ####################################################CRETE##############################################################
    @classmethod
    def CreateArchivero(cls, idA, Nombre):
        if idA > 0 and Nombre != "":
            Nombre = cls(idA, Nombre)
            cls.TablaArchivero.append(Nombre)
            print(cls.TablaArchivero[len(Archivero.TablaArchivero)-1].ReadOnlyArchiveroById())
        else: 
            print("Haz introducido el id o nombre incorrectamente")

    def AddCajones(self, *Cajones):
        for i in Cajones:
            self.ListaCajones.append(i)

    @classmethod
    def CrateAddCajones(cls, idArchivero):
        if idArchivero > -1:
            ObjetoArchivero = cls.BuscarArchiveroById(idArchivero)
            if ObjetoArchivero > -1:
                print("¿Que Cajones Quieres Agregar?")
                ArrayCajones = input("Respuesta: ")
                for i in ArrayCajones:
                    ObjetoCajon = Cajon.BuscarCajonById(int(i))
                    if ObjetoCajon > -1: 
                        cls.TablaArchivero[ObjetoArchivero].ListaCajones.append(int(Cajon.CajonesLista[ObjetoCajon].idCajon))
                        print(f"Se Agrego El Cajon Con Id: {i}")
                    else: 
                        print(f"No Se Agrego El Cajon Con Id: {i} Por Que No Exite")
            else:
                print(f"No Exite el Archivero con Id: {idArchivero} {ObjetoArchivero}")
        else:   
            print(f"No Se Puede Buscar Un Archivero Con id: {idArchivero} Negativa")

    ####################################################READ##############################################################
    #METODO READ STATICO BY ID
    @classmethod
    def BuscarArchiveroById(cls, idArchivero):
        Contador = 0
        idArchivero = int(idArchivero)
        for i in cls.TablaArchivero:
            if i.idArchivero == idArchivero:
                return Contador
            else:
                Contador = Contador + 1
        
        Contador = -1
        return Contador
        
    #METODO DE INSTANCIA MUESTRA TODO
    def ReadArciveroAll(self):
        print("\"id\" : "+str(self.idArchivero)+",")
        print("\"Nombre Archivero\" : \""+str(self.NombreArchivero)+"\",")
        print("\"Cajones\" : [", )

        for i in self.ListaCajones:
            POS = Cajon.BuscarCajonById(int(i))
            if POS > -1: 
                Cajon.TablaCajones[POS].ReadCajonAll()
                print("               ]")
                print("     },")
                print("     ]")
                
    #METODO DE INSTANCIA MUESTRA SOLO PROPIEDADES DEL OBJETO
    def ReadOnlyArchiveroById(self):
        print("             {")
        print("             \"id\": "+str(self.idArchivero)+"")
        print("             \"Nombre Archivero\": \""+str(self.NombreArchivero)+"\",")
        print("             \"Cajones\": []", )
        print("             }")

    @classmethod
    def MostrarTodasLosCajones(cls):
        for i in cls.TablaCajones:
            print("{")
            print("\"id\": "+str(i.idArchivero)+"")
            print("\"Nombre Archivero\": \""+str(i.NombreArchivero)+"\",")
            print("\"Cajones\": []", )
            print("}")


    ####################################################UPDATE##############################################################
    def UpdateArchivero(self, Nombre): 
        self.NombreArchivero = Nombre

    @classmethod
    def UpdateArchiveroById(cls, idArchivero):
        if idArchivero > -1:
            ObjetoArchivero = Archivero.BuscarArchiveroById(idArchivero)
            if ObjetoArchivero > -1:
                newNombre = input("Agregar Nuevo Nombre: ")
                cls.TablaArchivero[ObjetoArchivero].UpdateArchivero(newNombre)
                cls.TablaArchivero[ObjetoArchivero].ReadOnlyArchiveroById() 
            else:
                print(f"No Exite el Archivero con Id: {idArchivero}")  
        else:
            print("No Se Puede Actualizar Un Archivero Con Id Negativo")
      
    ####################################################DELETE##############################################################
    @classmethod
    def DeleteArchivero(cls, idArchivero):
        if idArchivero > -1: 
            ObjetoArchivero = cls.BuscarArchiveroById(idArchivero)
            if ObjetoArchivero > -1:
                cls.TablaArchivero[ObjetoArchivero].ReadOnlyArchiveroById()
                cls.TablaArchivero.pop(ObjetoArchivero)
                print(f"Se Ha Eliminado Exitosamente El Archivero Con id: {idArchivero}")
            else:
                print(f"No Exite el Archivero con Id: {idArchivero}")  
        else:
            print("No Se Puede Actualizar Un Archivero Con Id Negativo")
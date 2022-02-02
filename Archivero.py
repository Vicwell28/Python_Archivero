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

    #METODOS - CRUD
    ####################################################CRETE##############################################################
    @classmethod
    def CreateArchivero(cls, idA, Nombre):
        if idA > 0 and Nombre > 0:
            Nombre = cls(idA, Nombre)
            cls.ArchiverosLista.append(Nombre)
            print(cls.ArchiverosLista[len(Archivero.ArchiverosLista)-1].ReadOnlyArchiveroById())

    def AddCajones(self, *Cajones):
        for i in Cajones:
            self.ListaCajones.append(i)

    @classmethod
    def CrateAddCajones(cls, idA):
        if idA > -1:
            ObjetoArchivero = cls.BuscarArchiveroById(idA)
            if ObjetoArchivero > -1:
                print("¿Que Cajones Quieres Agregar?")
                ArrayCajones = input("Respuesta: ")
                for i in ArrayCajones:
                    ObjetoCajon = Cajon.BuscarCajonById(int(i))
                    if ObjetoCajon > -1:
                        cls.TablaArchivero[ObjetoArchivero].ListaCajones.append(Cajon.CajonesLista[ObjetoCajon].idCajon)
                        print(f"Se Agrego El Cajon Con Id: {i}")
                    else: 
                        print(f"No Se Agrego El Cajon Con Id: {i} Por Que No Exite")
            else:
                print(f"No Exite el Archivero con Id: {idA} {ObjetoArchivero}")
        else:   
            print(f"No Se Puede Buscar Un Archivero Con id: {idA} Negativa")

    ####################################################READ##############################################################

    #METODO READ STATICO BY ID
    @classmethod
    def BuscarArchiveroById(cls, idA):
        Contador = 0
        for i in cls.ArchiverosLista:
            if i.idArchivero == idA:
                return Contador
            else:
                Contador = Contador + 1
        
        Contador = -1
        return Contador
        
        
    #METODO DE INSTANCIA MUESTRA TODO
    def ReadArciveroAll(self):
        print("\"id\": "+str(self.idArchivero)+",")
        print("\"Nombre Archivero\": \""+str(self.NombreArchivero)+"\",")
        print("\"Cajones\": [", )

        for i in self.ListaCajones:
            POS = Cajon.BuscarCajonById(int(i))
            if POS > -1: 
                Cajon.CajonesLista[POS].ReadCajonAll()
                print("     ]")
                print("     },")
                print("     ]")
                

    #METODO DE INSTANCIA MUESTRA SOLO PROPIEDADES DEL OBJETO
    def ReadOnlyArchiveroById(self):
        print("             {")
        print("             \"id\": "+str(self.idArchivero)+"")
        print("             \"Nombre Archivero\": \""+str(self.NombreArchivero)+"\",")
        print("             \"Cajones\": []", )
        print("             }")

    ####################################################UPDATE##############################################################

    def UpdateArchivero(self, Nombre): 
        self.NombreArchivero = Nombre

    @classmethod
    def UpdateArchiveroById(cls, idA):
        if idA > -1:
            ObjetoArchivero = Archivero.ReadArchiverosById(idA)
            if ObjetoArchivero > -1:
                newNombre = input("Agregar Nuevo Nombre: ")
                cls.TablaArchivero[ObjetoArchivero].UpdateArchivero(newNombre)
                cls.TablaArchivero[ObjetoArchivero].ReadOnlyArchiveroById() 
            else:
                print(f"No Exite el Archivero con Id: {idA}")  
        else:
            print("No Se Puede Actualizar Un Archivero Con Id Negativo")
      

    ####################################################DELETE##############################################################
    @classmethod
    def DeleteArchivero(cls, idA):
        if idA > -1: 
            ObjetoArchivero = cls.BuscarArchiveroById(idA)
            if ObjetoArchivero > -1:
                cls.TablaArchivero[ObjetoArchivero].ReadOnlyArchiveroById()
                cls.TablaArchivero.pop(ObjetoArchivero)
            else:
                print(f"No Exite el Archivero con Id: {idA}")  
        else:
            print("No Se Puede Actualizar Un Archivero Con Id Negativo")
    
    

from Cajon import *

class Archivero: 
    pass 
    #PROPIEDADES
    idArchivero = ""
    NombreArchivero = ""
    ListaCajones = []

    #CONSTRUCTOR
    def __init__(self, id, Nombre):
        self.idArchivero = id
        self.NombreArchivero = Nombre
        self.ListaCajones = []

    #METODOS - CRUD
    ####################################################CRETE##############################################################
    
    def CreateAddCajones(self, *Cajones):

        for i in Cajones:
            self.ListaCajones.append(i)

    ####################################################READ##############################################################
    
    def ReadArciveroAll(self):
        print("\"id\": "+str(self.idArchivero)+",")
        print("\"Nombre\": \""+str(self.NombreArchivero)+"\",")

        print("\"Cajones\": [", )

        for i in self.ListaCajones:

            i.ReadCajonAll()
           
            print("     ]")

            print("     },")

        print("     ]")

    ####################################################UPDATE##############################################################

    def UpdateArchivero(self): 
        print("Modificar Nombre Del Archivero")
        Nombrex = input("Nuevo Nombre: ") 
        self.NombreArchivero = Nombrex

        CambiraArchivero = True

        try: 
            Listax = input(f"Quieres Cambiar Atributos De los Cajones De Archivero Con El Nombre {self.NombreArchivero} [s/n]: ")

            if Listax == "y" or Listax == "yes" or Listax == "si" or Listax == "s":
                CambiraArchivero = True

            elif Listax == "n" or Listax == "no": 
                CambiraArchivero = False

        except: 
            Listax = "n"
            CambiraArchivero = False

        

        while CambiraArchivero != False:

            for i in self.ListaCajones:
                print("{")
                print(i.idCajon)
                print(i.SeccionCajon)
                for j in i.ListaCarpetas:
                    print(j)
                print("}")
            
            NombreCajonx = input("Dame El Nombre del Cajon Al Cual Queires Actualizar: ")

            try:
                PosicionCajaAActualizar = self.ListaCajones.index(NombreCajonx)
            except:
                print("No Se Encontro El Cajon Con El Nombre: ", NombreCajonx)

       

            try: 
                OpcionSalir = input("¿Quieres Salir? [s/n]")
            except: 
                Listax = "n"
                CambiraArchivero = False

        print("Los cambios se han hecho correctamente")




    ####################################################DELETE##############################################################

    def DeleteArchivero(id):
        pass


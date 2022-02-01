from Archivero import *
from Cajon import *
from Carpeta import *
from Documento import *
from Color import *
C = Color()

#AQUI COMIENZA LA MAGIA
Salir = False
while Salir != True:

    print(C.OK +"¿Que Quieres Hacer?")
    print("1)CRATE \n2)READ \n3)UPDATE \n4)DELETE \n5)SALIR")
    
    try: 
        Opcion = int(input(C.RESET+C.WARNING+"Respuesta: "+C.RESET+C.OK))
    except: 
        Opcion = 6

    ##################################################################################################################
    #################################################################################################################
    #################################################################################################################
    #   OPCION CREATE
    #################################################################################################################
    ##################################################################################################################
    #################################################################################################################
    if Opcion == 1: 
        CreateSalir = False
        print("")
        print(C.RESET+C.FAIL+"CREAT"+C.RESET+C.OK)

        while CreateSalir != True:
            print("")
            print("¿Que Quieres Dar De Alta?")
            print("1)ARCHIVERO \n2)CAJON \n3)CARPETA \n4)DOCUMETNO \n5)SALIR")

            try: 
                OpcionCreate = int(input(C.RESET+C.WARNING+"Respuesta: "+C.RESET+C.OK))
            except: 
                OpcionCreate = 6

            ##################################################################################################################
            #   DAR ALTA ARCHIVERO
            ##################################################################################################################
            if OpcionCreate == 1:
                print("")
                print(C.RESET+C.FAIL+"DAR DE ALTA UN ARCHIVERO"+C.RESET+C.OK)
                SalirClientes = False
                
                while SalirClientes != True:
                    
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Crear Un ARCHIVERO?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 

                        try: 
                            OCP = input(C.RESET+C.FAIL+"¿Quieres Añadirle CAJONES A Un ARCHIVERO?[s/n]: "+C.RESET+C.OK).lower()
                        except: 
                            OCP = "n"

                        if OCP == "n" or OCP == "no": 
                            print(C.RESET+C.FAIL+"No Quieres Crear Un ARCHIVERO. Saliste De Crear Archivero"+C.RESET+C.OK)
                            SalirClientes = True

                        elif OCP == "y" or OCP == "yes" or OCP == "si" or OCP == "s":
                            print("VAMOS A AÑADIR CAJONES A EL ARCHIVERO")
                            print("¿A Cual Archivero Quieres Agreagar Cajones?")
                            idA = int(input("Respuesta: "))
                            ObjetoArchivero = Archivero.ReadArchiverosById(idA)
                            if ObjetoArchivero > -1:
                                print("¿Que Cajones Quieres Agregar?")
                                ArrayCajones = input("Respuesta: ")
                                for i in ArrayCajones:
                                    ObjetoCajon = Cajon.ReadCajonById(int(i))
                                    if ObjetoCajon > -1:
                                        Archivero.ArchiverosLista[ObjetoArchivero].ListaCajones.append(Cajon.CajonesLista[ObjetoCajon])
                                        print(f"Se Agrego El Cajon Con Id: {i}")
                                    else: 
                                        print(f"No Se Agrego El Cajon Con Id: {i} Por Que No Exite")
                            else:
                                print(f"No Exite el Archivero con Id: {idA} {ObjetoArchivero}")    

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("CREAR UN ARCHIVERO NUEVO")                       
                        idA = int(input("id: "))
                        NombreA =input("Nombre: ")
                        NombreA = Archivero(idA, NombreA)
                        Archivero.ArchiverosLista.append(NombreA)
                        print(Archivero.ArchiverosLista[len(Archivero.ArchiverosLista)-1].ReadOnlyArchiveroById())
                        SalirClientes = False

            ##################################################################################################################
            #   DAR ALTA CAJON
            ##################################################################################################################
            elif OpcionCreate == 2: 
                print("")
                print(C.RESET+C.FAIL+"DAR DE ALTA UN CAJON"+C.RESET+C.OK)
                SalirClientes = False

                while SalirClientes != True:

                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Crear Un CAJON?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 

                        try: 
                            OCP = input(C.RESET+C.FAIL+"¿Quieres Añadirle CARPETAS A Un CAJON?[s/n]: "+C.RESET+C.OK).lower()
                        except: 
                            OCP = "n"

                        if OCP == "n" or OCP == "no": 
                            print(C.RESET+C.FAIL+"No Quieres Crear Un CAJON. Saliste De Crear CAJON"+C.RESET+C.OK)
                            SalirClientes = True

                        elif OCP == "y" or OCP == "yes" or OCP == "si" or OCP == "s":
                            print("VAMOS A AÑADIR CARPETAS A LOS CAJONES")
                            print("¿A Cual Cajon Quires Agreagar Carpetas?")
                            idA = int(input("Respuesta: "))
                            ObjetoCajon = Cajon.ReadCajonById(idA)
                            if ObjetoCajon > -1:
                                print("¿Que Carpetas Quieres Agregar?")
                                ArrayCarpetas = input("Respuesta: ")
                                for i in ArrayCarpetas:
                                    ObjetoCarpeta = Carpeta.ReadCarpetasById(int(i))
                                    if ObjetoCarpeta > -1:
                                        Cajon.CajonesLista[ObjetoCajon].ListaCarpetas.append(Carpeta.CarpetasLista[ObjetoCarpeta])
                                        print(f"Se Agrego La Carpeta Con Id: {i}")
                                    else: 
                                        print(f"No Se Agrego La Carpeta Con Id: {i} Por Que No Exite")
                            else:
                                print(f"No Exite el Cajon con Id: {idA}")    

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("CREAR UN CAJON NUEVO")                       
                        idA = int(input("id: "))
                        NombreA =input("Seccion: ")
                        NombreA = Cajon(idA, NombreA)
                        Cajon.CajonesLista.append(NombreA)
                        print(Cajon.CajonesLista[len(Cajon.CajonesLista)-1].ReadOnlyCajonById())
                        SalirClientes = False

            ##################################################################################################################
            #   DAR ALTA CARPETA
            ##################################################################################################################
            elif OpcionCreate == 3: 
                print("")
                print(C.RESET+C.FAIL+"DAR DE ALTA UNA CARPETA"+C.RESET+C.OK)
                SalirClientes = False

                while SalirClientes != True:
                    
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Crear Un CARPETA?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 

                        try: 
                            OCP = input(C.RESET+C.FAIL+"¿Quieres Añadirle DOCUMENTOS A Un CARPETA?[s/n]: "+C.RESET+C.OK).lower()
                        except: 
                            OCP = "n"

                        if OCP == "n" or OCP == "no": 
                            print(C.RESET+C.FAIL+"No Quieres Crear Un CARPETA. Saliste De Crear CARPETA"+C.RESET+C.OK)
                            SalirClientes = True

                        elif OCP == "y" or OCP == "yes" or OCP == "si" or OCP == "s":
                            print("VAMOS A AÑADIR DOCUMENTOS A CARPETAS")
                            print("¿A Cual Carpeta Quieres Agreagar Documentos?")
                            idA = int(input("Respuesta: "))
                            ObjetoCarpeta = Carpeta.ReadCarpetasById(idA)
                            if ObjetoCarpeta > -1:
                                print("¿Que Documentos Quieres Agregar?")
                                ArrayDocumentos = input("Respuesta: ")
                                for i in ArrayDocumentos:
                                    ObjetoDocumento = Documento.ReadDocumentosById(int(i))
                                    if ObjetoDocumento > -1:
                                        Carpeta.CarpetasLista[ObjetoCarpeta].ListaDocumento.append(Documento.DocumentosLista[ObjetoDocumento])
                                        print(f"Se Agrego El Cajon Con Id: {i}")
                                    else: 
                                        print(f"No Se Agrego El Cajon Con Id: {i} Por Que No Exite")
                            else:
                                print(f"No Exite el Archivero con Id: {idA}")    

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("CREAR UNA CARPETA NUEVA")                       
                        idA = int(input("id: "))
                        NombreA =input("Nombre: ")
                        NombreA = Carpeta(idA, NombreA)
                        Carpeta.CarpetasLista.append(NombreA)
                        print(Carpeta.CarpetasLista[len(Carpeta.CarpetasLista)-1].ReadOnlyCarpetaById())
                        SalirClientes = False

            ##################################################################################################################
            #   DAR ALTA DOCUMENTO
            ##################################################################################################################
            elif OpcionCreate == 4: 
                print("")
                print(C.RESET+C.FAIL+"DAR DE ALTA UN DOCUMENTO"+C.RESET+C.OK)
                SalirClientes = False

                while SalirClientes != True:

                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Crear Un DOCUMENTO?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 
                        print(C.RESET+C.FAIL+"No Quieres Crear Un DOCUMENTO. Saliste De Crear DOCUMENTO"+C.RESET+C.OK)
                        SalirClientes = True

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("CREAR UN ARCHIVERO NUEVO")                       
                        idA = int(input("id: "))
                        NombreA =input("Nombre: ")
                        Texto = input("Text: ")
                        NombreA = Documento(idA, NombreA, Texto)
                        Documento.DocumentosLista.append(NombreA)
                        print(Documento.DocumentosLista[len(Documento.DocumentosLista)-1].ReadOnlyDocumentoById())
                        SalirClientes = False

            ##################################################################################################################
            #   SALIR
            ##################################################################################################################
            elif OpcionCreate == 5:
                print("") 
                print(C.RESET+C.FAIL+"¿Seguro Que Queires SALIR del CREATE?", end=" ")

                try:
                    SeguroCreate = input("(s/n): "+C.RESET+C.OK).lower()
                except:
                    SeguroCreate = "no"

                if  SeguroCreate == "y" or SeguroCreate == "yes" or SeguroCreate == "si" or SeguroCreate == "s":
                    CreateSalir = True

                elif SeguroCreate == "n" or SeguroCreate == "no":
                    CreateSalir = False
            ##################################################################################################################
            #   DEFAULT
            ##################################################################################################################
            else: 
                CreateSalir = False

    #################################################################################################################
    #################################################################################################################
    ##################################################################################################################
    #   OPCION READ
    ##################################################################################################################
    #################################################################################################################
    #################################################################################################################
    elif Opcion == 2: 
        CreateSalir = False
        print("")
        print(C.RESET+C.FAIL+"READ"+C.RESET+C.OK)

        while CreateSalir != True:
            print("")
            print("¿Donde Quieres Usar El Metodo READ?")
            print("1)ARCHIVERO \n2)CAJON \n3)CARPETA \n4)DOCUMETNO \n5)SALIR")

            try: 
                OpcionCreate = int(input(C.RESET+C.WARNING+"Respuesta: "+C.RESET+C.OK))
            except: 
                OpcionCreate = 6

            ##################################################################################################################
            #   DAR MOSTRAR ARCHIVERO
            ##################################################################################################################
            if OpcionCreate == 1:
                print("")
                print(C.RESET+C.FAIL+"Mostrar Informacion De Archivero "+C.RESET+C.OK)
                SalirClientes = False

                while SalirClientes != True:

                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quiere Mostrar Solo Informacion Del Archivero?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 

                        try: 
                            OCP = input(C.RESET+C.FAIL+"¿Quires Mostrar Toda la Infromacion Del Archivero?[s/n]: "+C.RESET+C.OK).lower()
                        except: 
                            OCP = "n"

                        if OCP == "n" or OCP == "no": 
                            print(C.RESET+C.FAIL+"No Quieres Crear Un ARCHIVERO. Saliste De Crear Archivero"+C.RESET+C.OK)
                            SalirClientes = True

                        elif OCP == "y" or OCP == "yes" or OCP == "si" or OCP == "s":
                            print("¿De Que Archivero Quires Mostrar Su Informacion?")
                            ObjetoArchivero = int(input("Respuesta: "))
                            ObjetoArchivero = Archivero.ReadArchiverosById(ObjetoArchivero)
                            if ObjetoArchivero > -1:
                                Archivero.ArchiverosLista[ObjetoArchivero].ReadArciveroAll()
                            else:
                                print(f"El Archivero Con id: {ObjetoArchivero} No Se Encontro")
                            SalirClientes = False

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("¿De Que Archivero Quires Mostrar Su Informacion?")
                        ObjetoArchivero = int(input("Respuesta: "))
                        ObjetoArchivero = Archivero.ReadArchiverosById(ObjetoArchivero)
                        if ObjetoArchivero > -1:
                            Archivero.ArchiverosLista[ObjetoArchivero].ReadOnlyArchiveroById()
                        else:
                            print(f"El Archivero Con id: {ObjetoArchivero} No Se Encontro")
                        SalirClientes = False

            ##################################################################################################################
            #   DAR MOSTRAR CAJON
            ##################################################################################################################
            elif OpcionCreate == 2: 
                print("")
                print(C.RESET+C.FAIL+"Mostrar Informacion De Cajon "+C.RESET+C.OK)
                SalirClientes = False

                while SalirClientes != True:

                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quiere Mostrar Solo Informacion Del Cajon?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 

                        try: 
                            OCP = input(C.RESET+C.FAIL+"¿Quires Mostrar Toda la Infromacion Del Cajon?[s/n]: "+C.RESET+C.OK).lower()
                        except: 
                            OCP = "n"

                        if OCP == "n" or OCP == "no": 
                            print(C.RESET+C.FAIL+"No Quieres Crear Un ARCHIVERO. Saliste De Crear Archivero"+C.RESET+C.OK)
                            SalirClientes = True

                        elif OCP == "y" or OCP == "yes" or OCP == "si" or OCP == "s":
                            print("¿De Que Archivero Quires Mostrar Su Informacion?")
                            ObjetoCajon = int(input("Respuesta: "))
                            ObjetoCajon = Cajon.ReadCajonById(ObjetoCajon)
                            if ObjetoCajon > -1:
                                Cajon.CajonesLista[ObjetoCajon].ReadCajonAll()
                            else:
                                print(f"El Cajon Con id: {ObjetoCajon} No Se Encontro")
                            SalirClientes = False

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("¿De Que Archivero Quires Mostrar Su Informacion?")
                        ObjetoCajon = int(input("Respuesta: "))
                        ObjetoCajon = Cajon.ReadCajonById(ObjetoCajon)
                        if ObjetoCajon > -1:
                            Cajon.CajonesLista[ObjetoCajon].ReadOnlyCajonById()
                        else:
                            print(f"El Cajon Con id: {ObjetoCajon} No Se Encontro")
                        SalirClientes = False

            ##################################################################################################################
            #   DAR MOSTRAR CARPETA
            ##################################################################################################################
            elif OpcionCreate == 3: 
                print("")
                print(C.RESET+C.FAIL+"Mostrar Informacion De Carpeta "+C.RESET+C.OK)
                SalirClientes = False

                while SalirClientes != True:

                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quiere Mostrar Solo Informacion De La Carpeta?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 

                        try: 
                            OCP = input(C.RESET+C.FAIL+"¿Quires Mostrar Toda la Infromacion De La Carpeta?[s/n]: "+C.RESET+C.OK).lower()
                        except: 
                            OCP = "n"

                        if OCP == "n" or OCP == "no": 
                            print(C.RESET+C.FAIL+"No Quieres Ver Toda La Informacion De La Capreta"+C.RESET+C.OK)
                            SalirClientes = True

                        elif OCP == "y" or OCP == "yes" or OCP == "si" or OCP == "s":
                            print("¿De Que Carpeta Quires Mostrar Su Informacion?")
                            ObjetoCarpeta = int(input("Respuesta: "))
                            ObjetoCarpeta = Carpeta.ReadCarpetasById(ObjetoCarpeta)
                            if ObjetoCarpeta > -1:
                                Archivero.ArchiverosLista[ObjetoCarpeta].ReadCarpetaAll()
                            else:
                                print(f"El Archivero Con id: {ObjetoCarpeta} No Se Encontro")
                            SalirClientes = False

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("¿De Que Carpeta Quires Mostrar Su Informacion?")
                        ObjetoCarpeta = int(input("Respuesta: "))
                        ObjetoCarpeta = Carpeta.ReadCarpetasById(ObjetoCarpeta)
                        if ObjetoCarpeta > -1:
                            Archivero.ArchiverosLista[ObjetoCarpeta].ReadOnlyCarpetaById()
                        else:
                            print(f"El Archivero Con id: {ObjetoCarpeta} No Se Encontro")
                        SalirClientes = False


            ##################################################################################################################
            #   DAR MOSTRAR DOCUMENTO
            ##################################################################################################################
            elif OpcionCreate == 4: 
                print("")
                print(C.RESET+C.FAIL+"Mostrar Informacion De Archivero "+C.RESET+C.OK)
                SalirClientes = False

                while SalirClientes != True:

                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quiere Mostrar Solo Informacion Del Archivero?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 
                        print("No Quiers Mostarar Informacion Sobre Documento. Saliste.")
                        SalirClientes = True

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("¿De Que Archivero Quires Mostrar Su Informacion?")
                        ObjetoDocumenot = int(input("Respuesta: "))
                        ObjetoDocumenot = Documento.ReadDocumentosById(ObjetoDocumenot)
                        if ObjetoDocumenot > -1:
                            Documento.ReadDocumentosById[ObjetoDocumenot].ReadOnlyDocumentoById()
                        else:
                            print(f"El Archivero Con id: {ObjetoDocumenot} No Se Encontro")
                        SalirClientes = False

            ##################################################################################################################
            #   SALIR
            ##################################################################################################################
            elif OpcionCreate == 5:
                print("") 
                print(C.RESET+C.FAIL+"¿Seguro Que Queires SALIR del READ?", end=" ")

                try:
                    SeguroCreate = input("(s/n): "+C.RESET+C.OK).lower()
                except:
                    SeguroCreate = "no"

                if  SeguroCreate == "y" or SeguroCreate == "yes" or SeguroCreate == "si" or SeguroCreate == "s":
                    CreateSalir = True

                elif SeguroCreate == "n" or SeguroCreate == "no":
                    CreateSalir = False
            ##################################################################################################################
            #   DEFAULT
            ##################################################################################################################
            else: 
                CreateSalir = False

    ##################################################################################################################
    #################################################################################################################
    ##################################################################################################################
    #   OPCION UPDATE
    ##################################################################################################################
    ##################################################################################################################
    #################################################################################################################
    elif Opcion == 3: 
        CreateSalir = False
        print("")
        print(C.RESET+C.FAIL+"CREAT"+C.RESET+C.OK)

        while CreateSalir != True:
            print("") 
            print("¿Que Quieres ACTUALIZAR?")
            print("1)ARCHIVERO \n2)CAJON \n3)CARPETA \n4)DOCUMETNO \n5)SALIR")

            try: 
                OpcionCreate = int(input(C.RESET+C.WARNING+"Respuesta: "+C.RESET+C.OK))
            except: 
                OpcionCreate = 6

            ##################################################################################################################
            #   DAR ACTUALIZAR ARCHIVERO
            ##################################################################################################################
            if OpcionCreate == 1:
                print("")
                print(C.RESET+C.FAIL+"ACTUALIZAR UN ARCHIVERO"+C.RESET+C.OK)
                SalirClientes = False
                
                while SalirClientes != True:
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Actualizar Un ARCHIVERO?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 
                        SalirClientes = True
                        print("No Quieres Acualizar Un ARCHIVERO")

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("¿Que Archivero Quieres Actualizar?")
                        ida = int(input("Buscar Id: "))
                        ObjetoArchivero = Archivero.ReadArchiverosById(idA)
                        if ObjetoArchivero > -1:
                            newNombre = input("Agregar Nuevo Nombre: ")
                            Archivero.ArchiverosLista[ObjetoArchivero].NombreArchivero = newNombre
                            Archivero.ArchiverosLista[ObjetoArchivero].ReadOnlyArchiveroById() 
                        else:
                            print(f"No Exite el Archivero con Id: {idA}")  
                        SalirClientes = False

            ##################################################################################################################
            #   DAR ACTUALIZAR CAJON
            ##################################################################################################################
            elif OpcionCreate == 2: 
                print("")
                print(C.RESET+C.FAIL+"ACTUALIZAR UN CAJON"+C.RESET+C.OK)
                SalirClientes = False
                
                while SalirClientes != True:
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Actualizar Un CAJON?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 
                        SalirClientes = True
                        print("No Quieres Acualizar Un CAJON")

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("¿Que Cajon Quieres Actualizar?")
                        ida = int(input("Buscar Id: "))
                        ObjetoCajon = Cajon.CajonesLista(idA)
                        if ObjetoCajon > -1:
                            newNombre = input("Agregar Nueva Seccion: ")
                            Cajon.CajonesLista[ObjetoCajon].SeccionCajon = newNombre
                            Cajon.CajonesLista[ObjetoCajon].ReadOnlyArchiveroById() 
                        else:
                            print(f"No Exite el Cajon con Id: {idA}")  
                        SalirClientes = False

            ##################################################################################################################
            #   DAR ACTUALIZAR CARPETA
            ##################################################################################################################
            elif OpcionCreate == 3: 
                print("")
                print(C.RESET+C.FAIL+"ACTUALIZAR UN CARPETA"+C.RESET+C.OK)
                SalirClientes = False
                
                while SalirClientes != True:
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Actualizar Un CARPETA?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 
                        SalirClientes = True
                        print("No Quieres Acualizar Un CARPETA")

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("¿Que Archivero Quieres Actualizar?")
                        ida = int(input("Buscar Id: "))
                        ObjetoCarpeta = Carpeta.ReadCarpetasById(idA)
                        if ObjetoCarpeta > -1:
                            newNombre = input("Agregar Nuevo Nombre: ")
                            Carpeta.CarpetasLista[ObjetoCarpeta].NombreCarpeta = newNombre
                            Carpeta.CarpetasLista[ObjetoCarpeta].ReadOnlyCarpetaById() 
                        else:
                            print(f"No Exite La Carpeta con Id: {idA}")  
                        SalirClientes = False

            ##################################################################################################################
            #   DAR ACTUALIZAR DOCUMENTO
            ##################################################################################################################
            elif OpcionCreate == 4: 
                print("")
                print(C.RESET+C.FAIL+"ACTUALIZAR UN DOCUMENTO"+C.RESET+C.OK)
                SalirClientes = False
                
                while SalirClientes != True:
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Actualizar Un DOCUMENTO?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 
                        SalirClientes = True
                        print("No Quieres Acualizar Un DOCUMENTO")

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("¿Que Archivero Quieres Actualizar?")
                        ida = int(input("Buscar Id: "))
                        ObjetoDocumento = Documento.ReadDocumentosById(idA)
                        if ObjetoDocumento > -1:
                            newNombre = input("Agregar Nuevo Nombre: ")
                            newTexto = input("Agregar Nuevo Texto: ")
                            Documento.DocumentosLista[ObjetoDocumento].UpdateDocumento(newNombre, newTexto)
                            Documento.DocumentosLista[ObjetoDocumento].ReadOnlyArchiveroById() 
                        else:
                            print(f"No Exite el Archivero con Id: {idA}")  
                        SalirClientes = False

            ##################################################################################################################
            #   SALIR
            ##################################################################################################################
            elif OpcionCreate == 5:
                print("") 
                print(C.RESET+C.FAIL+"¿Seguro Que Queires SALIR del CREATE?", end=" ")

                try:
                    SeguroCreate = input("(s/n): "+C.RESET+C.OK).lower()
                except:
                    SeguroCreate = "no"

                if  SeguroCreate == "y" or SeguroCreate == "yes" or SeguroCreate == "si" or SeguroCreate == "s":
                    CreateSalir = True

                elif SeguroCreate == "n" or SeguroCreate == "no":
                    CreateSalir = False
            ##################################################################################################################
            #   DEFAULT
            ##################################################################################################################
            else: 
                CreateSalir = False

    ##################################################################################################################
    #################################################################################################################
    ##################################################################################################################
    #   OPCION DELETE
    ##################################################################################################################
    ##################################################################################################################
    #################################################################################################################

    elif Opcion == 4: 
        CreateSalir = False
        print("")
        print(C.RESET+C.FAIL+"DELETE"+C.RESET+C.OK)

        while CreateSalir != True:
            print("")
            print("¿Que Quieres Eliminar?")
            print("1)ARCHIVERO \n2)CAJON \n3)CARPETA \n4)DOCUMETNO \n5)SALIR")

            try: 
                OpcionCreate = int(input(C.RESET+C.WARNING+"Respuesta: "+C.RESET+C.OK))
            except: 
                OpcionCreate = 6

            ##################################################################################################################
            #   DAR DELETE ARCHIVERO
            ##################################################################################################################
            if OpcionCreate == 1:
                print("")
                print(C.RESET+C.FAIL+"Eliminar Un ARCHIVERO"+C.RESET+C.OK)
                SalirClientes = False
        
                while SalirClientes != True:
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Eliminar Un ARCHIVERO?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 
                        print("No Quieres Eliminar Un Archivo")
                        SalirClientes = True

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("¿Que Archivero Quieres Eliminar?")
                        ida = int(input("Buscar Id: "))
                        ObjetoArchivero = Archivero.ReadArchiverosById(idA)
                        if ObjetoArchivero > -1:
                            Archivero.ArchiverosLista[ObjetoArchivero].ReadOnlyArchiveroById()
                            Archivero.ArchiverosLista.pop(ObjetoArchivero)
                        else:
                            print(f"No Exite el Archivero con Id: {idA}")  
                        SalirClientes = False

            ##################################################################################################################
            #   DAR ALTA CAJON
            ##################################################################################################################
            elif OpcionCreate == 2: 
                print("")
                print(C.RESET+C.FAIL+"Eliminar Un CAJON"+C.RESET+C.OK)
                SalirClientes = False
        
                while SalirClientes != True:
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Eliminar Un CAJON?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 
                        print("No Quieres Eliminar Un Archivo")
                        SalirClientes = True

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("¿Que Cajon Quieres Eliminar?")
                        ida = int(input("Buscar Id: "))
                        ObjetoCajon = Cajon.ReadCajonById(idA)
                        if ObjetoCajon > -1:
                            Cajon.CajonesLista[ObjetoCajon].ReadOnlyArchiveroById()
                            Cajon.CajonesLista.pop(ObjetoCajon)
                        else:
                            print(f"No Exite el Archivero con Id: {idA}")  
                        SalirClientes = False


            ##################################################################################################################
            #   DAR ALTA CARPETA
            ##################################################################################################################
            elif OpcionCreate == 3: 
                print("")
                print(C.RESET+C.FAIL+"Eliminar Un CARPETA"+C.RESET+C.OK)
                SalirClientes = False
        
                while SalirClientes != True:
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Eliminar Un CARPETA?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 
                        print("No Quieres Eliminar Un CARPETA")
                        SalirClientes = True

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("¿Que Archivero Quieres Eliminar?")
                        ida = int(input("Buscar Id: "))
                        ObjetoCarpeta = Carpeta.ReadCarpetasById(idA)
                        if ObjetoCarpeta > -1:
                            Carpeta.CarpetasLista[ObjetoCarpeta].ReadOnlyArchiveroById()
                            Carpeta.CarpetasListaCarpeta.CarpetasLista.pop(ObjetoCarpeta)
                        else:
                            print(f"No Exite el Archivero con Id: {idA}")  
                        SalirClientes = False


            ##################################################################################################################
            #   DAR ALTA DOCUMENTO
            ##################################################################################################################
            elif OpcionCreate == 4: 
                print("")
                print(C.RESET+C.FAIL+"Eliminar Un DOCUMENTO"+C.RESET+C.OK)
                SalirClientes = False
        
                while SalirClientes != True:
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Eliminar Un DOCUMENTO?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    if OC == "n" or OC == "no": 
                        print("No Quieres Eliminar Un DOCUMENTO")
                        SalirClientes = True

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("¿Que Archivero Quieres Eliminar?")
                        ida = int(input("Buscar Id: "))
                        Documento.DeleteDocumento(ida)
                        SalirClientes = False


            ##################################################################################################################
            #   SALIR
            ##################################################################################################################
            elif OpcionCreate == 5:
                print("") 
                print(C.RESET+C.FAIL+"¿Seguro Que Queires SALIR del CREATE?", end=" ")

                try:
                    SeguroCreate = input("(s/n): "+C.RESET+C.OK).lower()
                except:
                    SeguroCreate = "no"

                if  SeguroCreate == "y" or SeguroCreate == "yes" or SeguroCreate == "si" or SeguroCreate == "s":
                    CreateSalir = True

                elif SeguroCreate == "n" or SeguroCreate == "no":
                    CreateSalir = False
            ##################################################################################################################
            #   DEFAULT
            ##################################################################################################################
            else: 
                CreateSalir = False
    
    ##################################################################################################################
    #################################################################################################################
    ##################################################################################################################
    #   OPCION SALIR
    ##################################################################################################################
    ##################################################################################################################
    #################################################################################################################
    elif Opcion == 5: 
        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del Programa?", end=" ")

        try:
            SeguroCreate = input("(s/n): "+C.RESET+C.OK).lower()
        except:
            SeguroCreate = "no"

        if  SeguroCreate == "y" or SeguroCreate == "yes" or SeguroCreate == "si" or SeguroCreate == "s":
            print("Salista Del Programa")
            Salir = True

        elif SeguroCreate == "n" or SeguroCreate == "no":
            Salir = False
    
    ##################################################################################################################
    #################################################################################################################
    ##################################################################################################################
    #   OPCION DEFAULT
    ##################################################################################################################
    ##################################################################################################################
    #################################################################################################################
    else:
        Salir == False
# #

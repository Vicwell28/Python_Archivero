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
                #PREGUNAT SI QUIERE CREAR UN  NUEVO OBJETO O AGREGARLE PROPIEDADES A UN OBJETO
                while SalirClientes != True:
                    #AQUI VAMOS A EMPEZAR A CREARE LOS CLIENTES PREGUNTANDO EN CADA INSTANCIACION SI QUIERE VOLVER A CREARE OTRO O SALIR
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Crear Un ARCHIVERO?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    #AQUI ES DONDE NOS VAMOS A TRAER LOS METODO PARA CREAR LOS ARCHVIERO Y COLOCARLOS EN LA ARCHIVEROLISTA STATIC
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

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("Creacion De ARCHIVERO Nuevo")
                        SalirClientes = False

            ##################################################################################################################
            #   DAR ALTA CAJON
            ##################################################################################################################
            elif OpcionCreate == 2: 
                print("")
                print(C.RESET+C.FAIL+"DAR DE ALTA UN CAJON"+C.RESET+C.OK)
                SalirClientes = False
                #PREGUNAT SI QUIERE CREAR UN  NUEVO OBJETO O AGREGARLE PROPIEDADES A UN OBJETO
                while SalirClientes != True:
                    #AQUI VAMOS A EMPEZAR A CREARE LOS CLIENTES PREGUNTANDO EN CADA INSTANCIACION SI QUIERE VOLVER A CREARE OTRO O SALIR
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Crear Un CAJON?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    #AQUI ES DONDE NOS VAMOS A TRAER LOS METODO PARA CREAR LOS ARCHVIERO Y COLOCARLOS EN LA ARCHIVEROLISTA STATIC
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

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("Creacion De CAJON Nuevo")
                        SalirClientes = False


            ##################################################################################################################
            #   DAR ALTA CARPETA
            ##################################################################################################################
            elif OpcionCreate == 3: 
                print("")
                print(C.RESET+C.FAIL+"DAR DE ALTA UNA CARPETA"+C.RESET+C.OK)
                SalirClientes = False
                #PREGUNAT SI QUIERE CREAR UN  NUEVO OBJETO O AGREGARLE PROPIEDADES A UN OBJETO
                while SalirClientes != True:
                    #AQUI VAMOS A EMPEZAR A CREARE LOS CLIENTES PREGUNTANDO EN CADA INSTANCIACION SI QUIERE VOLVER A CREARE OTRO O SALIR
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Crear Un CARPETA?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    #AQUI ES DONDE NOS VAMOS A TRAER LOS METODO PARA CREAR LOS ARCHVIERO Y COLOCARLOS EN LA ARCHIVEROLISTA STATIC
                    if OC == "n" or OC == "no": 

                        try: 
                            OCP = input(C.RESET+C.FAIL+"¿Quieres Añadirle DOCUMENTOS A Un CARPETA?[s/n]: "+C.RESET+C.OK).lower()
                        except: 
                            OCP = "n"

                        if OCP == "n" or OCP == "no": 
                            print(C.RESET+C.FAIL+"No Quieres Crear Un CARPETA. Saliste De Crear CARPETA"+C.RESET+C.OK)
                            SalirClientes = True

                        elif OCP == "y" or OCP == "yes" or OCP == "si" or OCP == "s":
                            print("VAMOS A AÑADIR DOCUMENTOS A EL CARPETA")

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("Creacion De CARPETA Nuevo")
                        SalirClientes = False


            ##################################################################################################################
            #   DAR ALTA DOCUMENTO
            ##################################################################################################################
            elif OpcionCreate == 4: 
                print("")
                print(C.RESET+C.FAIL+"DAR DE ALTA UN DOCUMENTO"+C.RESET+C.OK)
                SalirClientes = False
                #PREGUNAT SI QUIERE CREAR UN  NUEVO OBJETO O AGREGARLE PROPIEDADES A UN OBJETO
                while SalirClientes != True:
                    #AQUI VAMOS A EMPEZAR A CREARE LOS CLIENTES PREGUNTANDO EN CADA INSTANCIACION SI QUIERE VOLVER A CREARE OTRO O SALIR
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quieres Crear Un DOCUMENTO?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    #AQUI ES DONDE NOS VAMOS A TRAER LOS METODO PARA CREAR LOS ARCHVIERO Y COLOCARLOS EN LA ARCHIVEROLISTA STATIC
                    if OC == "n" or OC == "no": 
                        print(C.RESET+C.FAIL+"No Quieres Crear Un DOCUMENTO. Saliste De Crear DOCUMENTO"+C.RESET+C.OK)
                        SalirClientes = True

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("Creacion De ARCHIVERO Nuevo")
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
                #PREGUNAT SI QUIERE CREAR UN  NUEVO OBJETO O AGREGARLE PROPIEDADES A UN OBJETO
                while SalirClientes != True:
                    #AQUI VAMOS A EMPEZAR A CREARE LOS CLIENTES PREGUNTANDO EN CADA INSTANCIACION SI QUIERE VOLVER A CREARE OTRO O SALIR
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quiere Mostrar Solo Informacion Del Archivero?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    #AQUI ES DONDE NOS VAMOS A TRAER LOS METODO PARA CREAR LOS ARCHVIERO Y COLOCARLOS EN LA ARCHIVEROLISTA STATIC
                    if OC == "n" or OC == "no": 

                        try: 
                            OCP = input(C.RESET+C.FAIL+"¿Quires Mostrar Toda la Infromacion Del Archivero?[s/n]: "+C.RESET+C.OK).lower()
                        except: 
                            OCP = "n"

                        if OCP == "n" or OCP == "no": 
                            print(C.RESET+C.FAIL+"No Quieres Crear Un ARCHIVERO. Saliste De Crear Archivero"+C.RESET+C.OK)
                            SalirClientes = True

                        elif OCP == "y" or OCP == "yes" or OCP == "si" or OCP == "s":
                            print("ESTAREMOS MOSTRANDO TODA LA INFROAMCION DEL ARCHIVERO")

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("ESTAREMOS MOSTRARNDO SOLO INFORMACION DEL ARCHIVERO")
                        SalirClientes = False

            ##################################################################################################################
            #   DAR MOSTRAR CAJON
            ##################################################################################################################
            elif OpcionCreate == 2: 
                print("")
                print(C.RESET+C.FAIL+"Mostrar Informacion De Archivero "+C.RESET+C.OK)
                SalirClientes = False
                #PREGUNAT SI QUIERE CREAR UN  NUEVO OBJETO O AGREGARLE PROPIEDADES A UN OBJETO
                while SalirClientes != True:
                    #AQUI VAMOS A EMPEZAR A CREARE LOS CLIENTES PREGUNTANDO EN CADA INSTANCIACION SI QUIERE VOLVER A CREARE OTRO O SALIR
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quiere Mostrar Solo Informacion Del Archivero?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    #AQUI ES DONDE NOS VAMOS A TRAER LOS METODO PARA CREAR LOS ARCHVIERO Y COLOCARLOS EN LA ARCHIVEROLISTA STATIC
                    if OC == "n" or OC == "no": 

                        try: 
                            OCP = input(C.RESET+C.FAIL+"¿Quires Mostrar Toda la Infromacion Del Archivero?[s/n]: "+C.RESET+C.OK).lower()
                        except: 
                            OCP = "n"

                        if OCP == "n" or OCP == "no": 
                            print(C.RESET+C.FAIL+"No Quieres Crear Un ARCHIVERO. Saliste De Crear Archivero"+C.RESET+C.OK)
                            SalirClientes = True

                        elif OCP == "y" or OCP == "yes" or OCP == "si" or OCP == "s":
                            print("ESTAREMOS MOSTRANDO TODA LA INFROAMCION DEL ARCHIVERO")

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("ESTAREMOS MOSTRARNDO SOLO INFORMACION DEL ARCHIVERO")
                        SalirClientes = False


            ##################################################################################################################
            #   DAR MOSTRAR CARPETA
            ##################################################################################################################
            elif OpcionCreate == 3: 
                print("")
                print(C.RESET+C.FAIL+"Mostrar Informacion De Archivero "+C.RESET+C.OK)
                SalirClientes = False
                #PREGUNAT SI QUIERE CREAR UN  NUEVO OBJETO O AGREGARLE PROPIEDADES A UN OBJETO
                while SalirClientes != True:
                    #AQUI VAMOS A EMPEZAR A CREARE LOS CLIENTES PREGUNTANDO EN CADA INSTANCIACION SI QUIERE VOLVER A CREARE OTRO O SALIR
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quiere Mostrar Solo Informacion Del Archivero?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    #AQUI ES DONDE NOS VAMOS A TRAER LOS METODO PARA CREAR LOS ARCHVIERO Y COLOCARLOS EN LA ARCHIVEROLISTA STATIC
                    if OC == "n" or OC == "no": 

                        try: 
                            OCP = input(C.RESET+C.FAIL+"¿Quires Mostrar Toda la Infromacion Del Archivero?[s/n]: "+C.RESET+C.OK).lower()
                        except: 
                            OCP = "n"

                        if OCP == "n" or OCP == "no": 
                            print(C.RESET+C.FAIL+"No Quieres Crear Un ARCHIVERO. Saliste De Crear Archivero"+C.RESET+C.OK)
                            SalirClientes = True

                        elif OCP == "y" or OCP == "yes" or OCP == "si" or OCP == "s":
                            print("ESTAREMOS MOSTRANDO TODA LA INFROAMCION DEL ARCHIVERO")

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("ESTAREMOS MOSTRARNDO SOLO INFORMACION DEL ARCHIVERO")
                        SalirClientes = False


            ##################################################################################################################
            #   DAR MOSTRAR DOCUMENTO
            ##################################################################################################################
            elif OpcionCreate == 4: 
                print("")
                print(C.RESET+C.FAIL+"Mostrar Informacion De Archivero "+C.RESET+C.OK)
                SalirClientes = False
                #PREGUNAT SI QUIERE CREAR UN  NUEVO OBJETO O AGREGARLE PROPIEDADES A UN OBJETO
                while SalirClientes != True:
                    #AQUI VAMOS A EMPEZAR A CREARE LOS CLIENTES PREGUNTANDO EN CADA INSTANCIACION SI QUIERE VOLVER A CREARE OTRO O SALIR
                    try: 
                        OC = input(C.RESET+C.FAIL+"¿Quiere Mostrar Solo Informacion Del Archivero?[s/n]: "+C.RESET+C.OK).lower()
                    except: 
                        OC = "n"
                    
                    #AQUI ES DONDE NOS VAMOS A TRAER LOS METODO PARA CREAR LOS ARCHVIERO Y COLOCARLOS EN LA ARCHIVEROLISTA STATIC
                    if OC == "n" or OC == "no": 

                        try: 
                            OCP = input(C.RESET+C.FAIL+"¿Quires Mostrar Toda la Infromacion Del Archivero?[s/n]: "+C.RESET+C.OK).lower()
                        except: 
                            OCP = "n"

                        if OCP == "n" or OCP == "no": 
                            print(C.RESET+C.FAIL+"No Quieres Crear Un ARCHIVERO. Saliste De Crear Archivero"+C.RESET+C.OK)
                            SalirClientes = True

                        elif OCP == "y" or OCP == "yes" or OCP == "si" or OCP == "s":
                            print("ESTAREMOS MOSTRANDO TODA LA INFROAMCION DEL ARCHIVERO")

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("ESTAREMOS MOSTRARNDO SOLO INFORMACION DEL ARCHIVERO")
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
                        print("Actualizar Un Archivero, Mediante ID")
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
                        print("Actualizar Un CAJON, Mediante ID")
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
                        print("Actualizar Un CARPETA, Mediante ID")
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
                        print("Actualizar Un Archivero, Mediante ID")
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
        print(C.RESET+C.FAIL+"CREAT"+C.RESET+C.OK)

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
                        print("Creacion De ARCHIVERO Nuevo")
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
                        print("Creacion De CAJON Nuevo")
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
                        print("Creacion De CARPETA Nuevo")
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
                        print("Creacion De DOCUMENTO Nuevo")
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






# ArchiveroUno = Archivero(1, "Universidad Tecnologica de Torreon")
# # print(type(ArchiveroUno))

# Cajon1 = Cajon(1, "A")
# Cajon2 = Cajon(2, "B")
# # print(type(Cajon1))
# # print(type(Cajon2))

# # Cajon3 = Cajon(3, "C")

# Carpeta1 = Carpeta(1, "Carpeta Uno")
# Carpeta2 = Carpeta(2, "Carpeta Dos")
# Carpeta3 = Carpeta(3, "Carpeta Tres")
# # print(type(Carpeta1))
# # print(type(Carpeta2))
# # print(type(Carpeta3))

# # Carpeta4 = Carpeta(4, "Carpeta Cuatro")
# # Carpeta5 = Carpeta(5, "Carpeta Cinco")
# # Carpeta6 = Carpeta(6, "Carpeta Seis")

# Archivo1 = Documento(1, "Documento Uno", "Texto" )
# Archivo2 = Documento(2, "Documento Uno", "Texto" )
# Archivo3 = Documento(3, "Documento Uno", "Texto" )
# Archivo4 = Documento(4, "Documento Uno", "Texto" )
# # print(type(Archivo1))
# # print(type(Archivo2))
# # print(type(Archivo3))
# Archivo1.DeleteDocumento()
# # print(type(Archivo4))
# # Archivo5 = Documento(5, "Documento Uno", "Texto" )
# # Archivo6 = Documento(6, "Documento Uno", "Texto" )
# # Archivo7 = Documento(7, "Documento Uno", "Texto" )
# # Archivo8 = Documento(8, "Documento Uno", "Texto" )
# # Archivo9 = Documento(9, "Documento Uno", "Texto" )
# # Archivo10 = Documento(10, "Documento Uno", "Texto" )
# # Archivo11 = Documento(11, "Documento Uno", "Texto" )
# # Archivo12 = Documento(12, "Documento Uno", "Texto" )

# ArchiveroUno.CreateAddCajones(Cajon1, Cajon2)
# # print("Cajones De Archivero: ",ArchiveroUno.ListaCajones[:])

# Cajon1.CreteAddCarpetas(Carpeta1)
# Cajon2.CreteAddCarpetas(Carpeta2, Carpeta3)
# # print("Carpetas Del Cajon Uno",Cajon1.ListaCarpetas[:])
# # print("Carpetas Del Cajon Dos",Cajon2.ListaCarpetas[:])
# # Cajon3.CreteAddCarpetas(Carpeta4, Carpeta5, Carpeta6)

# Carpeta1.CreteAddDocumentos(Archivo1)
# Carpeta2.CreteAddDocumentos(Archivo2, Archivo4)
# # print("Documentos De La Carpeta Uno",Carpeta1.ListaDocumento[:])
# # print("Documentos De La Carpeta Uno",Carpeta2.ListaDocumento[:])
# # Carpeta3.CreteAddDocumentos(Archivo2, Archivo4)
# # Carpeta4.CreteAddDocumentos(Archivo5, Archivo6)
# # Carpeta5.CreteAddDocumentos(Archivo7, Archivo8, Archivo9)
# # Carpeta6.CreteAddDocumentos(Archivo10, Archivo11, Archivo12)
# ArchiveroUno.ReadArciveroAll()
# print(ArchiveroUno.ReadCajonById(2))
# ArchiveroUno.DeleteArchivero()
# # ArchiveroUno.ReadArciveroAll()
# # ArchiveroUno.UpdateArchivero()
# # ArchiveroUno.UpdateArchivero()

# # ArchiveroUno.DeleteArchivero()

# print(ArchiveroUno)
# Archivero.ArchiverosLista.append(ArchiveroUno)
# print(Archivero.ArchiverosLista[:])
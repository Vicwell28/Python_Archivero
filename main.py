from Archivero import *
from Cajon import *
from Carpeta import *
from Documento import *
from Color import *
import os
C = Color()
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

SalirMenuCrud = False
while SalirMenuCrud != True:
    print(C.OK+"1)CRATE \n2)READ \n3)UPDATE \n4)DELETE \n5)SALIR")

    try:
        RespuestaMenuCrud = int(input("Respuesta: "))        
    except:
        RespuestaMenuCrud = 0
    #####################################################################################################################################################################################################################################CREAD#############################################################################################################################################################################################################################################
    if RespuestaMenuCrud  == 1:
        clearConsole()
        print("CREATE")
        
        SalirMetodoCreate = False
        while SalirMetodoCreate != True:
            print(C.RESET+C.WARNING+"1)ARCHIVERO \n2)CAJON \n3)CARPETA \n4)DOCUMENTO \n5)SALIR")
            try:
                RespuestaMetodoCreate = int(input("Respuesta: "))        
            except:
                RespuestaMetodoCreate = 0
            #################################################### CREATE ARCHIVERO ####################################################
            if RespuestaMetodoCreate == 1: 
                clearConsole()
                print("METODO CREATE: Archivero")

                OpcionCreateArticulo = False
                while OpcionCreateArticulo != True:
                    print(C.RESET+C.OK+"1)Crear Nuevo Archivero \n2)Agregar Cajones A Archivero \n3)SALIR")
                    try:
                        RespuestaOpcionCreateArticulo = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionCreateArticulo = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionCreateArticulo == 1: 
                        clearConsole()
                        idArchivero = int(input("id:"))
                        Nombre = input("Nombre Archivero: ")
                        Archivero.CreateArchivero(idArchivero, Nombre)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateArticulo == 2:
                        clearConsole()
                        print("¿A Que Archivero Quieres Agregar Cajones?")
                        idArchivero = int(input("id: "))
                        Archivero.CrateAddCajones(idArchivero)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateArticulo == 3:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del CREATE : ARTICULO?", end=" ")
                        try:
                            SeguroSalirArtiucloOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirArtiucloOpcion = "no"

                        if  SeguroSalirArtiucloOpcion == "y" or SeguroSalirArtiucloOpcion == "yes" or SeguroSalirArtiucloOpcion == "si" or SeguroSalirArtiucloOpcion == "s":
                            clearConsole()
                            print("Saliste De Create Articulo Menu")
                            OpcionCreateArticulo = True

                        elif SeguroSalirArtiucloOpcion == "n" or SeguroSalirArtiucloOpcion == "no":
                            clearConsole()
                            OpcionCreateArticulo = False
                    else:
                        clearConsole()
                        OpcionCreateArticulo = False
            #################################################### CREATE CAJON ####################################################
            elif RespuestaMetodoCreate == 2:
                clearConsole()
                print("METODO CREATE: Cajon")

                OpcionCreateCajon = False
                while OpcionCreateCajon != True:
                    print(C.RESET+C.OK+"1)Crear Un Nuevo Cajon \n2)Agreagar Carpetas A Cajon \n3)SALIR")
                    try:
                        RespuestaOpcionCreateCajon = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionCreateCajon = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionCreateCajon == 1: 
                        clearConsole()
                        idCajon = int(input("id: "))
                        Seccion = input("Seccion Cajon")
                        Cajon.CreateCajon(idCajon, Seccion)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateCajon == 2:
                        clearConsole()
                        print("¿A Que Cajon Quieres Agregar Carpetas?")
                        idCajon = int(input("id: "))
                        Cajon.CrateAddCarpetas(idCajon)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateCajon == 3:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del CREATE : CAJON?", end=" ")
                        try:
                            SeguroSalirCajonOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirCajonOpcion = "no"

                        if  SeguroSalirCajonOpcion == "y" or SeguroSalirCajonOpcion == "yes" or SeguroSalirCajonOpcion == "si" or SeguroSalirCajonOpcion == "s":
                            clearConsole()
                            print("Saliste De Create Cajon Menu")
                            OpcionCreateCajon = True

                        elif SeguroSalirCajonOpcion == "n" or SeguroSalirCajonOpcion == "no":
                            clearConsole()
                            OpcionCreateCajon = False
                    else:
                        clearConsole()
                        OpcionCreateCajon = False       
            #################################################### CREATE CARPETA ####################################################
            elif RespuestaMetodoCreate == 3:
                clearConsole()
                print("METODO CREATE: Carpeta")

                OpcionCreateCarpeta = False
                while OpcionCreateCarpeta != True:
                    print(C.RESET+C.OK+"1)Crear Nueva Carpeta \n2)Agregar Documento A Carpeta \n3)SALIR")
                    try:
                        RespuestaOpcionCreateCarpeta = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionCreateCarpeta = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionCreateCarpeta == 1: 
                        clearConsole()
                        idCarpeta = int(input("id: "))
                        Nombre = input("Nombre: ") 
                        Carpeta.CreateCarpeta(idCarpeta, Nombre)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateCarpeta == 2:
                        clearConsole()
                        print("¿A Que Carpeta Quieres Agregar Documetnos?")
                        idCarpeta = int(input("id: "))
                        Carpeta.CrateAddDocumentos(idCarpeta)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateCarpeta == 3:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del CREATE : CARPETA?", end=" ")
                        try:
                            SeguroSalirCarpetaOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirCarpetaOpcion = "no"

                        if  SeguroSalirCarpetaOpcion == "y" or SeguroSalirCarpetaOpcion == "yes" or SeguroSalirCarpetaOpcion == "si" or SeguroSalirCarpetaOpcion == "s":
                            clearConsole()
                            print("Saliste De Create Articulo Menu")
                            OpcionCreateCarpeta = True

                        elif SeguroSalirCarpetaOpcion == "n" or SeguroSalirCarpetaOpcion == "no":
                            clearConsole()
                            OpcionCreateCarpeta = False
                    else:
                        clearConsole()
                        OpcionCreateCarpeta = False  
            #################################################### CREATE DOCUMENTO ####################################################
            elif RespuestaMetodoCreate == 4:
                clearConsole()
                print("METODO CREATE: Documento")

                OpcionCreateDocumento = False
                while OpcionCreateDocumento != True:
                    print(C.RESET+C.OK+"1)Crear Un Nuevo Documento \n2)SALIR")
                    try:
                        RespuestaOpcionCreateDocumento = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionCreateDocumento = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionCreateDocumento == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateDocumento == 2:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del CREATE : DOCUMENTO?", end=" ")
                        try:
                            SeguroSalirDocumentoOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirDocumentoOpcion = "no"

                        if  SeguroSalirDocumentoOpcion == "y" or SeguroSalirDocumentoOpcion == "yes" or SeguroSalirDocumentoOpcion == "si" or SeguroSalirDocumentoOpcion == "s":
                            clearConsole()
                            print("Saliste De Create Articulo Menu")
                            OpcionCreateDocumento = True

                        elif SeguroSalirDocumentoOpcion == "n" or SeguroSalirDocumentoOpcion == "no":
                            clearConsole()
                            OpcionCreateDocumento = False
                    else:
                        clearConsole()
                        OpcionCreateDocumento = False        
            #################################################### CREATE SALIR ####################################################
            elif RespuestaMetodoCreate == 5:
                clearConsole()
                print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del CREATE?", end=" ")
                try:
                    SeguroSalirMetodoCreate = input("(s/n): "+C.RESET+C.OK).lower()
                except:
                    SeguroSalirMetodoCreate = "no"

                if  SeguroSalirMetodoCreate == "y" or SeguroSalirMetodoCreate == "yes" or SeguroSalirMetodoCreate == "si" or SeguroSalirMetodoCreate == "s":
                    clearConsole()
                    SalirMetodoCreate = True   
                elif SeguroSalirMetodoCreate == "n" or SeguroSalirMetodoCreate == "no":
                    clearConsole()
                    OpcionCreateArticulo = False  
            else:
                clearConsole()
                SalirMetodoCreate  = False
    #####################################################################################################################################################################################################################################READ##############################################################################################################################################################################################################################################
    elif RespuestaMenuCrud == 2:
        clearConsole()
        print("READ")
        SalirMetodoRead = False
        while SalirMetodoRead != True:
            print(C.RESET+C.WARNING+"1)ARCHIVERO \n2)CAJON \n3)CARPETA \n4)DOCUMENTO \n5)SALIR")
            try:
                RespuestaMetodoRead = int(input("Respuesta: "))        
            except:
                RespuestaMetodoRead = 0
            #################################################### Read ARTICULO ####################################################
            if RespuestaMetodoRead == 1: 
                clearConsole()
                print("METODO Read: Archivero")

                OpcionReadArticulo = False
                while OpcionReadArticulo != True:
                    print(C.RESET+C.OK+"1)Mostrar Solo Valores Propios \n2)Mostrar Valores All \n3)Mostrar Todos Los Articulso \n4)SALIR")
                    try:
                        RespuestaOpcionReadArticulo = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionReadArticulo = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionReadArticulo == 1: 
                        clearConsole()
                        idArchivero = int(input("id Archivero: "))
                        Archivero.ReadCajon(idArchivero, 1)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadArticulo == 2:
                        clearConsole()
                        idArchivero = int(input("id Archivero: "))
                        Archivero.ReadCajon(idArchivero, 2)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadArticulo == 3:
                        clearConsole()
                        Archivero.MostrarTodasLosArchvios()
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadArticulo == 4:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del READ : CAJON?", end=" ")
                        try:
                            SeguroSalirArtiucloOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirArtiucloOpcion = "no"

                        if  SeguroSalirArtiucloOpcion == "y" or SeguroSalirArtiucloOpcion == "yes" or SeguroSalirArtiucloOpcion == "si" or SeguroSalirArtiucloOpcion == "s":
                            clearConsole()
                            print("Saliste De Read Articulo Menu")
                            OpcionReadArticulo = True

                        elif SeguroSalirArtiucloOpcion == "n" or SeguroSalirArtiucloOpcion == "no":
                            clearConsole()
                            OpcionReadArticulo = False
                    else:
                        clearConsole()
                        OpcionReadArticulo = False
            #################################################### Read CAJON ####################################################
            elif RespuestaMetodoRead == 2:
                clearConsole()
                print("METODO Read: Cajon")

                OpcionReadCajon = False
                while OpcionReadCajon != True:
                    print(C.RESET+C.OK+"1)Mostrar Solo Valores Propios \n2)Mostrar Valores All \n3)Mostrar Todos Los Articulso \n4)SALIR")
                    try:
                        RespuestaOpcionReadCajon = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionReadCajon = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionReadCajon == 1: 
                        clearConsole()
                        idCajon = int(input("id Cajon: "))
                        Cajon.ReadCajon(idCajon, 1)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadCajon == 2:
                        clearConsole()
                        idCajon = int(input("id Cajon: "))
                        Cajon.ReadCajon(idCajon, 2)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadCajon == 3:
                        clearConsole()
                        Cajon.MostrarTodasLosCajones()
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadCajon == 4:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del READ : CAJON?", end=" ")
                        try:
                            SeguroSalirCajonOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirCajonOpcion = "no"

                        if  SeguroSalirCajonOpcion == "y" or SeguroSalirCajonOpcion == "yes" or SeguroSalirCajonOpcion == "si" or SeguroSalirCajonOpcion == "s":
                            clearConsole()
                            print("Saliste De Read Cajon Menu")
                            OpcionReadCajon = True

                        elif SeguroSalirCajonOpcion == "n" or SeguroSalirCajonOpcion == "no":
                            clearConsole()
                            OpcionReadCajon = False
                    else:
                        clearConsole()
                        OpcionReadCajon = False       
            #################################################### Read CARPETA ####################################################
            elif RespuestaMetodoRead == 3:
                clearConsole()
                print("METODO Read: Carpeta")

                OpcionReadCarpeta = False
                while OpcionReadCarpeta != True:
                    print(C.RESET+C.OK+"1)Mostrar Solo Valores Propios \n2)Mostrar Valores All \n3)Mostrar Todos Los Articulso \n4)SALIR")
                    try:
                        RespuestaOpcionReadCarpeta = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionReadCarpeta = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionReadCarpeta == 1: 
                        clearConsole()
                        idCarpeta = int(input("id Carpeta: "))
                        Carpeta.ReadCajon(idCarpeta, 1)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadCarpeta == 2:
                        clearConsole()
                        idCarpeta = int(input("id Carpeta: "))
                        Carpeta.ReadCajon(idCarpeta, 2)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadCarpeta == 3:
                        clearConsole()
                        Carpeta.MostrarTodasLasCarpetas()
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadCarpeta == 4:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del READ : CARPETA?", end=" ")
                        try:
                            SeguroSalirCarpetaOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirCarpetaOpcion = "no"

                        if  SeguroSalirCarpetaOpcion == "y" or SeguroSalirCarpetaOpcion == "yes" or SeguroSalirCarpetaOpcion == "si" or SeguroSalirCarpetaOpcion == "s":
                            clearConsole()
                            print("Saliste De Read Articulo Menu")
                            OpcionReadCarpeta = True

                        elif SeguroSalirCarpetaOpcion == "n" or SeguroSalirCarpetaOpcion == "no":
                            clearConsole()
                            OpcionReadCarpeta = False
                    else:
                        clearConsole()
                        OpcionReadCarpeta = False  
            #################################################### Read DOCUMENTO ####################################################
            elif RespuestaMetodoRead == 4:
                clearConsole()
                print("METODO Read: Documento")

                OpcionReadDocumento = False
                while OpcionReadDocumento != True:
                    print(C.RESET+C.OK+"1)Mostrar Solo Valores Propios \n2)Mostrar Valores All \n3)Mostrar Todos Los Articulso \n4)SALIR")
                    try:
                        RespuestaOpcionReadDocumento = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionReadDocumento = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionReadDocumento == 1: 
                        clearConsole()
                        idDocumento = int(input("id Documento: "))
                        Documento.ReadDocumento(idDocumento, 1)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadDocumento == 2:
                        clearConsole()
                        idDocumento = int(input("id Documento: "))
                        Documento.ReadDocumento(idDocumento, 2)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadDocumento == 3:
                        clearConsole()
                        Documento.MostrarTodosLosDocumentos()
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadDocumento == 4:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del READ : DOCUMENTO?", end=" ")
                        try:
                            SeguroSalirDocumentoOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirDocumentoOpcion = "no"

                        if  SeguroSalirDocumentoOpcion == "y" or SeguroSalirDocumentoOpcion == "yes" or SeguroSalirDocumentoOpcion == "si" or SeguroSalirDocumentoOpcion == "s":
                            clearConsole()
                            print("Saliste De Read Articulo Menu")
                            OpcionReadDocumento = True

                        elif SeguroSalirDocumentoOpcion == "n" or SeguroSalirDocumentoOpcion == "no":
                            clearConsole()
                            OpcionReadDocumento = False
                    else:
                        clearConsole()
                        OpcionReadDocumento = False        
            #################################################### Read SALIR ####################################################
            elif RespuestaMetodoRead == 5:
                clearConsole()
                print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del READ?", end=" ")
                try:
                    SeguroSalirMetodoRead = input("(s/n): "+C.RESET+C.OK).lower()
                except:
                    SeguroSalirMetodoRead = "no"

                if  SeguroSalirMetodoRead == "y" or SeguroSalirMetodoRead == "yes" or SeguroSalirMetodoRead == "si" or SeguroSalirMetodoRead == "s":
                    clearConsole()
                    SalirMetodoRead = True   
                elif SeguroSalirMetodoRead == "n" or SeguroSalirMetodoRead == "no":
                    clearConsole()
                    OpcionReadArticulo = False  
            else:
                clearConsole()
                SalirMetodoRead  = False

    #####################################################################################################################################################################################################################################UPDATE############################################################################################################################################################################################################################################
    elif RespuestaMenuCrud == 3:
        clearConsole()
        print("UPDATE")
        SalirMetodoUpdate = False
        while SalirMetodoUpdate != True:
            print(C.RESET+C.WARNING+"1)ARCHIVERO \n2)CAJON \n3)CARPETA \n4)DOCUMENTO \n5)SALIR")
            try:
                RespuestaMetodoUpdate = int(input("Respuesta: "))        
            except:
                RespuestaMetodoUpdate = 0
            #################################################### Update ARTICULO ####################################################
            if RespuestaMetodoUpdate == 1: 
                clearConsole()
                print("METODO Update: Archivero")

                OpcionUpdateArticulo = False
                while OpcionUpdateArticulo != True:
                    print(C.RESET+C.OK+"1)Actualizar Articulo \n2)SALIR")
                    try:
                        RespuestaOpcionUpdateArticulo = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionUpdateArticulo = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionUpdateArticulo == 1: 
                        clearConsole()
                        print("¿Que Archivero quieres Actualizar by id?")
                        idArchivero = int(input("id Archivero: "))
                        Archivero.UpdateArchiveroById(idArchivero)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateArticulo == 2:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del UPDATE : CAJON?", end=" ")
                        try:
                            SeguroSalirArtiucloOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirArtiucloOpcion = "no"

                        if  SeguroSalirArtiucloOpcion == "y" or SeguroSalirArtiucloOpcion == "yes" or SeguroSalirArtiucloOpcion == "si" or SeguroSalirArtiucloOpcion == "s":
                            clearConsole()
                            print("Saliste De Update Articulo Menu")
                            OpcionUpdateArticulo = True

                        elif SeguroSalirArtiucloOpcion == "n" or SeguroSalirArtiucloOpcion == "no":
                            clearConsole()
                            OpcionUpdateArticulo = False
                    else:
                        clearConsole()
                        OpcionUpdateArticulo = False
            #################################################### Update CAJON ####################################################
            elif RespuestaMetodoUpdate == 2:
                clearConsole()
                print("METODO Update: Cajon")

                OpcionUpdateCajon = False
                while OpcionUpdateCajon != True:
                    print(C.RESET+C.OK+"1)Actualizar Articulo \n2)SALIR")
                    try:
                        RespuestaOpcionUpdateCajon = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionUpdateCajon = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionUpdateCajon == 1: 
                        clearConsole()
                        print("¿Que Cajon quieres Actualizar by id?")
                        idCajon = int(input("id Archivero: "))
                        Cajon.UpdateCajonById(idCajon)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateCajon == 2:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del UPDATE : CAJON?", end=" ")
                        try:
                            SeguroSalirCajonOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirCajonOpcion = "no"

                        if  SeguroSalirCajonOpcion == "y" or SeguroSalirCajonOpcion == "yes" or SeguroSalirCajonOpcion == "si" or SeguroSalirCajonOpcion == "s":
                            clearConsole()
                            print("Saliste De Update Cajon Menu")
                            OpcionUpdateCajon = True

                        elif SeguroSalirCajonOpcion == "n" or SeguroSalirCajonOpcion == "no":
                            clearConsole()
                            OpcionUpdateCajon = False
                    else:
                        clearConsole()
                        OpcionUpdateCajon = False       
            #################################################### Update CARPETA ####################################################
            elif RespuestaMetodoUpdate == 3:
                clearConsole()
                print("METODO Update: Carpeta")

                OpcionUpdateCarpeta = False
                while OpcionUpdateCarpeta != True:
                    print(C.RESET+C.OK+"1)Actualizar Articulo \n2)SALIR")
                    try:
                        RespuestaOpcionUpdateCarpeta = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionUpdateCarpeta = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionUpdateCarpeta == 1: 
                        clearConsole()
                        print("¿Que Carpeta quieres Actualizar by id?")
                        idCarpeta = int(input("id Archivero: "))
                        Carpeta.UpdateCarpetaById(idCarpeta)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateCarpeta == 2:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del UPDATE : CARPETA?", end=" ")
                        try:
                            SeguroSalirCarpetaOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirCarpetaOpcion = "no"

                        if  SeguroSalirCarpetaOpcion == "y" or SeguroSalirCarpetaOpcion == "yes" or SeguroSalirCarpetaOpcion == "si" or SeguroSalirCarpetaOpcion == "s":
                            clearConsole()
                            print("Saliste De Update Articulo Menu")
                            OpcionUpdateCarpeta = True

                        elif SeguroSalirCarpetaOpcion == "n" or SeguroSalirCarpetaOpcion == "no":
                            clearConsole()
                            OpcionUpdateCarpeta = False
                    else:
                        clearConsole()
                        OpcionUpdateCarpeta = False  
            #################################################### Update DOCUMENTO ####################################################
            elif RespuestaMetodoUpdate == 4:
                clearConsole()
                print("METODO Update: Documento")

                OpcionUpdateDocumento = False
                while OpcionUpdateDocumento != True:
                    print(C.RESET+C.OK+"1)Actualizar Articulo \n2)SALIR")
                    try:
                        RespuestaOpcionUpdateDocumento = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionUpdateDocumento = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionUpdateDocumento == 1: 
                        clearConsole()
                        print("¿Que Documento quieres Actualizar by id?")
                        idDocumento = int(input("id Archivero: "))
                        Documento.UpdateDocumentoById(idDocumento)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateDocumento == 2:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del UPDATE : DOCUMENTO?", end=" ")
                        try:
                            SeguroSalirDocumentoOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirDocumentoOpcion = "no"

                        if  SeguroSalirDocumentoOpcion == "y" or SeguroSalirDocumentoOpcion == "yes" or SeguroSalirDocumentoOpcion == "si" or SeguroSalirDocumentoOpcion == "s":
                            clearConsole()
                            print("Saliste De Update Articulo Menu")
                            OpcionUpdateDocumento = True

                        elif SeguroSalirDocumentoOpcion == "n" or SeguroSalirDocumentoOpcion == "no":
                            clearConsole()
                            OpcionUpdateDocumento = False
                    else:
                        clearConsole()
                        OpcionUpdateDocumento = False        
            #################################################### Update SALIR ####################################################
            elif RespuestaMetodoUpdate == 5:
                clearConsole()
                print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del UPDATE?", end=" ")
                try:
                    SeguroSalirMetodoUpdate = input("(s/n): "+C.RESET+C.OK).lower()
                except:
                    SeguroSalirMetodoUpdate = "no"

                if  SeguroSalirMetodoUpdate == "y" or SeguroSalirMetodoUpdate == "yes" or SeguroSalirMetodoUpdate == "si" or SeguroSalirMetodoUpdate == "s":
                    clearConsole()
                    SalirMetodoUpdate = True   
                elif SeguroSalirMetodoUpdate == "n" or SeguroSalirMetodoUpdate == "no":
                    clearConsole()
                    OpcionUpdateArticulo = False  
            else:
                clearConsole()
                SalirMetodoUpdate  = False

    #####################################################################################################################################################################################################################################DELETE############################################################################################################################################################################################################################################
    elif RespuestaMenuCrud == 4:
        clearConsole()
        print("DELETE") 
        SalirMetodoDelete = False
        while SalirMetodoDelete != True:
            print(C.RESET+C.WARNING+"1)ARCHIVERO \n2)CAJON \n3)CARPETA \n4)DOCUMENTO \n5)SALIR")
            try:
                RespuestaMetodoDelete = int(input("Respuesta: "))        
            except:
                RespuestaMetodoDelete = 0
            #################################################### Delete ARTICULO ####################################################
            if RespuestaMetodoDelete == 1: 
                clearConsole()
                print("METODO Delete: Archivero")

                OpcionDeleteArticulo = False
                while OpcionDeleteArticulo != True:
                    print(C.RESET+C.OK+"1)Eliminar Archivero \n2)SALIR")
                    try:
                        RespuestaOpcionDeleteArticulo = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionDeleteArticulo = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionDeleteArticulo == 1: 
                        clearConsole()
                        print("¿Que Archivero Quieres Eliminar?")
                        idArchivero = int(input("id Archivero"))
                        Archivero.DeleteArchivero(idArchivero)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteArticulo == 2:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del DELETE : CAJON?", end=" ")
                        try:
                            SeguroSalirArtiucloOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirArtiucloOpcion = "no"

                        if  SeguroSalirArtiucloOpcion == "y" or SeguroSalirArtiucloOpcion == "yes" or SeguroSalirArtiucloOpcion == "si" or SeguroSalirArtiucloOpcion == "s":
                            clearConsole()
                            print("Saliste De Delete Articulo Menu")
                            OpcionDeleteArticulo = True

                        elif SeguroSalirArtiucloOpcion == "n" or SeguroSalirArtiucloOpcion == "no":
                            clearConsole()
                            OpcionDeleteArticulo = False
                    else:
                        clearConsole()
                        OpcionDeleteArticulo = False
            #################################################### Delete CAJON ####################################################
            elif RespuestaMetodoDelete == 2:
                clearConsole()
                print("METODO Delete: Cajon")

                OpcionDeleteCajon = False
                while OpcionDeleteCajon != True:
                    print(C.RESET+C.OK+"1)Eliminar Archivero \n2)SALIR")
                    try:
                        RespuestaOpcionDeleteCajon = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionDeleteCajon = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionDeleteCajon == 1: 
                        clearConsole()
                        print("¿Que Cajon Quieres Eliminar?")
                        idCajon = int(input("id Cajon: "))
                        Cajon.DeleteCajon(idCajon)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteCajon == 2:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del DELETE : CAJON?", end=" ")
                        try:
                            SeguroSalirCajonOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirCajonOpcion = "no"

                        if  SeguroSalirCajonOpcion == "y" or SeguroSalirCajonOpcion == "yes" or SeguroSalirCajonOpcion == "si" or SeguroSalirCajonOpcion == "s":
                            clearConsole()
                            print("Saliste De Delete Cajon Menu")
                            OpcionDeleteCajon = True

                        elif SeguroSalirCajonOpcion == "n" or SeguroSalirCajonOpcion == "no":
                            clearConsole()
                            OpcionDeleteCajon = False
                    else:
                        clearConsole()
                        OpcionDeleteCajon = False       
            #################################################### Delete CARPETA ####################################################
            elif RespuestaMetodoDelete == 3:
                clearConsole()
                print("METODO Delete: Carpeta")

                OpcionDeleteCarpeta = False
                while OpcionDeleteCarpeta != True:
                    print(C.RESET+C.OK+"1)Eliminar Archivero \n2)SALIR")
                    try:
                        RespuestaOpcionDeleteCarpeta = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionDeleteCarpeta = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionDeleteCarpeta == 1: 
                        clearConsole()
                        print("¿Que Carpeta Quieres Eliminar?")
                        idCarpeta = int(input("id Carpeta: "))
                        Carpeta.DeleteCarpeta(idCarpeta)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteCarpeta == 2:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del DELETE : CARPETA?", end=" ")
                        try:
                            SeguroSalirCarpetaOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirCarpetaOpcion = "no"

                        if  SeguroSalirCarpetaOpcion == "y" or SeguroSalirCarpetaOpcion == "yes" or SeguroSalirCarpetaOpcion == "si" or SeguroSalirCarpetaOpcion == "s":
                            clearConsole()
                            print("Saliste De Delete Articulo Menu")
                            OpcionDeleteCarpeta = True

                        elif SeguroSalirCarpetaOpcion == "n" or SeguroSalirCarpetaOpcion == "no":
                            clearConsole()
                            OpcionDeleteCarpeta = False
                    else:
                        clearConsole()
                        OpcionDeleteCarpeta = False  
            #################################################### Delete DOCUMENTO ####################################################
            elif RespuestaMetodoDelete == 4:
                clearConsole()
                print("METODO Delete: Documento")

                OpcionDeleteDocumento = False
                while OpcionDeleteDocumento != True:
                    print(C.RESET+C.OK+"1)Eliminar Archivero \n2)SALIR")
                    try:
                        RespuestaOpcionDeleteDocumento = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionDeleteDocumento = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionDeleteDocumento == 2: 
                        clearConsole()
                        print("¿Que Documento Quieres Eliminar?")
                        idDocumento = int(input("id Documento: "))
                        Documento.DeleteDocumento(idDocumento)
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteDocumento == 4:
                        clearConsole()
                        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del DELETE : DOCUMENTO?", end=" ")
                        try:
                            SeguroSalirDocumentoOpcion = input("(s/n): "+C.RESET+C.OK).lower()
                        except:
                            SeguroSalirDocumentoOpcion = "no"

                        if  SeguroSalirDocumentoOpcion == "y" or SeguroSalirDocumentoOpcion == "yes" or SeguroSalirDocumentoOpcion == "si" or SeguroSalirDocumentoOpcion == "s":
                            clearConsole()
                            print("Saliste De Delete Articulo Menu")
                            OpcionDeleteDocumento = True

                        elif SeguroSalirDocumentoOpcion == "n" or SeguroSalirDocumentoOpcion == "no":
                            clearConsole()
                            OpcionDeleteDocumento = False
                    else:
                        clearConsole()
                        OpcionDeleteDocumento = False        
            #################################################### Delete SALIR ####################################################
            elif RespuestaMetodoDelete == 5:
                clearConsole()
                print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del DELETE?", end=" ")
                try:
                    SeguroSalirMetodoDelete = input("(s/n): "+C.RESET+C.OK).lower()
                except:
                    SeguroSalirMetodoDelete = "no"

                if  SeguroSalirMetodoDelete == "y" or SeguroSalirMetodoDelete == "yes" or SeguroSalirMetodoDelete == "si" or SeguroSalirMetodoDelete == "s":
                    clearConsole()
                    SalirMetodoDelete = True   
                elif SeguroSalirMetodoDelete == "n" or SeguroSalirMetodoDelete == "no":
                    clearConsole()
                    OpcionDeleteArticulo = False  
            else:
                clearConsole()
                SalirMetodoDelete  = False

    #####################################################################################################################################################################################################################################SALIR#############################################################################################################################################################################################################################################
    elif RespuestaMenuCrud == 5:
        clearConsole()
        print(C.RESET+C.FAIL+"¿Seguro Que Quieres Salir Del Programa?", end=" ")
        try:
            SeguroSalirMetodoDelete = input("(s/n): "+C.RESET+C.OK).lower()
        except:
            SeguroSalirMetodoDelete = "no"
        if  SeguroSalirMetodoDelete == "y" or SeguroSalirMetodoDelete == "yes" or SeguroSalirMetodoDelete == "si" or SeguroSalirMetodoDelete == "s":
            clearConsole()
            SalirMenuCrud = True   
        elif SeguroSalirMetodoDelete == "n" or SeguroSalirMetodoDelete == "no":
            clearConsole()
            SalirMenuCrud = False  
    else: 
        clearConsole()
        SalirMenuCrud = False
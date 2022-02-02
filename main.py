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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionCreateArticulo = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionCreateArticulo = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionCreateArticulo == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateArticulo == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateArticulo == 3:
                        clearConsole()
                        print("Opcion Tres")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateArticulo == 4:
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionCreateCajon = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionCreateCajon = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionCreateCajon == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateCajon == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateCajon == 3:
                        clearConsole()
                        print("Opcion Tres")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateCajon == 4:
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionCreateCarpeta = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionCreateCarpeta = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionCreateCarpeta == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateCarpeta == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateCarpeta == 3:
                        clearConsole()
                        print("Opcion Tres")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateCarpeta == 4:
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
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
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateDocumento == 3:
                        clearConsole()
                        print("Opcion Tres")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionCreateDocumento == 4:
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionReadArticulo = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionReadArticulo = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionReadArticulo == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadArticulo == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadArticulo == 3:
                        clearConsole()
                        print("Opcion Tres")
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionReadCajon = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionReadCajon = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionReadCajon == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadCajon == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadCajon == 3:
                        clearConsole()
                        print("Opcion Tres")
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionReadCarpeta = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionReadCarpeta = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionReadCarpeta == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadCarpeta == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadCarpeta == 3:
                        clearConsole()
                        print("Opcion Tres")
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionReadDocumento = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionReadDocumento = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionReadDocumento == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadDocumento == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionReadDocumento == 3:
                        clearConsole()
                        print("Opcion Tres")
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionUpdateArticulo = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionUpdateArticulo = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionUpdateArticulo == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateArticulo == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateArticulo == 3:
                        clearConsole()
                        print("Opcion Tres")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateArticulo == 4:
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionUpdateCajon = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionUpdateCajon = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionUpdateCajon == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateCajon == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateCajon == 3:
                        clearConsole()
                        print("Opcion Tres")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateCajon == 4:
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionUpdateCarpeta = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionUpdateCarpeta = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionUpdateCarpeta == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateCarpeta == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateCarpeta == 3:
                        clearConsole()
                        print("Opcion Tres")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateCarpeta == 4:
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionUpdateDocumento = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionUpdateDocumento = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionUpdateDocumento == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateDocumento == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateDocumento == 3:
                        clearConsole()
                        print("Opcion Tres")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionUpdateDocumento == 4:
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionDeleteArticulo = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionDeleteArticulo = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionDeleteArticulo == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteArticulo == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteArticulo == 3:
                        clearConsole()
                        print("Opcion Tres")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteArticulo == 4:
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionDeleteCajon = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionDeleteCajon = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionDeleteCajon == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteCajon == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteCajon == 3:
                        clearConsole()
                        print("Opcion Tres")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteCajon == 4:
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionDeleteCarpeta = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionDeleteCarpeta = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionDeleteCarpeta == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteCarpeta == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteCarpeta == 3:
                        clearConsole()
                        print("Opcion Tres")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteCarpeta == 4:
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
                    print(C.RESET+C.OK+"1)OpcionUno \n2)OpcionDos \n3)OpcionTres \n4)SALIR")
                    try:
                        RespuestaOpcionDeleteDocumento = int(input("Respuesta: "))        
                    except:
                        RespuestaOpcionDeleteDocumento = 0
                    ############################# OPCIONES ############################
                    if RespuestaOpcionDeleteDocumento == 1: 
                        clearConsole()
                        print("Opcion Uno")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteDocumento == 2:
                        clearConsole()
                        print("Opcion Dos")
                    ############################# OPCIONES ############################
                    elif RespuestaOpcionDeleteDocumento == 3:
                        clearConsole()
                        print("Opcion Tres")
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
                               

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("CREAR UN ARCHIVERO NUEVO")                       
                        idA = int(input("id: "))
                        NombreA =input("Nombre: ")
                        
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
                                    ObjetoDocumento = Documento.BucarIdListaDocumentos(int(i))
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
                                Carpeta.CarpetasLista[ObjetoCarpeta].ReadCarpetaAll()
                            else:
                                print(f"El Archivero Con id: {ObjetoCarpeta} No Se Encontro")
                            SalirClientes = False

                    elif OC == "y" or OC == "yes" or OC == "si" or OC == "s":
                        print("¿De Que Carpeta Quires Mostrar Su Informacion?")
                        ObjetoCarpeta = int(input("Respuesta: "))
                        ObjetoCarpeta = Carpeta.ReadCarpetasById(ObjetoCarpeta)
                        if ObjetoCarpeta > -1:
                            Carpeta.CarpetasLista[ObjetoCarpeta].ReadOnlyCarpetaById()
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
                        ObjetoDocumenot = Documento.BucarIdListaDocumentos(ObjetoDocumenot)
                        if ObjetoDocumenot > -1:
                            Documento.DocumentosLista[ObjetoDocumenot].ReadOnlyDocumentoById()
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
                        ObjetoCajon = Cajon.ReadCajonById(idA)
                        if ObjetoCajon > -1:
                            newNombre = input("Agregar Nueva Seccion: ")
                            Cajon.CajonesLista[ObjetoCajon].SeccionCajon = newNombre
                            Cajon.CajonesLista[ObjetoCajon].ReadOnlyCajonById() 
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
                        ObjetoDocumento = Documento.BucarIdListaDocumentos(idA)
                        if ObjetoDocumento > -1:
                            newNombre = input("Agregar Nuevo Nombre: ")
                            newTexto = input("Agregar Nuevo Texto: ")
                            Documento.DocumentosLista[ObjetoDocumento].UpdateDocumento(newNombre, newTexto)
                            Documento.DocumentosLista[ObjetoDocumento].ReadOnlyDocumentoById() 
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
                         
                        SalirClientes = False

            ##################################################################################################################
            #   DAR DELETE CAJON
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
                            Cajon.CajonesLista[ObjetoCajon].ReadOnlyCajonById()
                            Cajon.CajonesLista.pop(ObjetoCajon)
                        else:
                            print(f"No Exite el Archivero con Id: {idA}")  
                        SalirClientes = False


            ##################################################################################################################
            #   DAR DELETE CARPETA
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
                            Carpeta.CarpetasLista[ObjetoCarpeta].ReadOnlyCarpetaById()
                            Carpeta.CarpetasLista.pop(ObjetoCarpeta)
                        else:
                            print(f"No Exite el Archivero con Id: {idA}")  
                        SalirClientes = False


            ##################################################################################################################
            #   DAR DELETE DOCUMENTO
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
                        print("¿Que Documento Quieres Eliminar?")
                        ida = int(input("Buscar Id: "))
                        ObjetoDocumento = Carpeta.ReadCarpetasById(idA)
                        if ObjetoDocumento > -1:
                            Documento.DocumentosLista[ObjetoDocumento].ReadOnlyDocumentoById()
                            Documento.DocumentosLista.pop(ObjetoDocumento)
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

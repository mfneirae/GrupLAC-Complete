#
#
# #############################################################################
#       Copyright (c) 2018 Universidad Nacional de Colombia All Rights Reserved.
#
#             This work was made as a development to improve data collection
#       for self-assessment and accreditation processes in the Vicedeanship
#       of academic affairs in the Engineering Faculty of the Universidad
#       Nacional de Colombia and is licensed under a Creative Commons
#       Attribution-NonCommercial - ShareAlike 4.0 International License
#       and MIT Licence.
#
#       by Manuel Embus.
#
#       For more information write me to jai@mfneirae.com
#       Or visit my webpage at https://mfneirae.com/
# #############################################################################
#
#
import openpyxl, sys, os, time, logging
start_time = time.time()
Dir = os.getcwd()
os.chdir(Dir+"/Bin")
sys.path.append('../Bin/')
import init
import datosbasicos
os.chdir(Dir)
condition = 0;
while condition != 1:
    try:
        print ("------> Seleccione la forma en la que desea obtener la información:")
        print ("1) Imprimir datos en CSV y en Insert")
        print ("2) Imprimir datos en Insert para MySQL")
        print ("3) Imprimir datos en CSV")
        mode = int(input('-> Seleccione una opción: '))
        if mode == 1 or mode == 2 or mode == 3:
            condition = 1
        else:
            print ("El varlor escogido no es valido")
    except ValueError:
        print ("Not a number")

wb = openpyxl.load_workbook('./Input/Base.xlsx')
# wb = openpyxl.load_workbook('./Input/Base.xlsx')
sheet = wb['Sheet1']
total = sheet.max_row +1
COD_PRODUCTO = 1;
init.inicio()
LOG_FILENAME = './Logs/Registros.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,
                        format = '%(asctime)s:%(levelname)s:%(message)s')
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}
if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)
print("------> Los GrupLAC han sido cargados, Estado: " + str(1/(total-1)*100) + "%")
for q in range(2,total):
    coduapa = sheet['A'+str(q)].value
    codhermes = sheet['B'+str(q)].value
    codcolciencias = sheet['C'+str(q)].value
    nombregi = sheet['D'+str(q)].value
    dnilider = sheet['E'+str(q)].value
    my_url = sheet['F'+str(q)].value
    datosbasicos.datosextract()
    datosbasicos.institucionesextract()
    datosbasicos.lineasextract()
    datosbasicos.sectoresextract()
    datosbasicos.integrantesextract()
    print("El grupo: " + nombregi + " ha sido  procesado, Estado: " + str(q/(total-1)*100) + "%")
    # from datosbasicos import conteventos
    # COD_PRODUCTO = int("".join(str(x) for x in conteventos))
    if q==total-1:
        logging.shutdown()
        print ("------> Escribiendo las bases de datos.")
        if mode == 1:
            import printcsv
            import printinsert
        elif mode == 2:
            import printinsert
        else:
             import printcsv
        print ("-----------------------------------------------------------------------------------------------")
        print ("")
        print ("------> ¡Extracción Exitosa!")
        print ("------> La información se encuentra en la carpeta: Resultados.")
        print ("------> Tiempo de ejecución: %s Minutos." % ((time.time() - start_time)/60))
        print ("")
        print ("***********************************************************************************************")
        sys.exit()

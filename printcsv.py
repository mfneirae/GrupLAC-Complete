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
import init
f = open ("./Resultados/GP_DATOS_BASE.csv", "w")
for item in init.GP_DATOS_BASE_CSV:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/GP_DATOS_INSTITUCIONES.csv", "w")
for item in init.GP_DATOS_INSTITUCIONES_CSV:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/GP_DATOS_LINEAS.csv", "w")
for item in init.GP_DATOS_LINEAS_CSV:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/GP_DATOS_SECTORES.csv", "w")
for item in init.GP_DATOS_SECTORES_CSV:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/GP_DATOS_INTEGRANTES.csv", "w")
for item in init.GP_DATOS_INTEGRANTES_CSV:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

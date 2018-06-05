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

f = open ("./Resultados/GP_DATOS_BASE.sql", "w")
init.GP_DATOS_BASE = [w.replace("''", 'null') for w in init.GP_DATOS_BASE]
init.GP_DATOS_BASE = [w.replace(",,", ',null,') for w in init.GP_DATOS_BASE]
for item in init.GP_DATOS_BASE:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/GP_DATOS_INSTITUCIONES.sql", "w")
init.GP_DATOS_INSTITUCIONES = [w.replace("''", 'null') for w in init.GP_DATOS_INSTITUCIONES]
init.GP_DATOS_INSTITUCIONES = [w.replace(",,", ',null,') for w in init.GP_DATOS_INSTITUCIONES]
for item in init.GP_DATOS_INSTITUCIONES:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/GP_DATOS_LINEAS.sql", "w")
init.GP_DATOS_LINEAS = [w.replace("''", 'null') for w in init.GP_DATOS_LINEAS]
init.GP_DATOS_LINEAS = [w.replace(",,", ',null,') for w in init.GP_DATOS_LINEAS]
for item in init.GP_DATOS_LINEAS:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/GP_DATOS_SECTORES.sql", "w")
init.GP_DATOS_SECTORES = [w.replace("''", 'null') for w in init.GP_DATOS_SECTORES]
init.GP_DATOS_SECTORES = [w.replace(",,", ',null,') for w in init.GP_DATOS_SECTORES]
for item in init.GP_DATOS_SECTORES:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/GP_DATOS_INTEGRANTES.sql", "w")
init.GP_DATOS_INTEGRANTES = [w.replace("''", 'null') for w in init.GP_DATOS_INTEGRANTES]
init.GP_DATOS_INTEGRANTES = [w.replace(",,", ',null,') for w in init.GP_DATOS_INTEGRANTES]
for item in init.GP_DATOS_INTEGRANTES:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/REL_GRUPO_PRODUCTO.sql", "w")
init.REL_GRUPO_PRODUCTO = [w.replace("''", 'null') for w in init.REL_GRUPO_PRODUCTO]
init.REL_GRUPO_PRODUCTO = [w.replace(",,", ',null,') for w in init.REL_GRUPO_PRODUCTO]
for item in init.REL_GRUPO_PRODUCTO:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/GP_PROD_BIB.sql", "w")
init.GP_PROD_BIB = [w.replace("''", 'null') for w in init.GP_PROD_BIB]
init.GP_PROD_BIB = [w.replace(",,", ',null,') for w in init.GP_PROD_BIB]
for item in init.GP_PROD_BIB:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/GP_PROD_TEC.sql", "w")
init.GP_PROD_TEC = [w.replace("''", 'null') for w in init.GP_PROD_TEC]
init.GP_PROD_TEC = [w.replace(",,", ',null,') for w in init.GP_PROD_TEC]
for item in init.GP_PROD_TEC:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/GP_APROPIACION.sql", "w")
init.GP_APROPIACION = [w.replace("''", 'null') for w in init.GP_APROPIACION]
init.GP_APROPIACION = [w.replace(",,", ',null,') for w in init.GP_APROPIACION]
for item in init.GP_APROPIACION:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/GP_OBRAS.sql", "w")
init.GP_OBRAS = [w.replace("''", 'null') for w in init.GP_OBRAS]
init.GP_OBRAS = [w.replace(",,", ',null,') for w in init.GP_OBRAS]
for item in init.GP_OBRAS:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/GP_ACTIVIDADES_FORM.sql", "w")
init.GP_ACTIVIDADES_FORM = [w.replace("''", 'null') for w in init.GP_ACTIVIDADES_FORM]
init.GP_ACTIVIDADES_FORM = [w.replace(",,", ',null,') for w in init.GP_ACTIVIDADES_FORM]
for item in init.GP_ACTIVIDADES_FORM:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

f = open ("./Resultados/v_colciencias_tipo_producto.sql", "w")
init.inv_colciencias_tipo_producto = [w.replace("''", 'null') for w in init.inv_colciencias_tipo_producto]
init.inv_colciencias_tipo_producto = [w.replace(",,", ',null,') for w in init.inv_colciencias_tipo_producto]
for item in init.inv_colciencias_tipo_producto:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()

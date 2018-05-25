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
def inicio():
    global GP_DATOS_BASE
    global GP_DATOS_BASE_CSV
    global GP_DATOS_INSTITUCIONES
    global GP_DATOS_INSTITUCIONES_CSV
    global GP_DATOS_LINEAS
    global GP_DATOS_LINEAS_CSV
    global GP_DATOS_SECTORES
    global GP_DATOS_SECTORES_CSV

    GP_DATOS_BASE = []
    GP_DATOS_INSTITUCIONES = []
    GP_DATOS_LINEAS = []
    GP_DATOS_SECTORES = []

    GP_DATOS_BASE_CSV = ["CODGP;\
Año Formación;\
Mes Formación;\
Lugar;\
Nombre Lider;\
Información Certificada;\
Página Web;\
Correo;\
Clasificación;\
Área del Conocimiento;\
Programa Nacional;\
Programa Nacional 2;\
Plan de trabajo;\
Estado del Arte;\
Objetivos;\
Retos;\
Visión\n"]

    GP_DATOS_INSTITUCIONES_CSV = ["CODGP_INSTI;\
CODGP;\
Nombre Institución\n"]

    GP_DATOS_LINEAS_CSV = ["CODGP_INSTI;\
CODGP;\
Línea de Investigación\n"]

    GP_DATOS_SECTORES_CSV = ["CODGP_INSTI;\
CODGP;\
Sector\n"]

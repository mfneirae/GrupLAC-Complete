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

def clc(str):
    import re
    str = re.sub(r'[^A-Za-z0-9:=_?ÁÀÉÈÍÌÓñÒÚÙéèáàéñèíìúùóò .\-/+]',r'',re.sub(' +',' ',str.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    return str;

def datosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url
    import bs4, logging, sys, re, init
    global contdatoss
    LOG_FILENAME = './Logs/Registros.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,
        format = "%(asctime)s:%(levelname)s:%(message)s")
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level)
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    all = 0
    a = 0
    x = 0
    y = 0
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("table")
    for a in range(0,len(containers)):
        buscadatoss = containers[a].td
        #print(buscadatoss)
        try:
            if buscadatoss.text == "Datos básicos":
                all = a + 1
                #print(all)
                break
        except AttributeError:
            pass
    if all != 0:
        containerb = containers[all - 1]
        container = containerb.findAll("tr")
        cont = container[1]
        info_datos = cont.text
    #Año de Inicio
        index1 = info_datos.find("Año y mes de formación") + 22
        index2 = info_datos.find(" -")
        anoinidatos = clc(info_datos[index1:index2]);
    #Mes Inicio
        index1 = index2 + 2
        index2 = len(info_datos)
        mesinidatos = clc(info_datos[index1:index2]);
        cont = container[2]
        info_datos = cont.text
    #Lugar
        index1 = info_datos.find("Departamento - Ciudad") + 22
        index2 = len(info_datos)
        Lugar = clc(info_datos[index1:index2]);
    #Lider
        cont = container[3]
        info_datos = cont.text
        index1 = info_datos.find("Líder ") + 7
        index2 = len(info_datos)
        Lider = clc(info_datos[index1:index2]);
    #Info Certificada
        cont = container[4]
        info_datos = cont.text
        index1 = info_datos.find("¿La información de este grupo se ha certificado?") + 48
        index2 = len(info_datos)
        InfoCer = clc(info_datos[index1:index2]);
    #Página web
        cont = container[5]
        info_datos = cont.text
        index1 = info_datos.find("Página web") + 10
        index2 = len(info_datos)
        Paginaweb = clc(info_datos[index1:index2]);
    #Email
        cont = container[6]
        info_datos = cont.text
        index1 = info_datos.find("E-mail") + 6
        index2 = len(info_datos)
        Email = clc(info_datos[index1:index2]);
    #Clasificación
        cont = container[7]
        info_datos = cont.text
        index1 = info_datos.find("Clasificación") + 13
        index2 = len(info_datos)
        Clasisfica = clc(info_datos[index1:index2]);
    #Área del conocimiento
        cont = container[8]
        info_datos = cont.text
        index1 = info_datos.find("Área de conocimiento") + 20
        index2 = len(info_datos)
        Area = clc(info_datos[index1:index2]);
    #Programa Nacional de Ciencia y Tecnología
        cont = container[9]
        info_datos = cont.text
        index1 = info_datos.find("Programa nacional de ciencia y tecnología") + 41
        index2 = len(info_datos)
        ProgramaNacional = clc(info_datos[index1:index2]);
    #Programa Nacional de Ciencia y Tecnología2
        cont = container[10]
        info_datos = cont.text
        index1 = info_datos.find("Programa nacional de ciencia y tecnología (secundario)") + 54
        index2 = len(info_datos)
        ProgramaNacional2 = clc(info_datos[index1:index2]);
    else:
        print(' El Grupo de Investigación ' + nombregi + ' no tiene datos Asociados')
        anoinidatos = 0000
        mesinidatos = 00
        Lugar = ""
        Lider = ""
        InfoCer = ""
        Paginaweb = ""
        Email = ""
        Clasisfica = ""
        Area = ""
        ProgramaNacional = ""
        ProgramaNacional2 = ""
        logging.info(' El Grupo de Investigación ' + nombregi + ' no tiene datos Asociados')
    for a in range(0,len(containers)):
        buscadatoss = containers[a].td
        #print(buscadatoss)
        try:
            if buscadatoss.text == "Plan Estratégico":
                all = a + 1
                #print(all)
                break
        except AttributeError:
            pass
    if all != 0:
        containerb = containers[all - 1]
    #Plan Trabajo
        info_datos = containerb.text
        index1 = info_datos.find("Plan de trabajo:") + 16
        index2 = info_datos.find("                    Estado del arte: ")
        PlanTrabajo = clc(info_datos[index1:index2]);
    #Estado del arte
        index1 = index2 + 37
        index2 = info_datos.find("                    Objetivos: ")
        EstadoArte = clc(info_datos[index1:index2]);
    #Objetivos
        index1 = index2 + 31
        index2 = info_datos.find("                    Retos: ")
        Objetivos = clc(info_datos[index1:index2]);
    #Retos
        index1 = index2 + 27
        index2 = info_datos.find("                    Visión: ")
        Retos = clc(info_datos[index1:index2]);
    #Vision
        index1 = index2 + 28
        index2 = len(info_datos)
        Vision = clc(info_datos[index1:index2]);
    else:
        print(' El Grupo de Investigación ' + nombregi + ' no tiene plan estratégico asociado')
        PlanTrabajo = ""
        EstadoArte = ""
        Objetivos = ""
        Retos = ""
        Vision = ""
        logging.info(' El Grupo de Investigación ' + nombregi + ' no tiene datos Asociados')
    #csv
    init.GP_DATOS_BASE_CSV.append(str(codcolciencias) + ";"\
    + anoinidatos + ";" \
    + mesinidatos + ";" \
    + Lugar + ";" \
    + Lider + ";" \
    + InfoCer + ";" \
    + Paginaweb + ";" \
    + Email + ";" \
    + Clasisfica + ";" \
    + Area + ";" \
    + ProgramaNacional + ";" \
    + ProgramaNacional2 + ";" \
    + PlanTrabajo + ";" \
    + EstadoArte + ";" \
    + Objetivos + ";" \
    + Retos + ";" \
    + Vision + "\n")
    #Insert
    init.GP_DATOS_BASE.append( \
    "REPLACE INTO `uapa_db`.`GP_DATOS_BASE`(`CODGP`,`Año_Formación`,`Mes_Formación`,`Lugar`,`Nombre_Lider`,`Información_Certificada`,`Página_Web`,`Correo`,`Clasificación`,`Área_del_Conocimiento`,`Programa_Nacional`,`Programa_Nacional_2`,`Plan_de_trabajo`,`Estado_del_Arte`,`Objetivos`,`Retos`,`Visión`) VALUES"
    + "('" + str(codcolciencias) + "',"\
    + anoinidatos + "," \
    + mesinidatos + "," \
    + "'" + Lugar + "'," \
    + "'" + Lider + "'," \
    + "'" + InfoCer + "'," \
    + "'" + Paginaweb + "'," \
    + "'" + Email + "'," \
    + "'" + Clasisfica + "'," \
    + "'" + Area + "'," \
    + "'" + ProgramaNacional + "'," \
    + "'" + ProgramaNacional2 + "'," \
    + "'" + PlanTrabajo + "'," \
    + "'" + EstadoArte + "'," \
    + "'" + Objetivos + "'," \
    + "'" + Retos + "'," \
    + "'" + Vision + "'" \
    + ");\n")

def institucionesextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url
    import bs4, logging, sys, re, init
    global contdatoss
    LOG_FILENAME = './Logs/Registros.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,
        format = "%(asctime)s:%(levelname)s:%(message)s")
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level)
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    all = 0
    a = 0
    x = 0
    y = 0
    COD_INSTI = 1;
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("table")
    for a in range(0,len(containers)):
        buscadatoss = containers[a].td
        #print(buscadatoss)
        try:
            if buscadatoss.text == "Instituciones":
                all = a
                #print(all)
                break
        except AttributeError:
            pass
    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("tr")
        for x in range(1, len(container)):
            cont = container[x]
            info_instituciones = cont.text
            index1 = info_instituciones.find('-') + 1
            index2 = len(info_instituciones)
            institucion = clc(info_instituciones[index1:index2])
            #csv
            init.GP_DATOS_INSTITUCIONES_CSV.append(str(codcolciencias) + str(COD_INSTI) + ";"\
            + str(codcolciencias) + ";" \
            + institucion + "\n")
            #Insert
            init.GP_DATOS_INSTITUCIONES.append( \
            "REPLACE INTO `uapa_db`.`GP_DATOS_INSTITUCIONES`(`CODGP_INSTI`,`CODGP`,`INSTITUCIÓN`) VALUES"
            + "('" + str(codcolciencias) + str(COD_INSTI) + "',"\
            + str(codcolciencias) + ","\
            + "'" + institucion + "'" \
            + ");\n")
            COD_INSTI = COD_INSTI + 1
    else:
        logging.info(' El Grupo de investigación no tiene instituciones Asociadas')

def lineasextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url
    import bs4, logging, sys, re, init
    global contdatoss
    LOG_FILENAME = './Logs/Registros.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,
        format = "%(asctime)s:%(levelname)s:%(message)s")
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level)
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    all = 0
    a = 0
    x = 0
    y = 0
    COD_LINEA = 1;
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("table")
    for a in range(0,len(containers)):
        buscadatoss = containers[a].td
        #print(buscadatoss)
        try:
            if buscadatoss.text == "Líneas de investigación declaradas por el grupo":
                all = a
                #print(all)
                break
        except AttributeError:
            pass
    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("tr")
        for x in range(1, len(container)):
            cont = container[x]
            info_lineas = cont.text
            index1 = info_lineas.find('-') + 1
            index2 = len(info_lineas)
            institucion = clc(info_lineas[index1:index2])
            #csv
            init.GP_DATOS_LINEAS_CSV.append(str(codcolciencias) + str(COD_LINEA) + ";"\
            + str(codcolciencias) + ";" \
            + institucion + "\n")
            #Insert
            init.GP_DATOS_LINEAS.append( \
            "REPLACE INTO `uapa_db`.`GP_DATOS_LINEAS`(`CODGP_LINEA`,`CODGP`,`Nombre_Línea_Inv`) VALUES"
            + "('" + str(codcolciencias) + str(COD_LINEA) + "',"\
            + "'" + str(codcolciencias) + "',"\
            + "'" + institucion + "'" \
            + ");\n")
            COD_LINEA = COD_LINEA + 1
    else:
        logging.info(' El Grupo de investigación no tiene lineas Asociadas')

def sectoresextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url
    import bs4, logging, sys, re, init
    global contdatoss
    LOG_FILENAME = './Logs/Registros.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,
        format = "%(asctime)s:%(levelname)s:%(message)s")
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level)
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    all = 0
    a = 0
    x = 0
    y = 0
    COD_SECTOR = 1;
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("table")
    for a in range(0,len(containers)):
        buscadatoss = containers[a].td
        #print(buscadatoss)
        try:
            if buscadatoss.text == "Sectores de aplicación":
                all = a
                #print(all)
                break
        except AttributeError:
            pass
    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("tr")
        for x in range(1, len(container)):
            cont = container[x]
            info_sectores = cont.text
            index1 = info_sectores.find('-') + 1
            index2 = len(info_sectores)
            institucion = clc(info_sectores[index1:index2])
            #csv
            init.GP_DATOS_SECTORES_CSV.append(str(codcolciencias) + str(COD_SECTOR) + ";"\
            + str(codcolciencias) + ";" \
            + institucion + "\n")
            #Insert
            init.GP_DATOS_SECTORES.append( \
            "REPLACE INTO `uapa_db`.`GP_DATOS_SECTORES`(`CODGP_SECTOR`,`CODGP`,`Sector_de_Aplicación`) VALUES"
            + "('" + str(codcolciencias) + str(COD_SECTOR) + "',"\
            + "'" + str(codcolciencias) + "',"\
            + "'" + institucion + "'" \
            + ");\n")
            COD_SECTOR = COD_SECTOR + 1
    else:
        logging.info(' El Grupo de investigación no tiene sectores Asociadas')

def integrantesextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url
    import bs4, logging, sys, re, init
    global contdatoss
    LOG_FILENAME = './Logs/Registros.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,
        format = "%(asctime)s:%(levelname)s:%(message)s")
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level)
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    all = 0
    a = 0
    x = 0
    y = 0
    COD_INTEGRANTES = 1;
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("table")
    for a in range(0,len(containers)):
        buscadatoss = containers[a].td
        #print(buscadatoss)
        try:
            if buscadatoss.text == "Integrantes del grupo":
                all = a
                #print(all)
                break
        except AttributeError:
            pass
    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("tr")
        for x in range(2, len(container)):
            cont = container[x]
            info_integrantes = str(cont)
            #RH
            index1 = info_integrantes.find('cod_rh=') + 7
            index2 = info_integrantes.find('"',index1,len(info_integrantes))
            cod_rh = clc(info_integrantes[index1:index2])
            #csvs
            index1 = info_integrantes.find('href="') + 6
            index2 = info_integrantes.find('"',index1,len(info_integrantes))
            linkcv = clc(info_integrantes[index1:index2])
            #Nombre
            index = index2
            index1 = info_integrantes.find('blank">',index,len(info_integrantes)) + 7
            index2 = info_integrantes.find('</a>',index1,len(info_integrantes))
            nombre = clc(info_integrantes[index1:index2])
            #Vinculación
            index = index2
            index1 = info_integrantes.find('">',index,len(info_integrantes)) + 2
            index2 = info_integrantes.find('</td>',index1,len(info_integrantes))
            tipvincula = clc(info_integrantes[index1:index2])
            #HorasDedicación
            index = index2
            index1 = info_integrantes.find('">',index,len(info_integrantes)) + 2
            index2 = info_integrantes.find('</td>',index1,len(info_integrantes))
            horasdedic = clc(info_integrantes[index1:index2])
            #Duración Vincula
            index = index2
            index1 = info_integrantes.find('">',index,len(info_integrantes)) + 2
            index2 = info_integrantes.find('</td>',index1,len(info_integrantes))
            index = index2
            duravincula = clc(info_integrantes[index1:index2])
            index2 = info_integrantes.find('-',index1,len(info_integrantes))
            duravinculaini = clc(info_integrantes[index1:index2])
            index1 = index2 + 2
            index2 = index
            duravinculafin = clc(info_integrantes[index1:index2])

            init.GP_DATOS_INTEGRANTES_CSV.append(str(codcolciencias) + str(COD_INTEGRANTES) + ";"\
            + str(codcolciencias) + ";" \
            + str(cod_rh) + ";" \
            + str(linkcv) + ";" \
            + nombre + ";" \
            + tipvincula + ";" \
            + str(horasdedic) + ";" \
            + str(duravincula) + ";" \
            + str(duravinculaini) + ";" \
            + str(duravinculafin) + "\n")
            #Insert
            init.GP_DATOS_INTEGRANTES.append( \
            "REPLACE INTO `uapa_db`.`GP_DATOS_INTEGRANTES`('CODGP_INTEGRANTE','CODGP','COD_RG','CVLAC','NOMBRE_COMPLETO','Tipo_Vinculación','Horas_de_Dedicación','Duración_Vinculación','Inicio_Vinculación','Fin_Vinculación','Fin_Vinculación') VALUES"
            + "('" + str(codcolciencias) + str(COD_INTEGRANTES) + "',"\
            + "'" + str(codcolciencias) + "',"\
            + "'" + str(cod_rh) + "',"\
            + "'" + linkcv + "'," \
            + "'" + nombre + "'," \
            + "'" + tipvincula + "'," \
            + str(horasdedic) + ","\
            + "'" + duravincula + "'," \
            + "'" + duravinculaini + "'," \
            + "'" + duravinculafin + "'" \
            + ");\n")
            COD_INTEGRANTES = COD_INTEGRANTES + 1
    else:
        logging.info(' El Grupo de investigación no tiene integrantes Asociados')

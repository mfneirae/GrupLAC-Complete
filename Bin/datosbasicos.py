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
        anoinidatos = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    #Mes Inicio
        index1 = index2 + 2
        index2 = len(info_datos)
        mesinidatos = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
        cont = container[2]
        info_datos = cont.text
    #Lugar
        index1 = info_datos.find("Departamento - Ciudad") + 22
        index2 = len(info_datos)
        Lugar = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    #Lider
        cont = container[3]
        info_datos = cont.text
        index1 = info_datos.find("Líder ") + 7
        index2 = len(info_datos)
        Lider = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    #Info Certificada
        cont = container[4]
        info_datos = cont.text
        index1 = info_datos.find("¿La información de este grupo se ha certificado?") + 48
        index2 = len(info_datos)
        InfoCer = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    #Página web
        cont = container[5]
        info_datos = cont.text
        index1 = info_datos.find("Página web") + 10
        index2 = len(info_datos)
        Paginaweb = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    #Email
        cont = container[6]
        info_datos = cont.text
        index1 = info_datos.find("E-mail") + 6
        index2 = len(info_datos)
        Email = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    #Clasificación
        cont = container[7]
        info_datos = cont.text
        index1 = info_datos.find("Clasificación") + 13
        index2 = len(info_datos)
        Clasisfica = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    #Área del conocimiento
        cont = container[8]
        info_datos = cont.text
        index1 = info_datos.find("Área de conocimiento") + 20
        index2 = len(info_datos)
        Area = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    #Programa Nacional de Ciencia y Tecnología
        cont = container[9]
        info_datos = cont.text
        index1 = info_datos.find("Programa nacional de ciencia y tecnología") + 41
        index2 = len(info_datos)
        ProgramaNacional = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    #Programa Nacional de Ciencia y Tecnología2
        cont = container[10]
        info_datos = cont.text
        index1 = info_datos.find("Programa nacional de ciencia y tecnología (secundario)") + 54
        index2 = len(info_datos)
        ProgramaNacional2 = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
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
        PlanTrabajo = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    #Estado del arte
        index1 = index2 + 37
        index2 = info_datos.find("                    Objetivos: ")
        EstadoArte = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    #Objetivos
        index1 = index2 + 31
        index2 = info_datos.find("                    Retos: ")
        Objetivos = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    #Retos
        index1 = index2 + 27
        index2 = info_datos.find("                    Visión: ")
        Retos = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    #Vision
        index1 = index2 + 28
        index2 = len(info_datos)
        Vision = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
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
    "REPLACE INTO `uapa_db`.`GP_DATOS_BASE`(`CODGP`,`Año Formación`,`Mes Formación`,`Lugar`,`Nombre Lider`,`Información Certificada`,`Página Web`,`Correo`,`Clasificación`,`Área del Conocimiento`,`Programa Nacional`,`Programa Nacional 2`,`Plan de trabajo`,`Estado del Arte`,`Objetivos`,`Retos`,`Visión`) VALUES"
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

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
    str = re.sub(r'[^A-Za-z0-9:=_?ÁÀÉÈÍÌÓÒÚÙéèáà,éñèíìńúùóò .\-/+]',r'',re.sub(' +',' ',str.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    if str == ",":
        str = "-"
    return str;

def ediciones_apropiacionextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contediciones_apropiacion
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
        buscaediciones_apropiacion = containers[a].td
        #print(buscaediciones_apropiacion)
        try:
            if buscaediciones_apropiacion.text == "Ediciones":
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
            info_ediciones_apropiacion = cont.text
            index1 = info_ediciones_apropiacion.find("- ") + 2
            index2 = info_ediciones_apropiacion.find(':')
            tipo = clc(info_ediciones_apropiacion[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Anales":
                tipo = "97"
            elif tipo.strip() == "Libro":
                tipo = "98"
            elif tipo.strip() == "Revista":
                tipo = "120"
            else:
                logging.critical('Añadir: ' + tipo + ' a ediciones_apropiacion')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_ediciones_apropiacion.find('\n', index1, len(info_ediciones_apropiacion))
            nombreart = clc(info_ediciones_apropiacion[index1:index2])
            index1 = index2 + 2
            index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
            lugar = clc(info_ediciones_apropiacion[index1:index2])
            index1 = index2 + 2
            index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
            anopub = clc(info_ediciones_apropiacion[index1:index2])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""
            index1 = info_ediciones_apropiacion.find('Editorial:') + 10
            index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
            editorial = clc(info_ediciones_apropiacion[index1:index2])
            index1 = info_ediciones_apropiacion.find('Idiomas:') + 8
            index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
            idioma = clc(info_ediciones_apropiacion[index1:index2])
            index1 = info_ediciones_apropiacion.find('Páginas:') + 8
            index2 = info_ediciones_apropiacion.find('\n', index1, len(info_ediciones_apropiacion))
            paginas = clc(info_ediciones_apropiacion[index1:index2])
            index1 = info_ediciones_apropiacion.find('Autores:') + 9
            index2 = info_ediciones_apropiacion.find('/n', index1, len(info_ediciones_apropiacion))
            autores = clc(info_ediciones_apropiacion[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "'" + lugar + "'," \
            + anopub + "," \
            + "'" + idioma + "'," \
            + "'" + paginas + "'," \
            + "null" + "," \
            + "'" + editorial + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + autores + "'" \
            + ");\n")
            init.REL_GRUPO_PRODUCTO_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) +";" \
            + tipo +";" \
            + nombreart +";" \
            + lugar +";" \
            + anopub +";" \
            + idioma +";" \
            + paginas +";" \
            + "" +";" \
            + editorial +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_APROPIACION.append( \
            "REPLACE INTO `uapa_db`.`GP_APROPIACION`(`CODGP_PROD_APROPIACION`,`CODGP_PROD`,`Tipos_de_Participación`,`Fecha_Inicio`,`Fecha_Fin`,`Proyecto_de_Inv`,`Medio_de_publicación`,`Emisora`,`Número_de_Participantes`) VALUES"
            + "('" + str(codcolciencias) + "A" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_APROPIACION_CSV.append(str(codcolciencias) + "A" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contediciones_apropiacion = [COD_PRODUCTO]

def eventos_cientificosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global conteventos_cientificos
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
        buscaeventos_cientificos = containers[a].td
        #print(buscaeventos_cientificos)
        try:
            if buscaeventos_cientificos.text == "Eventos Científicos":
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
            info_eventos_cientificos = cont.text
            index1 = info_eventos_cientificos.find("- ") + 2
            index2 = info_eventos_cientificos.find(':')
            tipo = clc(info_eventos_cientificos[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Otro":
                tipo = "97"
            elif tipo.strip() == "Taller":
                tipo = "98"
            elif tipo.strip() == "Congreso":
                tipo = "99"
            elif tipo.strip() == "Encuentro":
                tipo = "100"
            elif tipo.strip() == "Seminario":
                tipo = "101"
            elif tipo.strip() == "Simposio":
                tipo = "102"
            else:
                logging.critical('Añadir: ' + tipo + ' a eventos_cientificos')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_eventos_cientificos.find('\n', index1, len(info_eventos_cientificos))
            nombreart = clc(info_eventos_cientificos[index1:index2])
            index1 = index2 + 2
            index2 = info_eventos_cientificos.find(',', index1, len(info_eventos_cientificos))
            lugar = clc(info_eventos_cientificos[index1:index2])
            index1 = info_eventos_cientificos.find(', desde ') + 8
            index2 = info_eventos_cientificos.find(' - \n                ', index1, len(info_eventos_cientificos))
            desde = clc(info_eventos_cientificos[index1:index2])
            anopub = clc(desde[index1:index1 + 4])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""
            index1 = info_eventos_cientificos.find('- \n                hasta ') + 25
            index2 = info_eventos_cientificos.find('\n', index1, len(info_eventos_cientificos))
            hasta = clc(info_eventos_cientificos[index1:index2])
            index1 = info_eventos_cientificos.find('Ámbito:') + 7
            index2 = info_eventos_cientificos.find(',', index1, len(info_eventos_cientificos))
            ambito = clc(info_eventos_cientificos[index1:index2])
            index1 = info_eventos_cientificos.find('Tipos de participación:') + 23
            index2 = info_eventos_cientificos.find('\n', index1, len(info_eventos_cientificos))
            participacion = clc(info_eventos_cientificos[index1:index2])
            index1 = info_eventos_cientificos.find('Nombre de la institución:') + 25
            index2 = info_eventos_cientificos.find('\n', index1, len(info_eventos_cientificos))
            institucion = clc(info_eventos_cientificos[index1:index2])
            index1 = info_eventos_cientificos.find('Tipo de vinculación') + 19
            index2 = info_eventos_cientificos.find('\n', index1, len(info_eventos_cientificos))
            vinculacion = clc(info_eventos_cientificos[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "'" + lugar + "'," \
            + anopub + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + ambito + "'," \
            + "null" + "," \
            + "null" + "," \
            + "'" + institucion + "'," \
            + "'" + vinculacion + "'," \
            + "null" \
            + ");\n")
            init.REL_GRUPO_PRODUCTO_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) +";" \
            + tipo +";" \
            + nombreart +";" \
            + lugar +";" \
            + anopub +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + ambito +";" \
            + "" +";" \
            + "" +";" \
            + institucion +";" \
            + vinculacion +";" \
            + "" +";" \
            + "\n")
            init.GP_APROPIACION.append( \
            "REPLACE INTO `uapa_db`.`GP_APROPIACION`(`CODGP_PROD_APROPIACION`,`CODGP_PROD`,`Tipos_de_Participación`,`Fecha_Inicio`,`Fecha_Fin`,`Proyecto_de_Inv`,`Medio_de_publicación`,`Emisora`,`Número_de_Participantes`) VALUES"
            + "('" + str(codcolciencias) + "A" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + participacion + "'," \
            + "'" + desde + "'," \
            + "'" + hasta + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_APROPIACION_CSV.append(str(codcolciencias) + "A" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + participacion +";" \
            + desde +";" \
            + hasta +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    conteventos_cientificos = [COD_PRODUCTO]

def informes_investigacionextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global continformes_investigacion
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
        buscainformes_investigacion = containers[a].td
        #print(buscainformes_investigacion)
        try:
            if buscainformes_investigacion.text == "Informes de investigación":
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
            info_informes_investigacion = cont.text
            index1 = info_informes_investigacion.find("- ") + 2
            index2 = info_informes_investigacion.find(':')
            tipo = clc(info_informes_investigacion[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Informes de investigación":
                tipo = "103"
            else:
                logging.critical('Añadir: ' + tipo + ' a informes_investigacion')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_informes_investigacion.find('\n', index1, len(info_informes_investigacion))
            nombreart = clc(info_informes_investigacion[index1:index2])
            index1 = index2 + 2
            index2 = info_informes_investigacion.find(',', index1, len(info_informes_investigacion))
            anopub = clc(info_informes_investigacion[index1:index2])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""
            index1 = info_informes_investigacion.find('Proyecto de investigación:') + 26
            index2 = info_informes_investigacion.find('Autores:', index1, len(info_informes_investigacion))
            proyecto = clc(info_informes_investigacion[index1:index2])
            index1 = info_informes_investigacion.find('Autores:') + 9
            index2 = info_informes_investigacion.find('/n', index1, len(info_informes_investigacion))
            autores = clc(info_informes_investigacion[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "null" + "," \
            + anopub + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + autores + "'" \
            + ");\n")
            init.REL_GRUPO_PRODUCTO_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) +";" \
            + tipo +";" \
            + nombreart +";" \
            + "" +";" \
            + anopub +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_APROPIACION.append( \
            "REPLACE INTO `uapa_db`.`GP_APROPIACION`(`CODGP_PROD_APROPIACION`,`CODGP_PROD`,`Tipos_de_Participación`,`Fecha_Inicio`,`Fecha_Fin`,`Proyecto_de_Inv`,`Medio_de_publicación`,`Emisora`,`Número_de_Participantes`) VALUES"
            + "('" + str(codcolciencias) + "A" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + proyecto + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_APROPIACION_CSV.append(str(codcolciencias) + "A" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + proyecto +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    continformes_investigacion = [COD_PRODUCTO]

def redes_conocimientosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contredes_conocimientos
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
        buscaredes_conocimientos = containers[a].td
        #print(buscaredes_conocimientos)
        try:
            if buscaredes_conocimientos.text == "Redes de Conocimiento Especializado":
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
            info_redes_conocimientos = cont.text
            index1 = info_redes_conocimientos.find("- ") + 2
            index2 = info_redes_conocimientos.find(':')
            tipo = "1"
            index1 = info_redes_conocimientos.find("- ") + 2
            index2 = info_redes_conocimientos.find('\n')
            nombreart = clc(info_redes_conocimientos[index1:index2])
            index1 = info_redes_conocimientos.find('\n                en',index2,len(info_redes_conocimientos)) + 20
            index2 = info_redes_conocimientos.find(', desde ', index1, len(info_redes_conocimientos))
            lugar = clc(info_redes_conocimientos[index1:index2])
            index1 = info_redes_conocimientos.find(', desde ',index2,len(info_redes_conocimientos)) + 8
            index2 = info_redes_conocimientos.find(' - \n', index1, len(info_redes_conocimientos))
            desde = clc(info_redes_conocimientos[index1:index2])
            anopub = clc(info_redes_conocimientos[index1:index1+4])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""
            index1 = info_redes_conocimientos.find('\n                hasta',index2,len(info_redes_conocimientos)) + 24
            index2 = info_redes_conocimientos.find(' Número de participantes:', index1, len(info_redes_conocimientos))
            hasta = clc(info_redes_conocimientos[index1:index2])
            index1 = info_redes_conocimientos.find(' Número de participantes:',index2,len(info_redes_conocimientos)) + 25
            index2 = info_redes_conocimientos.find('\n', index1, len(info_redes_conocimientos))
            participantes = clc(info_redes_conocimientos[index1:index2])
            if len(participantes) > 10:
                participantes = "";
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "'" + lugar + "'," \
            + anopub + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.REL_GRUPO_PRODUCTO_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) +";" \
            + tipo +";" \
            + nombreart +";" \
            + lugar +";" \
            + anopub +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            init.GP_APROPIACION.append( \
            "REPLACE INTO `uapa_db`.`GP_APROPIACION`(`CODGP_PROD_APROPIACION`,`CODGP_PROD`,`Tipos_de_Participación`,`Fecha_Inicio`,`Fecha_Fin`,`Proyecto_de_Inv`,`Medio_de_publicación`,`Emisora`,`Número_de_Participantes`) VALUES"
            + "('" + str(codcolciencias) + "A" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "'" + desde + "'," \
            + "'" + hasta + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + participantes + "'" \
            + ");\n")
            init.GP_APROPIACION_CSV.append(str(codcolciencias) + "A" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + desde +";" \
            + hasta +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + participantes +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contredes_conocimientos = [COD_PRODUCTO]

def contenidos_impresosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contcontenidos_impresos
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
        buscacontenidos_impresos = containers[a].td
        #print(buscacontenidos_impresos)
        try:
            if buscacontenidos_impresos.text == "Generación de Contenido Impreso":
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
            info_contenidos_impresos = cont.text
            index1 = info_contenidos_impresos.find("- ") + 2
            index2 = info_contenidos_impresos.find(':')
            tipo = clc(info_contenidos_impresos[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Manual":
                tipo = "104"
            elif tipo.strip() == "Boletín":
                tipo = "105"
            elif tipo.strip() == "Cartilla":
                tipo = "121"
            else:
                logging.critical('Añadir: ' + tipo + ' a contenidos_impresos')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_contenidos_impresos.find('\n', index1, len(info_contenidos_impresos))
            nombreart = clc(info_contenidos_impresos[index1:index2])
            index1 = info_contenidos_impresos.find('\n                ',index1,len(info_contenidos_impresos)) + 17
            index2 = info_contenidos_impresos.find(',', index1, len(info_contenidos_impresos))
            desde = clc(info_contenidos_impresos[index1:index2])
            anopub = clc(info_contenidos_impresos[index1:index1 + 4])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""
            index1 = info_contenidos_impresos.find('Ambito:',index1,len(info_contenidos_impresos)) + 7
            index2 = info_contenidos_impresos.find(',', index1, len(info_contenidos_impresos))
            ambito = clc(info_contenidos_impresos[index1:index2])
            index1 = info_contenidos_impresos.find('Medio de circulación:',index1,len(info_contenidos_impresos)) + 21
            index2 = info_contenidos_impresos.find('Lugar de publicación:', index1, len(info_contenidos_impresos))
            medio = clc(info_contenidos_impresos[index1:index2])
            index1 = info_contenidos_impresos.find('Lugar de publicación:',index1,len(info_contenidos_impresos)) + 21
            index2 = info_contenidos_impresos.find(',', index1, len(info_contenidos_impresos))
            lugar = clc(info_contenidos_impresos[index1:index2])
            index1 = info_contenidos_impresos.find('Sitio web:',index1,len(info_contenidos_impresos)) + 10
            index2 = info_contenidos_impresos.find('Autores:', index1, len(info_contenidos_impresos))
            DOI = clc(info_contenidos_impresos[index1:index2])
            index1 = info_contenidos_impresos.find('Autores:') + 9
            index2 = info_contenidos_impresos.find('/n', index1, len(info_contenidos_impresos))
            autores = clc(info_contenidos_impresos[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "'" + lugar + "'," \
            + anopub + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + ambito + "'," \
            + "'" + DOI + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + autores + "'" \
            + ");\n")
            init.REL_GRUPO_PRODUCTO_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) +";" \
            + tipo +";" \
            + nombreart +";" \
            + lugar +";" \
            + anopub +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + ambito +";" \
            + DOI +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_APROPIACION.append( \
            "REPLACE INTO `uapa_db`.`GP_APROPIACION`(`CODGP_PROD_APROPIACION`,`CODGP_PROD`,`Tipos_de_Participación`,`Fecha_Inicio`,`Fecha_Fin`,`Proyecto_de_Inv`,`Medio_de_publicación`,`Emisora`,`Número_de_Participantes`) VALUES"
            + "('" + str(codcolciencias) + "A" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_APROPIACION_CSV.append(str(codcolciencias) + "A" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contcontenidos_impresos = [COD_PRODUCTO]

def contenidos_multimediaextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contcontenidos_multimedia
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
        buscacontenidos_multimedia = containers[a].td
        #print(buscacontenidos_multimedia)
        try:
            if buscacontenidos_multimedia.text == "Generación de Contenido Multimedia":
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
            info_contenidos_multimedia = cont.text
            index1 = info_contenidos_multimedia.find("- ") + 2
            index2 = info_contenidos_multimedia.find(':')
            tipo = clc(info_contenidos_multimedia[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Comentario":
                tipo = "106"
            elif tipo.strip() == "Entrevista":
                tipo = "107"
            elif tipo.strip() == "Otro":
                tipo = "123"
            else:
                logging.critical('Añadir: ' + tipo + ' a contenidos_multimedia')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_contenidos_multimedia.find('\n', index1, len(info_contenidos_multimedia))
            nombreart = clc(info_contenidos_multimedia[index1:index2])
            index1 = info_contenidos_multimedia.find('\n                ',index1,len(info_contenidos_multimedia)) + 17
            index2 = info_contenidos_multimedia.find(',', index1, len(info_contenidos_multimedia))
            anopub = clc(info_contenidos_multimedia[index1:index2])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""
            index1 = index2 + 2
            index2 = info_contenidos_multimedia.find(',', index1, len(info_contenidos_multimedia))
            lugar = clc(info_contenidos_multimedia[index1:index2])
            index1 = info_contenidos_multimedia.find('Idioma:',index1,len(info_contenidos_multimedia)) + 7
            index2 = info_contenidos_multimedia.find(' Medio de divulgación:', index1, len(info_contenidos_multimedia))
            idioma = clc(info_contenidos_multimedia[index1:index2])
            index1 = info_contenidos_multimedia.find('Medio de divulgación:',index1,len(info_contenidos_multimedia)) + 21
            index2 = info_contenidos_multimedia.find(', Sitio web:', index1, len(info_contenidos_multimedia))
            medio = clc(info_contenidos_multimedia[index1:index2])
            index1 = info_contenidos_multimedia.find('Sitio web:',index1,len(info_contenidos_multimedia)) + 10
            index2 = info_contenidos_multimedia.find('Emisora:', index1, len(info_contenidos_multimedia))
            DOI = clc(info_contenidos_multimedia[index1:index2])
            index1 = info_contenidos_multimedia.find('Emisora:',index1,len(info_contenidos_multimedia)) + 8
            index2 = info_contenidos_multimedia.find('Instituciones participantes:', index1, len(info_contenidos_multimedia))
            emisora = clc(info_contenidos_multimedia[index1:index2])
            index1 = info_contenidos_multimedia.find('Instituciones participantes:',index1,len(info_contenidos_multimedia)) + 28
            index2 = info_contenidos_multimedia.find('Autores:', index1, len(info_contenidos_multimedia))
            instituciones = clc(info_contenidos_multimedia[index1:index2])
            index1 = info_contenidos_multimedia.find('Autores:') + 9
            index2 = info_contenidos_multimedia.find('/n', index1, len(info_contenidos_multimedia))
            autores = clc(info_contenidos_multimedia[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "'" + lugar + "'," \
            + "'" + anopub + "'," \
            + "'" + idioma + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + DOI + "'," \
            + "null" + "," \
            + "'" + instituciones + "'," \
            + "null" + "," \
            + "'" + autores + "'" \
            + ");\n")
            init.REL_GRUPO_PRODUCTO_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) +";" \
            + tipo +";" \
            + nombreart +";" \
            + lugar +";" \
            + anopub +";" \
            + idioma +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + DOI +";" \
            + "" +";" \
            + instituciones +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_APROPIACION.append( \
            "REPLACE INTO `uapa_db`.`GP_APROPIACION`(`CODGP_PROD_APROPIACION`,`CODGP_PROD`,`Tipos_de_Participación`,`Fecha_Inicio`,`Fecha_Fin`,`Proyecto_de_Inv`,`Medio_de_publicación`,`Emisora`,`Número_de_Participantes`) VALUES"
            + "('" + str(codcolciencias) + "A" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + medio + "'," \
            + "'" + emisora + "'," \
            + "null" \
            + ");\n")
            init.GP_APROPIACION_CSV.append(str(codcolciencias) + "A" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + medio +";" \
            + emisora +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contcontenidos_multimedia = [COD_PRODUCTO]

def contenido_virtualextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contcontenido_virtual
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
        buscacontenido_virtual = containers[a].td
        #print(buscacontenido_virtual)
        try:
            if buscacontenido_virtual.text == "Generación de Contenido Virtual":
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
            info_contenido_virtual = cont.text
            index1 = info_contenido_virtual.find("- ") + 2
            index2 = info_contenido_virtual.find(':')
            tipo = clc(info_contenido_virtual[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Página web":
                tipo = "108"
            elif tipo.strip() == "Blog":
                tipo = "124"
            elif tipo.strip() == "Aplicativo":
                tipo = "125"
            else:
                logging.critical('Añadir: ' + tipo + ' a contenido_virtual')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_contenido_virtual.find('\n', index1, len(info_contenido_virtual))
            nombreart = clc(info_contenido_virtual[index1:index2])
            index1 = info_contenido_virtual.find('\n                ',index1,len(info_contenido_virtual)) + 17
            index2 = info_contenido_virtual.find(',', index1, len(info_contenido_virtual))
            desde = clc(info_contenido_virtual[index1:index2])
            anopub = clc(info_contenido_virtual[index1:index1 + 4])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""
            index1 = info_contenido_virtual.find('Entidades vinculadas:',index1,len(info_contenido_virtual)) + 21
            index2 = info_contenido_virtual.find('Sitio web:', index1, len(info_contenido_virtual))
            instituciones = clc(info_contenido_virtual[index1:index2])
            index1 = info_contenido_virtual.find('Sitio web:',index1,len(info_contenido_virtual)) + 10
            index2 = info_contenido_virtual.find('Autores:', index1, len(info_contenido_virtual))
            DOI = clc(info_contenido_virtual[index1:index2])
            index1 = info_contenido_virtual.find('Autores:') + 9
            index2 = info_contenido_virtual.find('/n', index1, len(info_contenido_virtual))
            autores = clc(info_contenido_virtual[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "null" + "," \
            + anopub + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + DOI + "'," \
            + "null" + "," \
            + "'" + instituciones + "'," \
            + "null" + "," \
            + "'" + autores + "'" \
            + ");\n")
            init.REL_GRUPO_PRODUCTO_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) +";" \
            + tipo +";" \
            + nombreart +";" \
            + "" +";" \
            + anopub +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + DOI +";" \
            + "" +";" \
            + instituciones +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_APROPIACION.append( \
            "REPLACE INTO `uapa_db`.`GP_APROPIACION`(`CODGP_PROD_APROPIACION`,`CODGP_PROD`,`Tipos_de_Participación`,`Fecha_Inicio`,`Fecha_Fin`,`Proyecto_de_Inv`,`Medio_de_publicación`,`Emisora`,`Número_de_Participantes`) VALUES"
            + "('" + str(codcolciencias) + "A" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "'" + desde + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_APROPIACION_CSV.append(str(codcolciencias) + "A" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + desde +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contcontenido_virtual = [COD_PRODUCTO]

def estrategias_comunicacionextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contestrategias_comunicacion
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
        buscaestrategias_comunicacion = containers[a].td
        #print(buscaestrategias_comunicacion)
        try:
            if buscaestrategias_comunicacion.text == "Estrategias de Comunicación del Conocimiento":
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
            info_estrategias_comunicacion = cont.text
            tipo = "109"
            index1 = info_estrategias_comunicacion.find("- ") + 2
            index2 = info_estrategias_comunicacion.find(':')
            nombreart = clc(info_estrategias_comunicacion[index1:index2])
            index1 = info_estrategias_comunicacion.find(': desde ',index1,len(info_estrategias_comunicacion)) + 8
            index2 = info_estrategias_comunicacion.find(' hasta ', index1, len(info_estrategias_comunicacion))
            desde = clc(info_estrategias_comunicacion[index1:index2])
            anopub = clc(info_estrategias_comunicacion[index2 - 4:index2])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""
            index1 = info_estrategias_comunicacion.find(' hasta ',index1,len(info_estrategias_comunicacion)) + 7
            index2 = info_estrategias_comunicacion.find('Descripción:', index1, len(info_estrategias_comunicacion))
            hasta = clc(info_estrategias_comunicacion[index1:index2])
            index1 = info_estrategias_comunicacion.find('Descripción:',index1,len(info_estrategias_comunicacion)) + 12
            index2 = info_estrategias_comunicacion.find('/n', index1, len(info_estrategias_comunicacion))
            descripcion = clc(info_estrategias_comunicacion[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "null" + "," \
            + anopub + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + descripcion + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.REL_GRUPO_PRODUCTO_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) +";" \
            + tipo +";" \
            + nombreart +";" \
            + "" +";" \
            + anopub +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + descripcion +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            init.GP_APROPIACION.append( \
            "REPLACE INTO `uapa_db`.`GP_APROPIACION`(`CODGP_PROD_APROPIACION`,`CODGP_PROD`,`Tipos_de_Participación`,`Fecha_Inicio`,`Fecha_Fin`,`Proyecto_de_Inv`,`Medio_de_publicación`,`Emisora`,`Número_de_Participantes`) VALUES"
            + "('" + str(codcolciencias) + "A" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "'" + desde + "'," \
            + "'" + hasta + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_APROPIACION_CSV.append(str(codcolciencias) + "A" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + desde +";" \
            + hasta +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contestrategias_comunicacion = [COD_PRODUCTO]

def estrategias_pedagogicasextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contestrategias_pedagogicas
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
        buscaestrategias_pedagogicas = containers[a].td
        #print(buscaestrategias_pedagogicas)
        try:
            if buscaestrategias_pedagogicas.text == "Estrategias Pedagógicas para el fomento a la CTI":
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
            info_estrategias_pedagogicas = cont.text
            tipo = "110"
            index1 = info_estrategias_pedagogicas.find("- ") + 2
            index2 = info_estrategias_pedagogicas.find(':')
            nombreart = clc(info_estrategias_pedagogicas[index1:index2])
            index1 = info_estrategias_pedagogicas.find(': desde ',index1,len(info_estrategias_pedagogicas)) + 8
            index2 = info_estrategias_pedagogicas.find(' hasta ', index1, len(info_estrategias_pedagogicas))
            desde = clc(info_estrategias_pedagogicas[index1:index2])
            anopub = clc(info_estrategias_pedagogicas[index2 - 4:index2])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""
            index1 = info_estrategias_pedagogicas.find(' hasta ',index1,len(info_estrategias_pedagogicas)) + 7
            index2 = info_estrategias_pedagogicas.find('Descripción:', index1, len(info_estrategias_pedagogicas))
            hasta = clc(info_estrategias_pedagogicas[index1:index2])
            index1 = info_estrategias_pedagogicas.find('Descripción:',index1,len(info_estrategias_pedagogicas)) + 12
            index2 = info_estrategias_pedagogicas.find('/n', index1, len(info_estrategias_pedagogicas))
            descripcion = clc(info_estrategias_pedagogicas[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "null" + "," \
            + anopub + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + descripcion + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.REL_GRUPO_PRODUCTO_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) +";" \
            + tipo +";" \
            + nombreart +";" \
            + "" +";" \
            + anopub +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + descripcion +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            init.GP_APROPIACION.append( \
            "REPLACE INTO `uapa_db`.`GP_APROPIACION`(`CODGP_PROD_APROPIACION`,`CODGP_PROD`,`Tipos_de_Participación`,`Fecha_Inicio`,`Fecha_Fin`,`Proyecto_de_Inv`,`Medio_de_publicación`,`Emisora`,`Número_de_Participantes`) VALUES"
            + "('" + str(codcolciencias) + "A" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "'" + desde + "'," \
            + "'" + hasta + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_APROPIACION_CSV.append(str(codcolciencias) + "A" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + desde +";" \
            + hasta +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contestrategias_pedagogicas = [COD_PRODUCTO]

def participacion_ciudadana_proyectosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contparticipacion_ciudadana_proyectos
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
        buscaparticipacion_ciudadana_proyectos = containers[a].td
        #print(buscaparticipacion_ciudadana_proyectos)
        try:
            if buscaparticipacion_ciudadana_proyectos.text == "Participación Ciudadana en Proyectos de CTI":
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
            info_participacion_ciudadana_proyectos = cont.text
            tipo = "111"
            index1 = info_participacion_ciudadana_proyectos.find("- ") + 2
            index2 = info_participacion_ciudadana_proyectos.find(':')
            nombreart = clc(info_participacion_ciudadana_proyectos[index1:index2])
            index1 = info_participacion_ciudadana_proyectos.find(': desde ',index1,len(info_participacion_ciudadana_proyectos)) + 8
            index2 = info_participacion_ciudadana_proyectos.find(' hasta ', index1, len(info_participacion_ciudadana_proyectos))
            desde = clc(info_participacion_ciudadana_proyectos[index1:index2])
            anopub = clc(info_participacion_ciudadana_proyectos[index2 - 4:index2])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""
            index1 = info_participacion_ciudadana_proyectos.find(' hasta ',index1,len(info_participacion_ciudadana_proyectos)) + 7
            index2 = info_participacion_ciudadana_proyectos.find('Descripción:', index1, len(info_participacion_ciudadana_proyectos))
            hasta = clc(info_participacion_ciudadana_proyectos[index1:index2])
            index1 = info_participacion_ciudadana_proyectos.find('Descripción:',index1,len(info_participacion_ciudadana_proyectos)) + 12
            index2 = info_participacion_ciudadana_proyectos.find('/n', index1, len(info_participacion_ciudadana_proyectos))
            descripcion = clc(info_participacion_ciudadana_proyectos[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "null" + "," \
            + anopub + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + descripcion + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.REL_GRUPO_PRODUCTO_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) +";" \
            + tipo +";" \
            + nombreart +";" \
            + "" +";" \
            + anopub +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + descripcion +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            init.GP_APROPIACION.append( \
            "REPLACE INTO `uapa_db`.`GP_APROPIACION`(`CODGP_PROD_APROPIACION`,`CODGP_PROD`,`Tipos_de_Participación`,`Fecha_Inicio`,`Fecha_Fin`,`Proyecto_de_Inv`,`Medio_de_publicación`,`Emisora`,`Número_de_Participantes`) VALUES"
            + "('" + str(codcolciencias) + "A" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "'" + desde + "'," \
            + "'" + hasta + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_APROPIACION_CSV.append(str(codcolciencias) + "A" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + desde +";" \
            + hasta +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contparticipacion_ciudadana_proyectos = [COD_PRODUCTO]

def participacion_ciudadana_espaciosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contparticipacion_ciudadana_espacios
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
        buscaparticipacion_ciudadana_espacios = containers[a].td
        #print(buscaparticipacion_ciudadana_espacios)
        try:
            if buscaparticipacion_ciudadana_espacios.text == "Espacios de Participación Ciudadana":
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
            info_participacion_ciudadana_espacios = cont.text
            tipo = "112"
            index1 = info_participacion_ciudadana_espacios.find("- ") + 2
            index2 = info_participacion_ciudadana_espacios.find('\n',index1,len(info_participacion_ciudadana_espacios))
            nombreart = clc(info_participacion_ciudadana_espacios[index1:index2])
            index1 = info_participacion_ciudadana_espacios.rfind(" en ") + 4
            lugar = clc(info_participacion_ciudadana_espacios[index1:index2])
            index1 = info_participacion_ciudadana_espacios.find(' desde ',index1,len(info_participacion_ciudadana_espacios)) + 7
            index2 = info_participacion_ciudadana_espacios.find('- hasta', index1, len(info_participacion_ciudadana_espacios))
            desde = clc(info_participacion_ciudadana_espacios[index1:index2])
            anopub = clc(info_participacion_ciudadana_espacios[index1:index1 + 4])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""
            index1 = info_participacion_ciudadana_espacios.find(' hasta ',index1,len(info_participacion_ciudadana_espacios)) + 7
            index2 = info_participacion_ciudadana_espacios.find('Número de participantes:', index1, len(info_participacion_ciudadana_espacios))
            hasta = clc(info_participacion_ciudadana_espacios[index1:index2])
            index1 = info_participacion_ciudadana_espacios.find('Número de participantes:',index1,len(info_participacion_ciudadana_espacios)) + 24
            index2 = info_participacion_ciudadana_espacios.find(', Página web:', index1, len(info_participacion_ciudadana_espacios))
            participantes = clc(info_participacion_ciudadana_espacios[index1:index2])
            index1 = info_participacion_ciudadana_espacios.find('Página web:',index1,len(info_participacion_ciudadana_espacios)) + 11
            index2 = info_participacion_ciudadana_espacios.find('\n', index1, len(info_participacion_ciudadana_espacios))
            DOI = clc(info_participacion_ciudadana_espacios[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "'" + lugar + "'," \
            + anopub + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + DOI + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.REL_GRUPO_PRODUCTO_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) +";" \
            + tipo +";" \
            + nombreart +";" \
            + lugar +";" \
            + anopub +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + DOI +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            init.GP_APROPIACION.append( \
            "REPLACE INTO `uapa_db`.`GP_APROPIACION`(`CODGP_PROD_APROPIACION`,`CODGP_PROD`,`Tipos_de_Participación`,`Fecha_Inicio`,`Fecha_Fin`,`Proyecto_de_Inv`,`Medio_de_publicación`,`Emisora`,`Número_de_Participantes`) VALUES"
            + "('" + str(codcolciencias) + "A" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "'" + desde + "'," \
            + "'" + hasta + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + participantes + "'" \
            + ");\n")
            init.GP_APROPIACION_CSV.append(str(codcolciencias) + "A" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + desde +";" \
            + hasta +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + participantes +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contparticipacion_ciudadana_espacios = [COD_PRODUCTO]

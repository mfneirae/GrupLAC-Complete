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

def cartasextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contcartas
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
        buscacartas = containers[a].td
        #print(buscacartas)
        try:
            if buscacartas.text == "Cartas, mapas o similares":
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
            info_cartas = cont.text
            index1 = info_cartas.find("- ") + 2
            index2 = info_cartas.find(':')
            tipo = clc(info_cartas[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Aerofotograma":
                tipo = "46"
            elif tipo.strip() == "Carta":
                tipo = "47"
            elif tipo.strip() == "Fotograma":
                tipo = "48"
            elif tipo.strip() == "Mapa":
                tipo = "49"
            elif tipo.strip() == "Otra":
                tipo = "50"
            else:
                logging.critical('Añadir: ' + tipo + ' a cartas')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_cartas.find('\n', index1, len(info_cartas))
            nombreart = clc(info_cartas[index1:index2])
            index1 = index2 + 2
            index2 = info_cartas.find(',', index1, len(info_cartas))
            lugar = clc(info_cartas[index1:index2])
            index1 = index2 + 2
            index2 = info_cartas.find(',', index1, len(info_cartas))
            anopub = clc(info_cartas[index1:index2])
            index1 = info_cartas.find('Institución financiadora:') + 25
            index2 = info_cartas.find(', Tema:', index1, len(info_cartas))
            institucion = clc(info_cartas[index1:index2])
            index1 = info_cartas.find('Tema:') + 5
            index2 = info_cartas.find('Autores:', index1, len(info_cartas))
            tema = clc(info_cartas[index1:index2])
            index1 = info_cartas.find('Autores:', index2, len(info_cartas)) + 9
            index2 = info_cartas.find('/br', index1, len(info_cartas))
            autores = clc(info_cartas[index1:index2])
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
            + "'" + institucion + "'," \
            + "'Financiadora'," \
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
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + tema + "'," \
            + "null" + "," \
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
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + tema +";" \
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
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene cartas Asociados')
    contcartas = [COD_PRODUCTO]

def consultoriasextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contconsultorias
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
        buscaconsultorias = containers[a].td
        #print(buscaconsultorias)
        try:
            if buscaconsultorias.text == "Consultorías científico tecnológicas e Informes técnicos":
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
            info_consultorias = cont.text
            index1 = info_consultorias.find("- ") + 2
            index2 = info_consultorias.find(':')
            tipo = clc(info_consultorias[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Servicios de proyectos de IDI":
                tipo = "52"
            elif tipo.strip() == "Comercialización de tecnología":
                tipo = "53"
            elif tipo.strip() == "Análisis de competitividad":
                tipo = "54"
            elif tipo.strip() == "Informe técnico":
                tipo = "55"
            elif tipo.strip() == "Otra":
                tipo = "56"
            elif tipo.strip() == "Acciones de transferencia tecnológica":
                tipo = "57"
            elif tipo.strip() == "Desarrollo de productos":
                tipo = "58"
            elif tipo.strip() == "Implementación de sistemas de análisis":
                tipo = "59"
            elif tipo.strip() == "Consultoría en artes,arquitectura y diseño":
                tipo = "60"
            elif tipo.strip() == "Servicios de Proyectos de I+D+I":
                tipo = "76"
            else:
                logging.critical('Añadir: ' + tipo + ' a consultorias')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_consultorias.find('\n', index1, len(info_consultorias))
            nombreart = clc(info_consultorias[index1:index2])
            index1 = index2 + 2
            index2 = info_consultorias.find(',', index1, len(info_consultorias))
            lugar = clc(info_consultorias[index1:index2])
            index1 = index2 + 2
            index2 = info_consultorias.find(',', index1, len(info_consultorias))
            anopub = clc(info_consultorias[index1:index2])
            index1 = info_consultorias.find('Idioma:') + 7
            index2 = info_consultorias.find(', Disponibilidad:', index1, len(info_consultorias))
            idioma = clc(info_consultorias[index1:index2])
            index1 = info_consultorias.find(', Disponibilidad:') + 17
            index2 = info_consultorias.find(',\n', index1, len(info_consultorias))
            disponibilidad = clc(info_consultorias[index1:index2])
            index1 = info_consultorias.find('Número del contrato:') + 20
            index2 = info_consultorias.find('Institución que se benefició del servicio:', index1, len(info_consultorias))
            contrato = clc(info_consultorias[index1:index2])
            index1 = info_consultorias.find('Institución que se benefició del servicio:') + 42
            index2 = info_consultorias.find('Autores:', index1, len(info_consultorias))
            institucion = clc(info_consultorias[index1:index2])
            index1 = info_consultorias.find('Autores:', index2, len(info_consultorias)) + 9
            index2 = info_consultorias.find('/br', index1, len(info_consultorias))
            autores = clc(info_consultorias[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "'" + lugar + "'," \
            + anopub + "," \
            + "'" + idioma + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + institucion + "'," \
            + "'Financiadora'," \
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
            + "" +";" \
            + "" +";" \
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + disponibilidad + "'," \
            + "null" + "," \
            + "null" + "," \
            + "'" + contrato + "'," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + disponibilidad +";" \
            + "" +";" \
            + "" +";" \
            + contrato +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene consultorias Asociados')
    contconsultorias = [COD_PRODUCTO]

def disenosiextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contdisenosi
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
        buscadisenosi = containers[a].td
        #print(buscadisenosi)
        try:
            if buscadisenosi.text == "Diseños industriales":
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
            info_disenosi = cont.text
            index1 = info_disenosi.find("- ") + 2
            index2 = info_disenosi.find(':')
            tipo = clc(info_disenosi[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Diseño Industrial":
                tipo = "40"
            elif tipo.strip() == "Diseńo Industrial":
                tipo = "40"
            elif tipo.strip() == "Industrial":
                tipo = "40"
            else:
                logging.critical('Añadir: ' + tipo + ' a disenosi')
            index1 = index2 + 2
            index2 = info_disenosi.find('\n                ', index1, len(info_disenosi))
            nombreart = clc(info_disenosi[index1:index2])
            index1 = index2 + 17
            index2 = info_disenosi.find(',', index1, len(info_disenosi))
            lugar = clc(info_disenosi[index1:index2])
            index1 = index2 + 2
            index2 = info_disenosi.find(',', index1, len(info_disenosi))
            anopub = clc(info_disenosi[index1:index2])
            index1 = info_disenosi.find('Disponibilidad:') + 15
            index2 = info_disenosi.find(',', index1, len(info_disenosi))
            disponibilidad = clc(info_disenosi[index1:index2])
            index1 = info_disenosi.find('Institución financiadora:') + 25
            index2 = info_disenosi.find('Autores:', index1, len(info_disenosi))
            institucion = clc(info_disenosi[index1:index2])
            index1 = info_disenosi.find('Autores:', index2, len(info_disenosi)) + 9
            index2 = info_disenosi.find('/br', index1, len(info_disenosi))
            autores = clc(info_disenosi[index1:index2])
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
            + "'" + institucion + "'," \
            + "'Financiadora'," \
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
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + disponibilidad + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + disponibilidad +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Diseños Industriales Asociados')
    contdisenosi = [COD_PRODUCTO]

def esquemas_trazadosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contesquemas_trazados
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
        buscaesquemas_trazados = containers[a].td
        #print(buscaesquemas_trazados)
        try:
            if buscaesquemas_trazados.text == "Esquemas de trazados de circuito integrado":
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
            info_esquemas_trazados = cont.text
            index1 = info_esquemas_trazados.find("- ") + 2
            index2 = info_esquemas_trazados.find(':')
            tipo = clc(info_esquemas_trazados[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Esquema de circuito integrado":
                tipo = "41"
            else:
                logging.critical('Añadir: ' + tipo + ' a esquemas_trazados')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_esquemas_trazados.find('\n                ', index1, len(info_esquemas_trazados))
            nombreart = clc(info_esquemas_trazados[index1:index2])
            index1 = index2 + 17
            index2 = info_esquemas_trazados.find(',', index1, len(info_esquemas_trazados))
            lugar = clc(info_esquemas_trazados[index1:index2])
            index1 = index2 + 2
            index2 = info_esquemas_trazados.find(',', index1, len(info_esquemas_trazados))
            anopub = clc(info_esquemas_trazados[index1:index2])
            index1 = info_esquemas_trazados.find('Disponibilidad:') + 15
            index2 = info_esquemas_trazados.find(',', index1, len(info_esquemas_trazados))
            disponibilidad = clc(info_esquemas_trazados[index1:index2])
            index1 = info_esquemas_trazados.find('Institución financiadora:') + 25
            index2 = info_esquemas_trazados.find('Autores:', index1, len(info_esquemas_trazados))
            institucion = clc(info_esquemas_trazados[index1:index2])
            index1 = info_esquemas_trazados.find('Autores:', index2, len(info_esquemas_trazados)) + 9
            index2 = info_esquemas_trazados.find('/br', index1, len(info_esquemas_trazados))
            autores = clc(info_esquemas_trazados[index1:index2])
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
            + "'" + institucion + "'," \
            + "'Financiadora'," \
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
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + disponibilidad + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + disponibilidad +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contesquemas_trazados = [COD_PRODUCTO]

def innovaciones_en_gestionextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global continnovaciones_en_gestion
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
        buscainnovaciones_en_gestion = containers[a].td
        #print(buscainnovaciones_en_gestion)
        try:
            if buscainnovaciones_en_gestion.text == "Innovaciones generadas en la Gestión Empresarial":
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
            info_innovaciones_en_gestion = cont.text
            index1 = info_innovaciones_en_gestion.find("- ") + 2
            index2 = info_innovaciones_en_gestion.find(':')
            tipo = clc(info_innovaciones_en_gestion[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Organizacional":
                tipo = "42"
            elif tipo.strip() == "Empresarial":
                tipo = "43"
            else:
                logging.critical('Añadir: ' + tipo + ' a innovaciones_en_gestion')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_innovaciones_en_gestion.find('\n                ', index1, len(info_innovaciones_en_gestion))
            nombreart = clc(info_innovaciones_en_gestion[index1:index2])
            index1 = index2 + 17
            index2 = info_innovaciones_en_gestion.find(',', index1, len(info_innovaciones_en_gestion))
            lugar = clc(info_innovaciones_en_gestion[index1:index2])
            index1 = index2 + 2
            index2 = info_innovaciones_en_gestion.find(',', index1, len(info_innovaciones_en_gestion))
            anopub = clc(info_innovaciones_en_gestion[index1:index2])
            index1 = info_innovaciones_en_gestion.find('Disponibilidad:') + 15
            index2 = info_innovaciones_en_gestion.find(',', index1, len(info_innovaciones_en_gestion))
            disponibilidad = clc(info_innovaciones_en_gestion[index1:index2])
            index1 = info_innovaciones_en_gestion.find('Institución financiadora:') + 25
            index2 = info_innovaciones_en_gestion.find('Autores:', index1, len(info_innovaciones_en_gestion))
            institucion = clc(info_innovaciones_en_gestion[index1:index2])
            index1 = info_innovaciones_en_gestion.find('Autores:', index2, len(info_innovaciones_en_gestion)) + 9
            index2 = info_innovaciones_en_gestion.find('/br', index1, len(info_innovaciones_en_gestion))
            autores = clc(info_innovaciones_en_gestion[index1:index2])
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
            + "'" + institucion + "'," \
            + "'Financiadora'," \
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
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + disponibilidad + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + disponibilidad +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    continnovaciones_en_gestion = [COD_PRODUCTO]

def innovaciones_procedimientosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global continnovaciones_procedimientos
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
        buscainnovaciones_procedimientos = containers[a].td
        #print(buscainnovaciones_procedimientos)
        try:
            if buscainnovaciones_procedimientos.text == "Innovaciones en Procesos y Procedimientos":
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
            info_innovaciones_procedimientos = cont.text
            index1 = info_innovaciones_procedimientos.find("- ") + 2
            index2 = info_innovaciones_procedimientos.find(':')
            tipo = clc(info_innovaciones_procedimientos[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Innovación de proceso o procedimiento":
                tipo = "45"
            else:
                logging.critical('Añadir: ' + tipo + ' a innovaciones_procedimientos')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_innovaciones_procedimientos.find('\n                ', index1, len(info_innovaciones_procedimientos))
            nombreart = clc(info_innovaciones_procedimientos[index1:index2])
            index1 = index2 + 17
            index2 = info_innovaciones_procedimientos.find(',', index1, len(info_innovaciones_procedimientos))
            lugar = clc(info_innovaciones_procedimientos[index1:index2])
            index1 = index2 + 2
            index2 = info_innovaciones_procedimientos.find(',', index1, len(info_innovaciones_procedimientos))
            anopub = clc(info_innovaciones_procedimientos[index1:index2])
            index1 = info_innovaciones_procedimientos.find('Disponibilidad:') + 15
            index2 = info_innovaciones_procedimientos.find(',', index1, len(info_innovaciones_procedimientos))
            disponibilidad = clc(info_innovaciones_procedimientos[index1:index2])
            index1 = info_innovaciones_procedimientos.find('Institución financiadora:') + 25
            index2 = info_innovaciones_procedimientos.find('Autores:', index1, len(info_innovaciones_procedimientos))
            institucion = clc(info_innovaciones_procedimientos[index1:index2])
            index1 = info_innovaciones_procedimientos.find('Autores:', index2, len(info_innovaciones_procedimientos)) + 9
            index2 = info_innovaciones_procedimientos.find('/br', index1, len(info_innovaciones_procedimientos))
            autores = clc(info_innovaciones_procedimientos[index1:index2])
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
            + "'" + institucion + "'," \
            + "'Financiadora'," \
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
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + disponibilidad + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + disponibilidad +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Innovaciones en Procedimientos Asociadas')
    continnovaciones_procedimientos = [COD_PRODUCTO]

def variedad_animalextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contvariedad_animal
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
        buscavariedad_animal = containers[a].td
        #print(buscavariedad_animal)
        try:
            if buscavariedad_animal.text == "Nuevas variedades animal":
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
            info_variedad_animal = cont.text
            index1 = info_variedad_animal.find("- ") + 2
            index2 = info_variedad_animal.find(':')
            tipo = clc(info_variedad_animal[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Variedad animal":
                tipo = "44"
            else:
                logging.critical('Añadir: ' + tipo + ' a variedad_animal')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_variedad_animal.find('\n                ', index1, len(info_variedad_animal))
            nombreart = clc(info_variedad_animal[index1:index2])
            index1 = index2 + 17
            index2 = info_variedad_animal.find(',', index1, len(info_variedad_animal))
            lugar = clc(info_variedad_animal[index1:index2])
            index1 = index2 + 2
            index2 = info_variedad_animal.find(',', index1, len(info_variedad_animal))
            anopub = clc(info_variedad_animal[index1:index2])
            index1 = info_variedad_animal.find('Acto administrativo del ICA:') + 28
            index2 = info_variedad_animal.find(', Institución financiadora: ', index1, len(info_variedad_animal))
            acto = clc(info_variedad_animal[index1:index2])
            index1 = info_variedad_animal.find('Institución financiadora:') + 25
            index2 = info_variedad_animal.find('Autores:', index1, len(info_variedad_animal))
            institucion = clc(info_variedad_animal[index1:index2])
            index1 = info_variedad_animal.find('Autores:', index2, len(info_variedad_animal)) + 9
            index2 = info_variedad_animal.find('/br', index1, len(info_variedad_animal))
            autores = clc(info_variedad_animal[index1:index2])
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
            + "'" + institucion + "'," \
            + "'Financiadora'," \
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
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + acto + "'" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
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
            + "" +";" \
            + acto +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Variedades Animales Asociadas')
    contvariedad_animal = [COD_PRODUCTO]

def variedad_vegetalextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contvariedad_vegetal
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
        buscavariedad_vegetal = containers[a].td
        #print(buscavariedad_vegetal)
        try:
            if buscavariedad_vegetal.text == "Nuevas variedades vegetal":
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
            info_variedad_vegetal = cont.text
            index1 = info_variedad_vegetal.find("- ") + 2
            index2 = info_variedad_vegetal.find(':')
            tipo = clc(info_variedad_vegetal[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Variedad vegetal":
                tipo = "51"
            else:
                logging.critical('Añadir: ' + tipo + ' a variedad_vegetal')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_variedad_vegetal.find('\n                ', index1, len(info_variedad_vegetal))
            nombreart = clc(info_variedad_vegetal[index1:index2])
            index1 = index2 + 17
            index2 = info_variedad_vegetal.find(',', index1, len(info_variedad_vegetal))
            lugar = clc(info_variedad_vegetal[index1:index2])
            index1 = index2 + 2
            index2 = info_variedad_vegetal.find(',', index1, len(info_variedad_vegetal))
            anopub = clc(info_variedad_vegetal[index1:index2])
            index1 = info_variedad_vegetal.find(', Sitio web:') + 12
            index2 = info_variedad_vegetal.find('\n', index1, len(info_variedad_vegetal))
            DOI = clc(info_variedad_vegetal[index1:index2])
            index1 = info_variedad_vegetal.find('Tipo de ciclo:') + 14
            index2 = info_variedad_vegetal.find(',', index1, len(info_variedad_vegetal))
            ciclo = clc(info_variedad_vegetal[index1:index2])
            index1 = info_variedad_vegetal.find('Institución financiadora:') + 25
            index2 = info_variedad_vegetal.find('Autores:', index1, len(info_variedad_vegetal))
            institucion = clc(info_variedad_vegetal[index1:index2])
            index1 = info_variedad_vegetal.find('Autores:', index2, len(info_variedad_vegetal)) + 9
            index2 = info_variedad_vegetal.find('/br', index1, len(info_variedad_vegetal))
            autores = clc(info_variedad_vegetal[index1:index2])
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
            + "'" + institucion + "'," \
            + "'Financiadora'," \
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
            + "" +";" \
            + DOI +";" \
            + "" +";" \
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" +ciclo + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + ciclo +";" \
            + "" +";" \
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
        logging.info(' El Grupo: ' + nombregi + 'no tiene Variedades Vegetales Asociadas')
    contvariedad_vegetal = [COD_PRODUCTO]

def planta_pilotoextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contplanta_piloto
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
        buscaplanta_piloto = containers[a].td
        #print(buscaplanta_piloto)
        try:
            if buscaplanta_piloto.text == "Plantas piloto":
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
            info_planta_piloto = cont.text
            index1 = info_planta_piloto.find("- ") + 2
            index2 = info_planta_piloto.find(':')
            tipo = clc(info_planta_piloto[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Planta piloto":
                tipo = "93"
            else:
                logging.critical('Añadir: ' + tipo + ' a planta_piloto')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_planta_piloto.find('\n                ', index1, len(info_planta_piloto))
            nombreart = clc(info_planta_piloto[index1:index2])
            index1 = index2 + 17
            index2 = info_planta_piloto.find(',', index1, len(info_planta_piloto))
            lugar = clc(info_planta_piloto[index1:index2])
            index1 = index2 + 2
            index2 = info_planta_piloto.find(',', index1, len(info_planta_piloto))
            anopub = clc(info_planta_piloto[index1:index2])
            index1 = info_planta_piloto.find('Nombre comercial:') + 17
            index2 = info_planta_piloto.find('Institución financiadora:', index1, len(info_planta_piloto))
            nombreplanta = clc(info_planta_piloto[index1:index2])
            index1 = info_planta_piloto.find('Disponibilidad:') + 15
            index2 = info_planta_piloto.find(',', index1, len(info_planta_piloto))
            disponibilidad = clc(info_planta_piloto[index1:index2])
            index1 = info_planta_piloto.find('Institución financiadora:') + 25
            index2 = info_planta_piloto.find('Autores:', index1, len(info_planta_piloto))
            institucion = clc(info_planta_piloto[index1:index2])
            index1 = info_planta_piloto.find('Autores:', index2, len(info_planta_piloto)) + 9
            index2 = info_planta_piloto.find('/br', index1, len(info_planta_piloto))
            autores = clc(info_planta_piloto[index1:index2])
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
            + "'" + institucion + "'," \
            + "'Financiadora'," \
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
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "'" + nombreplanta + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + disponibilidad + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + nombreplanta +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + disponibilidad +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Plantas Piloto Asociadas')
    contplanta_piloto = [COD_PRODUCTO]

def otros_productos_tecnicosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contotros_productos_tecnicos
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
        buscaotros_productos_tecnicos = containers[a].td
        #print(buscaotros_productos_tecnicos)
        try:
            if buscaotros_productos_tecnicos.text == "Otros productos tecnológicos":
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
            info_otros_productos_tecnicos = cont.text
            index1 = info_otros_productos_tecnicos.find("- ") + 2
            index2 = info_otros_productos_tecnicos.find(':')
            tipo = clc(info_otros_productos_tecnicos[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Gen Clonado":
                tipo = "36"
            elif tipo.strip() == "Coleccion biologica de referencia con informacion sistematizada":
                tipo = "37"
            elif tipo.strip() == "Otro":
                tipo = "38"
            elif tipo.strip() == "Base de datos de referencia para investigacion":
                tipo = "39"
            else:
                logging.critical('Añadir: ' + tipo + ' a otros_productos_tecnicos')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_otros_productos_tecnicos.find('\n                ', index1, len(info_otros_productos_tecnicos))
            nombreart = clc(info_otros_productos_tecnicos[index1:index2])
            index1 = index2 + 17
            index2 = info_otros_productos_tecnicos.find(',', index1, len(info_otros_productos_tecnicos))
            lugar = clc(info_otros_productos_tecnicos[index1:index2])
            index1 = index2 + 2
            index2 = info_otros_productos_tecnicos.find(',', index1, len(info_otros_productos_tecnicos))
            anopub = clc(info_otros_productos_tecnicos[index1:index2])
            index1 = info_otros_productos_tecnicos.find('Nombre comercial:') + 17
            index2 = info_otros_productos_tecnicos.find('Institución financiadora:', index1, len(info_otros_productos_tecnicos))
            nombreplanta = clc(info_otros_productos_tecnicos[index1:index2])
            index1 = info_otros_productos_tecnicos.find('Disponibilidad:') + 15
            index2 = info_otros_productos_tecnicos.find(',', index1, len(info_otros_productos_tecnicos))
            disponibilidad = clc(info_otros_productos_tecnicos[index1:index2])
            index1 = info_otros_productos_tecnicos.find('Institución financiadora:') + 25
            index2 = info_otros_productos_tecnicos.find('Autores:', index1, len(info_otros_productos_tecnicos))
            institucion = clc(info_otros_productos_tecnicos[index1:index2])
            index1 = info_otros_productos_tecnicos.find('Autores:', index2, len(info_otros_productos_tecnicos)) + 9
            index2 = info_otros_productos_tecnicos.find('/br', index1, len(info_otros_productos_tecnicos))
            autores = clc(info_otros_productos_tecnicos[index1:index2])
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
            + "'" + institucion + "'," \
            + "'Financiadora'," \
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
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "'" + nombreplanta + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + disponibilidad + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + nombreplanta +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + disponibilidad +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Plantas Piloto Asociadas')
    contotros_productos_tecnicos = [COD_PRODUCTO]

def regulaciones_normasextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contregulaciones_normas
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
        buscaregulaciones_normas = containers[a].td
        #print(buscaregulaciones_normas)
        try:
            if buscaregulaciones_normas.text == "Regulaciones y Normas":
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
            info_regulaciones_normas = cont.text
            index1 = info_regulaciones_normas.find("- ") + 2
            index2 = info_regulaciones_normas.find(':')
            tipo = clc(info_regulaciones_normas[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Ambiental o de Salud":
                tipo = "61"
            elif tipo.strip() == "Educativa":
                tipo = "62"
            elif tipo.strip() == "Social":
                tipo = "63"
            elif tipo.strip() == "Técnica":
                tipo = "64"
            elif tipo.strip() == "Guía de práctica clínica":
                tipo = "65"
            elif tipo.strip() == "Proyecto de ley":
                tipo = "66"
            elif tipo.strip() == "Técnica - Básica":
                tipo = "74"
            elif tipo.strip() == "Técnica - Ensayo":
                tipo = "75"
            elif tipo.strip() == "Técnica - Proceso":
                tipo = "77"
            else:
                logging.critical('Añadir: ' + tipo + ' a regulaciones_normas')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_regulaciones_normas.find('\n                ', index1, len(info_regulaciones_normas))
            nombreart = clc(info_regulaciones_normas[index1:index2])
            index1 = index2 + 17
            index2 = info_regulaciones_normas.find(',', index1, len(info_regulaciones_normas))
            lugar = clc(info_regulaciones_normas[index1:index2])
            index1 = index2 + 2
            index2 = info_regulaciones_normas.find(',', index1, len(info_regulaciones_normas))
            anopub = clc(info_regulaciones_normas[index1:index2])
            index1 = info_regulaciones_normas.find('Ambito:') + 7
            index2 = info_regulaciones_normas.find(',', index1, len(info_regulaciones_normas))
            ambito = clc(info_regulaciones_normas[index1:index2])
            index1 = info_regulaciones_normas.find('Disponibilidad:') + 15
            index2 = info_regulaciones_normas.find(',', index1, len(info_regulaciones_normas))
            disponibilidad = clc(info_regulaciones_normas[index1:index2])
            index1 = info_regulaciones_normas.find('Objeto:') + 7
            index2 = info_regulaciones_normas.find('Institución financiadora:', index1, len(info_regulaciones_normas))
            objeto = clc(info_regulaciones_normas[index1:index2])
            index1 = info_regulaciones_normas.find('Fecha de publicación:') + 21
            index2 = info_regulaciones_normas.find(',', index1, len(info_regulaciones_normas))
            fecha = clc(info_regulaciones_normas[index1:index2])
            index1 = info_regulaciones_normas.find('Institución financiadora:') + 25
            index2 = info_regulaciones_normas.find('Autores:', index1, len(info_regulaciones_normas))
            institucion = clc(info_regulaciones_normas[index1:index2])
            index1 = info_regulaciones_normas.find('Autores:', index2, len(info_regulaciones_normas)) + 9
            index2 = info_regulaciones_normas.find('/br', index1, len(info_regulaciones_normas))
            autores = clc(info_regulaciones_normas[index1:index2])
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
            + "'Financiadora'," \
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
            + "" +";" \
            + "" +";" \
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + objeto + "'," \
            + "'" + fecha + "'," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + objeto +";" \
            + fecha +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Plantas Piloto Asociadas')
    contregulaciones_normas = [COD_PRODUCTO]

def guias_clinicasextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contguias_clinicas
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
        buscaguias_clinicas = containers[a].td
        #print(buscaguias_clinicas)
        try:
            if buscaguias_clinicas.text == "Guias de práctica clínica":
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
            info_guias_clinicas = cont.text
            index1 = info_guias_clinicas.find("- ") + 2
            index2 = info_guias_clinicas.find(':')
            tipo = clc(info_guias_clinicas[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Ambiental o de Salud":
                tipo = "61"
            elif tipo.strip() == "Educativa":
                tipo = "62"
            elif tipo.strip() == "Social":
                tipo = "63"
            elif tipo.strip() == "Técnica":
                tipo = "64"
            elif tipo.strip() == "Guía de práctica clínica":
                tipo = "65"
            elif tipo.strip() == "Proyecto de ley":
                tipo = "66"
            elif tipo.strip() == "Técnica - Básica":
                tipo = "74"
            elif tipo.strip() == "Técnica - Ensayo":
                tipo = "75"
            elif tipo.strip() == "Técnica - Proceso":
                tipo = "77"
            else:
                logging.critical('Añadir: ' + tipo + ' a guias_clinicas' )
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_guias_clinicas.find('\n                ', index1, len(info_guias_clinicas))
            nombreart = clc(info_guias_clinicas[index1:index2])
            index1 = index2 + 17
            index2 = info_guias_clinicas.find(',', index1, len(info_guias_clinicas))
            lugar = clc(info_guias_clinicas[index1:index2])
            index1 = index2 + 2
            index2 = info_guias_clinicas.find(',', index1, len(info_guias_clinicas))
            anopub = clc(info_guias_clinicas[index1:index2])
            index1 = info_guias_clinicas.find('Ambito:') + 7
            index2 = info_guias_clinicas.find(',', index1, len(info_guias_clinicas))
            ambito = clc(info_guias_clinicas[index1:index2])
            index1 = info_guias_clinicas.find('Disponibilidad:') + 15
            index2 = info_guias_clinicas.find(',', index1, len(info_guias_clinicas))
            disponibilidad = clc(info_guias_clinicas[index1:index2])
            index1 = info_guias_clinicas.find('Objeto:') + 7
            index2 = info_guias_clinicas.find('Institución financiadora:', index1, len(info_guias_clinicas))
            objeto = clc(info_guias_clinicas[index1:index2])
            index1 = info_guias_clinicas.find('Fecha de publicación:') + 21
            index2 = info_guias_clinicas.find(',', index1, len(info_guias_clinicas))
            fecha = clc(info_guias_clinicas[index1:index2])
            index1 = info_guias_clinicas.find('Institución financiadora:') + 25
            index2 = info_guias_clinicas.find('Autores:', index1, len(info_guias_clinicas))
            institucion = clc(info_guias_clinicas[index1:index2])
            index1 = info_guias_clinicas.find('Autores:', index2, len(info_guias_clinicas)) + 9
            index2 = info_guias_clinicas.find('/br', index1, len(info_guias_clinicas))
            autores = clc(info_guias_clinicas[index1:index2])
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
            + "'Financiadora'," \
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
            + "" +";" \
            + "" +";" \
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + objeto + "'," \
            + "'" + fecha + "'," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + objeto +";" \
            + fecha +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Plantas Piloto Asociadas')
    contguias_clinicas = [COD_PRODUCTO]

def prototiposextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contprototipos
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
        buscaprototipos = containers[a].td
        #print(buscaprototipos)
        try:
            if buscaprototipos.text == "Prototipos":
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
            info_prototipos = cont.text
            index1 = info_prototipos.find("- ") + 2
            index2 = info_prototipos.find(':')
            tipo = clc(info_prototipos[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Servicios":
                tipo = "92"
            elif tipo.strip() == "Industrial":
                tipo = "94"
            else:
                logging.critical('Añadir: ' + tipo + ' a prototipos')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_prototipos.find('\n                ', index1, len(info_prototipos))
            nombreart = clc(info_prototipos[index1:index2])
            index1 = index2 + 17
            index2 = info_prototipos.find(',', index1, len(info_prototipos))
            lugar = clc(info_prototipos[index1:index2])
            index1 = index2 + 2
            index2 = info_prototipos.find(',', index1, len(info_prototipos))
            anopub = clc(info_prototipos[index1:index2])
            index1 = info_prototipos.find('Disponibilidad:') + 15
            index2 = info_prototipos.find(',', index1, len(info_prototipos))
            disponibilidad = clc(info_prototipos[index1:index2])
            index1 = info_prototipos.find('Institución financiadora:') + 25
            index2 = info_prototipos.find('Autores:', index1, len(info_prototipos))
            institucion = clc(info_prototipos[index1:index2])
            index1 = info_prototipos.find('Autores:', index2, len(info_prototipos)) + 9
            index2 = info_prototipos.find('/br', index1, len(info_prototipos))
            autores = clc(info_prototipos[index1:index2])
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
            + "'" + institucion + "'," \
            + "'Financiadora'," \
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
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + disponibilidad + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + disponibilidad +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contprototipos = [COD_PRODUCTO]

def reglamentos_tecnicosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contreglamentos_tecnicos
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
        buscareglamentos_tecnicos = containers[a].td
        #print(buscareglamentos_tecnicos)
        try:
            if buscareglamentos_tecnicos.text == "Reglamentos técnicos":
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
            info_reglamentos_tecnicos = cont.text
            index1 = info_reglamentos_tecnicos.find("- ") + 2
            index2 = info_reglamentos_tecnicos.find(':')
            tipo = clc(info_reglamentos_tecnicos[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Reglamento Técnico":
                tipo = "67"
            else:
                logging.critical('Añadir: ' + tipo + ' a reglamentos_tecnicos')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_reglamentos_tecnicos.find('\n                ', index1, len(info_reglamentos_tecnicos))
            nombreart = clc(info_reglamentos_tecnicos[index1:index2])
            index1 = index2 + 17
            index2 = info_reglamentos_tecnicos.find(',', index1, len(info_reglamentos_tecnicos))
            lugar = clc(info_reglamentos_tecnicos[index1:index2])
            index1 = index2 + 2
            index2 = info_reglamentos_tecnicos.find(',', index1, len(info_reglamentos_tecnicos))
            anopub = clc(info_reglamentos_tecnicos[index1:index2])
            index1 = info_reglamentos_tecnicos.find('Ambito:') + 7
            index2 = info_reglamentos_tecnicos.find(',', index1, len(info_reglamentos_tecnicos))
            ambito = clc(info_reglamentos_tecnicos[index1:index2])
            index1 = info_reglamentos_tecnicos.find('Sitio web:') + 10
            index2 = info_reglamentos_tecnicos.find('Institución financiadora:', index1, len(info_reglamentos_tecnicos))
            DOI = clc(info_reglamentos_tecnicos[index1:index2])
            index1 = info_reglamentos_tecnicos.find('Disponibilidad:') + 15
            index2 = info_reglamentos_tecnicos.find(',', index1, len(info_reglamentos_tecnicos))
            disponibilidad = clc(info_reglamentos_tecnicos[index1:index2])
            index1 = info_reglamentos_tecnicos.find('Objeto:') + 7
            index2 = info_reglamentos_tecnicos.find('Institución financiadora:', index1, len(info_reglamentos_tecnicos))
            objeto = clc(info_reglamentos_tecnicos[index1:index2])
            index1 = info_reglamentos_tecnicos.find('Fecha de publicación:') + 21
            index2 = info_reglamentos_tecnicos.find(',', index1, len(info_reglamentos_tecnicos))
            fecha = clc(info_reglamentos_tecnicos[index1:index2])
            index1 = info_reglamentos_tecnicos.find('Institución financiadora:') + 25
            index2 = info_reglamentos_tecnicos.find('Autores:', index1, len(info_reglamentos_tecnicos))
            institucion = clc(info_reglamentos_tecnicos[index1:index2])
            index1 = info_reglamentos_tecnicos.find('Autores:', index2, len(info_reglamentos_tecnicos)) + 9
            index2 = info_reglamentos_tecnicos.find('/br', index1, len(info_reglamentos_tecnicos))
            autores = clc(info_reglamentos_tecnicos[index1:index2])
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
            + "'" + institucion + "'," \
            + "'Financiadora'," \
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
            + "" +";" \
            + DOI +";" \
            + "" +";" \
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + disponibilidad + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + disponibilidad +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contreglamentos_tecnicos = [COD_PRODUCTO]

def signos_distintivosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contsignos_distintivos
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
        buscasignos_distintivos = containers[a].td
        #print(buscasignos_distintivos)
        try:
            if buscasignos_distintivos.text == "Signos distintivos ":
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
            info_signos_distintivos = cont.text
            index1 = info_signos_distintivos.find("- ") + 2
            index2 = info_signos_distintivos.find(':')
            tipo = clc(info_signos_distintivos[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Signos distintivos":
                tipo = "71"
            elif tipo.strip() == "Marcas":
                tipo = "95"
            elif tipo.strip() == "Nombres comerciales":
                tipo = "96"
            else:
                logging.critical('Añadir: ' + tipo + ' a signos_distintivos')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_signos_distintivos.find('\n                ', index1, len(info_signos_distintivos))
            nombreart = clc(info_signos_distintivos[index1:index2])
            index1 = index2 + 17
            index2 = info_signos_distintivos.find(',', index1, len(info_signos_distintivos))
            lugar = clc(info_signos_distintivos[index1:index2])
            index1 = index2 + 2
            index2 = info_signos_distintivos.find(',', index1, len(info_signos_distintivos))
            anopub = clc(info_signos_distintivos[index1:index2])
            index1 = info_signos_distintivos.find('Ambito:') + 7
            index2 = info_signos_distintivos.find(',', index1, len(info_signos_distintivos))
            ambito = clc(info_signos_distintivos[index1:index2])
            index1 = info_signos_distintivos.find('Sitio web:') + 10
            index2 = info_signos_distintivos.find('Institución financiadora:', index1, len(info_signos_distintivos))
            DOI = clc(info_signos_distintivos[index1:index2])
            index1 = info_signos_distintivos.find('Disponibilidad:') + 15
            index2 = info_signos_distintivos.find(',', index1, len(info_signos_distintivos))
            disponibilidad = clc(info_signos_distintivos[index1:index2])
            index1 = info_signos_distintivos.find('Objeto:') + 7
            index2 = info_signos_distintivos.find('Institución financiadora:', index1, len(info_signos_distintivos))
            objeto = clc(info_signos_distintivos[index1:index2])
            index1 = info_signos_distintivos.find('Fecha de publicación:') + 21
            index2 = info_signos_distintivos.find(',', index1, len(info_signos_distintivos))
            fecha = clc(info_signos_distintivos[index1:index2])
            index1 = info_signos_distintivos.find('Institución financiadora:') + 25
            index2 = info_signos_distintivos.find('Autores:', index1, len(info_signos_distintivos))
            institucion = clc(info_signos_distintivos[index1:index2])
            index1 = info_signos_distintivos.find('Número del registro:') + 20
            index2 = info_signos_distintivos.find(',', index1, len(info_signos_distintivos))
            contrato = clc(info_signos_distintivos[index1:index2])
            index1 = info_signos_distintivos.find('Nombre del titular:') + 19
            index2 = info_signos_distintivos.find('\n', index1, len(info_signos_distintivos))
            autores = clc(info_signos_distintivos[index1:index2])
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
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + contrato + "'," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
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
            + contrato +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contsignos_distintivos = [COD_PRODUCTO]

def empresas_base_tecextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contempresas_base_tec
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
        buscaempresas_base_tec = containers[a].td
        #print(buscaempresas_base_tec)
        try:
            if buscaempresas_base_tec.text == "Empresas de base tecnológica ":
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
            info_empresas_base_tec = cont.text
            index1 = info_empresas_base_tec.find("- ") + 2
            index2 = info_empresas_base_tec.find(':')
            tipo = clc(info_empresas_base_tec[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Spin-off":
               tipo = "68"
            elif tipo.strip() == "Start-up":
               tipo = "69"
            else:
                logging.critical('Añadir: ' + tipo + ' a empresas_base_tec')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_empresas_base_tec.find('\n                ', index1, len(info_empresas_base_tec))
            nombreart = clc(info_empresas_base_tec[index1:index2])
            index1 = index2 + 17
            index2 = info_empresas_base_tec.find(',', index1, len(info_empresas_base_tec))
            fecha_publica = clc(info_empresas_base_tec[index1:index2])
            index1 = index2 - 5
            index2 = info_empresas_base_tec.find(',', index1, len(info_empresas_base_tec))
            anopub = clc(info_empresas_base_tec[index1:index2])
            index1 = info_empresas_base_tec.find('Ambito:') + 7
            index2 = info_empresas_base_tec.find(',', index1, len(info_empresas_base_tec))
            ambito = clc(info_empresas_base_tec[index1:index2])
            index1 = info_empresas_base_tec.find('NIT:') + 4
            index2 = info_empresas_base_tec.find(',', index1, len(info_empresas_base_tec))
            nit = clc(info_empresas_base_tec[index1:index2])
            index1 = info_empresas_base_tec.find('Fecha de registro ante cámara:') + 30
            index2 = info_empresas_base_tec.find('\n', index1, len(info_empresas_base_tec))
            registrocamara = clc(info_empresas_base_tec[index1:index2])
            index1 = index2 +2
            index2 = info_empresas_base_tec.find('\n', index1, len(info_empresas_base_tec))
            productos = clc(info_empresas_base_tec[index1:index2])
            index1 = info_empresas_base_tec.find('Sitio web:') + 10
            index2 = info_empresas_base_tec.find('Institución financiadora:', index1, len(info_empresas_base_tec))
            DOI = clc(info_empresas_base_tec[index1:index2])
            index1 = info_empresas_base_tec.find('Disponibilidad:') + 15
            index2 = info_empresas_base_tec.find(',', index1, len(info_empresas_base_tec))
            disponibilidad = clc(info_empresas_base_tec[index1:index2])
            index1 = info_empresas_base_tec.find('Objeto:') + 7
            index2 = info_empresas_base_tec.find('Institución financiadora:', index1, len(info_empresas_base_tec))
            objeto = clc(info_empresas_base_tec[index1:index2])
            index1 = info_empresas_base_tec.find('Institución financiadora:') + 25
            index2 = info_empresas_base_tec.find('Autores:', index1, len(info_empresas_base_tec))
            institucion = clc(info_empresas_base_tec[index1:index2])
            index1 = info_empresas_base_tec.find('Número del registro:') + 20
            index2 = info_empresas_base_tec.find(',', index1, len(info_empresas_base_tec))
            contrato = clc(info_empresas_base_tec[index1:index2])
            index1 = info_empresas_base_tec.find('Nombre del titular:') + 19
            index2 = info_empresas_base_tec.find('\n', index1, len(info_empresas_base_tec))
            titular = clc(info_empresas_base_tec[index1:index2])
            index1 = info_empresas_base_tec.find('Nombre del proyecto:') + 20
            index2 = info_empresas_base_tec.find('Institución financiadora:', index1, len(info_empresas_base_tec))
            proyecto = clc(info_empresas_base_tec[index1:index2])
            index1 = info_empresas_base_tec.find('Nombre comercial:') + 17
            index2 = info_empresas_base_tec.find('Nombre del proyecto:', index1, len(info_empresas_base_tec))
            comercial = clc(info_empresas_base_tec[index1:index2])
            index1 = info_empresas_base_tec.find('Sitio web:') + 10
            index2 = info_empresas_base_tec.find('Nombre comercial:', index1, len(info_empresas_base_tec))
            DOI = clc(info_empresas_base_tec[index1:index2])
            index1 = info_empresas_base_tec.find('Autores:') + 9
            index2 = info_empresas_base_tec.find('/n', index1, len(info_empresas_base_tec))
            autores = clc(info_empresas_base_tec[index1:index2])
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
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + nit + "'," \
            + "'" + registrocamara + "'," \
            + "'" + productos + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + nit +";" \
            + registrocamara +";" \
            + productos +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contempresas_base_tec = [COD_PRODUCTO]

def software_registradoextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contsoftware_registrado
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
        buscasoftware_registrado = containers[a].td
        #print(buscasoftware_registrado)
        try:
            if buscasoftware_registrado.text == "Softwares ":
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
            info_software_registrado = cont.text
            index1 = info_software_registrado.find("- ") + 2
            index2 = info_software_registrado.find(':')
            tipo = clc(info_software_registrado[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Computacional":
                tipo = "35"
            elif tipo.strip() == "Multimedia":
                tipo = "72"
            elif tipo.strip() == "Otra":
                tipo = "73"
            else:
                logging.critical('Añadir: ' + tipo + ' a software_registrado')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_software_registrado.find('\n                ', index1, len(info_software_registrado))
            nombreart = clc(info_software_registrado[index1:index2])
            index1 = index2 + 17
            index2 = info_software_registrado.find(',', index1, len(info_software_registrado))
            lugar = clc(info_software_registrado[index1:index2])
            index1 = index2 + 2
            index2 = info_software_registrado.find(',', index1, len(info_software_registrado))
            anopub = clc(info_software_registrado[index1:index2])
            index1 = info_software_registrado.find('Ambito:') + 7
            index2 = info_software_registrado.find(',', index1, len(info_software_registrado))
            ambito = clc(info_software_registrado[index1:index2])
            index1 = info_software_registrado.find('Sitio web:') + 10
            index2 = info_software_registrado.find('Institución financiadora:', index1, len(info_software_registrado))
            DOI = clc(info_software_registrado[index1:index2])
            index1 = info_software_registrado.find('Disponibilidad:') + 15
            index2 = info_software_registrado.find(',', index1, len(info_software_registrado))
            disponibilidad = clc(info_software_registrado[index1:index2])
            index1 = info_software_registrado.find('Objeto:') + 7
            index2 = info_software_registrado.find('Institución financiadora:', index1, len(info_software_registrado))
            objeto = clc(info_software_registrado[index1:index2])
            index1 = info_software_registrado.find('Fecha de publicación:') + 21
            index2 = info_software_registrado.find(',', index1, len(info_software_registrado))
            fecha = clc(info_software_registrado[index1:index2])
            index1 = info_software_registrado.find('Institución financiadora:') + 25
            index2 = info_software_registrado.find('Autores:', index1, len(info_software_registrado))
            institucion = clc(info_software_registrado[index1:index2])
            index1 = info_software_registrado.find('Número del registro:') + 20
            index2 = info_software_registrado.find(',', index1, len(info_software_registrado))
            contrato = clc(info_software_registrado[index1:index2])
            index1 = info_software_registrado.find('Nombre del titular:') + 19
            index2 = info_software_registrado.find('\n', index1, len(info_software_registrado))
            titular = clc(info_software_registrado[index1:index2])
            index1 = info_software_registrado.find('Nombre del proyecto:') + 20
            index2 = info_software_registrado.find('Institución financiadora:', index1, len(info_software_registrado))
            proyecto = clc(info_software_registrado[index1:index2])
            index1 = info_software_registrado.find('Nombre comercial:') + 17
            index2 = info_software_registrado.find('Nombre del proyecto:', index1, len(info_software_registrado))
            comercial = clc(info_software_registrado[index1:index2])
            index1 = info_software_registrado.find('Sitio web:') + 10
            index2 = info_software_registrado.find('Nombre comercial:', index1, len(info_software_registrado))
            DOI = clc(info_software_registrado[index1:index2])
            index1 = info_software_registrado.find('Autores:', index2, len(info_software_registrado)) + 9
            index2 = info_software_registrado.find('/br', index1, len(info_software_registrado))
            autores = clc(info_software_registrado[index1:index2])
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
            + "'" + institucion + "'," \
            + "'Financiadora'," \
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
            + "" +";" \
            + DOI +";" \
            + "" +";" \
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "'" + comercial + "'," \
            + "'" + proyecto + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + disponibilidad + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + comercial +";" \
            + proyecto +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + disponibilidad +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contsoftware_registrado = [COD_PRODUCTO]

def proyectos_leyextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contproyectos_ley
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
        buscaproyectos_ley = containers[a].td
        #print(buscaproyectos_ley)
        try:
            if buscaproyectos_ley.text == "Proyectos de ley":
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
            info_proyectos_ley = cont.text
            index1 = info_proyectos_ley.find("- ") + 2
            index2 = info_proyectos_ley.find(':')
            tipo = clc(info_proyectos_ley[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Ambiental o de Salud":
                tipo = "61"
            elif tipo.strip() == "Educativa":
                tipo = "62"
            elif tipo.strip() == "Social":
                tipo = "63"
            elif tipo.strip() == "Técnica":
                tipo = "64"
            elif tipo.strip() == "Guía de práctica clínica":
                tipo = "65"
            elif tipo.strip() == "Proyecto de ley":
                tipo = "66"
            elif tipo.strip() == "Técnica - Básica":
                tipo = "74"
            elif tipo.strip() == "Técnica - Ensayo":
                tipo = "75"
            elif tipo.strip() == "Técnica - Proceso":
                tipo = "77"
            else:
                logging.critical('Añadir: ' + tipo + ' a proyectos_ley')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_proyectos_ley.find('\n                ', index1, len(info_proyectos_ley))
            nombreart = clc(info_proyectos_ley[index1:index2])
            index1 = index2 + 17
            index2 = info_proyectos_ley.find(',', index1, len(info_proyectos_ley))
            lugar = clc(info_proyectos_ley[index1:index2])
            index1 = index2 + 2
            index2 = info_proyectos_ley.find(',', index1, len(info_proyectos_ley))
            anopub = clc(info_proyectos_ley[index1:index2])
            index1 = info_proyectos_ley.find('Ambito:') + 7
            index2 = info_proyectos_ley.find(',', index1, len(info_proyectos_ley))
            ambito = clc(info_proyectos_ley[index1:index2])
            index1 = info_proyectos_ley.find('Sitio web:') + 10
            index2 = info_proyectos_ley.find('Institución financiadora:', index1, len(info_proyectos_ley))
            DOI = clc(info_proyectos_ley[index1:index2])
            index1 = info_proyectos_ley.find('Disponibilidad:') + 15
            index2 = info_proyectos_ley.find(',', index1, len(info_proyectos_ley))
            disponibilidad = clc(info_proyectos_ley[index1:index2])
            index1 = info_proyectos_ley.find('Objeto:') + 7
            index2 = info_proyectos_ley.find('Institución financiadora:', index1, len(info_proyectos_ley))
            objeto = clc(info_proyectos_ley[index1:index2])
            index1 = info_proyectos_ley.find('Fecha de publicación:') + 21
            index2 = info_proyectos_ley.find(',', index1, len(info_proyectos_ley))
            fecha = clc(info_proyectos_ley[index1:index2])
            index1 = info_proyectos_ley.find('Institución financiadora:') + 25
            index2 = info_proyectos_ley.find('Autores:', index1, len(info_proyectos_ley))
            institucion = clc(info_proyectos_ley[index1:index2])
            index1 = info_proyectos_ley.find('Número del registro:') + 20
            index2 = info_proyectos_ley.find(',', index1, len(info_proyectos_ley))
            contrato = clc(info_proyectos_ley[index1:index2])
            index1 = info_proyectos_ley.find('Nombre del titular:') + 19
            index2 = info_proyectos_ley.find('\n', index1, len(info_proyectos_ley))
            titular = clc(info_proyectos_ley[index1:index2])
            index1 = info_proyectos_ley.find('Nombre del proyecto:') + 20
            index2 = info_proyectos_ley.find('Institución financiadora:', index1, len(info_proyectos_ley))
            proyecto = clc(info_proyectos_ley[index1:index2])
            index1 = info_proyectos_ley.find('Nombre comercial:') + 17
            index2 = info_proyectos_ley.find('Nombre del proyecto:', index1, len(info_proyectos_ley))
            comercial = clc(info_proyectos_ley[index1:index2])
            index1 = info_proyectos_ley.find('Sitio web:') + 10
            index2 = info_proyectos_ley.find('Nombre comercial:', index1, len(info_proyectos_ley))
            DOI = clc(info_proyectos_ley[index1:index2])
            index1 = info_proyectos_ley.find('Autores:') + 9
            index2 = info_proyectos_ley.find('/n', index1, len(info_proyectos_ley))
            autores = clc(info_proyectos_ley[index1:index2])
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
            + "'" + institucion + "'," \
            + "'Financiadora'," \
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
            + institucion +";" \
            + "Financiadora" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_TEC.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD_TEC`,`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + "T" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + objeto + "'," \
            + "'" + fecha + "'," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + "T" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + objeto + ";" \
            + fecha + ";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contproyectos_ley = [COD_PRODUCTO]

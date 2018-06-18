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
                logging.critical('Añadir: ' + tipo)
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
            + str(codcolciencias) + "," \
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
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
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
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
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
                logging.critical('Añadir: ' + tipo)
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
            + str(codcolciencias) + "," \
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
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
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
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
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
            else:
                logging.critical('Añadir: ' + tipo)
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
            + str(codcolciencias) + "," \
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
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
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
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
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
                logging.critical('Añadir: ' + tipo)
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
            + str(codcolciencias) + "," \
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
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
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
            init.GP_PROD_TEC_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
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

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

def articulosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contarticulo
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
        buscaarticulos = containers[a].td
        #print(buscaarticulos)
        try:
            if buscaarticulos.text == "Artículos publicados":
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
            info_articulo = cont.text
            index1 = info_articulo.find("- ") + 2
            index2 = info_articulo.find(':')
            tipo = clc(info_articulo[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Publicado en revista especializada":
                tipo = "8"
            elif tipo.strip() == "Corto Resumen":
                tipo = "9"
            elif tipo.strip() == "Revisión Survey":
                tipo = "10"
            elif tipo.strip() == "Caso clínico":
                tipo = "11"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Artículos.log")
            index1 = index2 + 2
            index2 = info_articulo.find('\n', index1, len(info_articulo))
            nombreart = clc(info_articulo[index1:index2])
            index1 = index2 + 2
            index2 = info_articulo.find(',', index1, len(info_articulo))
            lugar = clc(info_articulo[index1:index2])
            index1 = index2 + 2
            index2 = info_articulo.find('ISSN:', index1, len(info_articulo))
            revista = clc(info_articulo[index1:index2])
            index1 = index2 + 6
            index2 = info_articulo.find(',', index1, len(info_articulo))
            ISSN = clc(info_articulo[index1:index2])
            index1 = index2 + 2
            index2 = info_articulo.find('vol:', index1, len(info_articulo))
            anopub = clc(info_articulo[index1:index2])
            index1 = index2 + 4
            index2 = info_articulo.find('fasc:', index1, len(info_articulo))
            vol = clc(info_articulo[index1:index2])
            index1 = index2 + 6
            index2 = info_articulo.find('págs:', index1, len(info_articulo))
            fasc = clc(info_articulo[index1:index2])
            index1 = index2 + 6
            index2 = info_articulo.find(', DOI:', index1, len(info_articulo))
            pags = clc(info_articulo[index1:index2])
            index = pags.find("-")
            pagsini = clc(pags[0:index])
            pagsfin = clc(pags[index + 2:len(pags)])
            index1 = index2 + 6
            index2 = info_articulo.find('Autores:', index1, len(info_articulo))
            DOI = clc(info_articulo[index1:index2])
            index1 = index2 + 9
            index2 = info_articulo.find('/br', index1, len(info_articulo))
            autores = clc(info_articulo[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "'" + lugar + "'," \
            + anopub + "," \
            + "null" + "," \
            + "'" + pags + "'," \
            + "'" + vol + "'," \
            + "null" + "," \
            + "null" + "," \
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
            + pags +";" \
            + vol +";" \
            + "" +";" \
            + "" +";" \
            + DOI +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_BIB.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_BIB`(`CODGP_PROD_BIB`,`CODGP_PROD`,`Revista`,`Autor_Original`,`Nombre_Libro`,`ISBN/ISSN`,`Medio_de_Divulgación`,`URL`,`Fasciculos`,`Idioma_Original`,`Idioma_Traduccion`,`Edición`,`Serie`,`Página_Inicial`,`Página_Final`) VALUES"
            + "('" + str(codcolciencias) + "B" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + revista + "'," \
            + "null" + "," \
            + "null" + "," \
            + "'" + ISSN + "'," \
            + "null" + "," \
            + "null" + "," \
            + "'" + fasc + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + pagsini + "," \
            + pagsfin \
            + ");\n")
            init.GP_PROD_BIB_CSV.append(str(codcolciencias) + "B" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + revista +";" \
            + "" +";" \
            + "" +";" \
            + ISSN +";" \
            + "" +";" \
            + "" +";" \
            + fasc +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + pagsini +";" \
            + pagsfin +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Artículos Asociados')
    contarticulo = [COD_PRODUCTO]

def librosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contlibros
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
        buscaarticulos = containers[a].td
        #print(buscaarticulos)
        try:
            if buscaarticulos.text == " Libros publicados ":
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
            info_libros = cont.text
            index1 = info_libros.find("- ") + 2
            index2 = info_libros.find(':')
            tipo = clc(info_libros[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Libro resultado de investigación":
                tipo = "17"
            elif tipo.strip() == "Otro libro publicado":
                tipo = "18"
            elif tipo.strip() == "Libro pedagógico y/o de divulgación":
                tipo = "19"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Libros.log")
            index1 = index2 + 2
            index2 = info_libros.find('\n', index1, len(info_libros))
            nombreart = clc(info_libros[index1:index2])
            index1 = index2 + 2
            index2 = info_libros.find(',', index1, len(info_libros))
            lugar = clc(info_libros[index1:index2])
            index1 = index2 + 1
            index2 = info_libros.find(', ISBN', index1, len(info_libros))
            anopub = clc(info_libros[index1:index2])
            index1 = index2 + 8
            index2 = info_libros.find('vol:', index1, len(info_libros))
            ISSN = clc(info_libros[index1:index2])
            index1 = index2 + 4
            index2 = info_libros.find('págs:', index1, len(info_libros))
            vol = clc(info_libros[index1:index2])
            index1 = index2 + 5
            index2 = info_libros.find(', Ed.', index1, len(info_libros))
            pags = clc(info_libros[index1:index2])
            index1 = index2 + 5
            index2 = info_libros.find('Autores:', index1, len(info_libros))
            editorial = clc(info_libros[index1:index2])
            index1 = index2 + 9
            index2 = info_libros.find('/br', index1, len(info_libros))
            autores = clc(info_libros[index1:index2])
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
            + "'" + vol + "'," \
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
            + "" +";" \
            + "" +";" \
            + vol +";" \
            + editorial +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_BIB.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_BIB`(`CODGP_PROD_BIB`,`CODGP_PROD`,`Revista`,`Autor_Original`,`Nombre_Libro`,`ISBN/ISSN`,`Medio_de_Divulgación`,`URL`,`Fasciculos`,`Idioma_Original`,`Idioma_Traduccion`,`Edición`,`Serie`,`Página_Inicial`,`Página_Final`) VALUES"
            + "('" + str(codcolciencias) + "B" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + ISSN + "'," \
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
            init.GP_PROD_BIB_CSV.append(str(codcolciencias) + "B" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + ISSN +";" \
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
        logging.info(' El Grupo: ' + nombregi + 'no tiene libros Asociados')
    contlibros = [COD_PRODUCTO]

def caplibrosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contcaplibros
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
        buscaarticulos = containers[a].td
        #print(buscaarticulos)
        try:
            if buscaarticulos.text == "Capítulos de libro publicados ":
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
            info_caplibros = cont.text
            index1 = info_caplibros.find("- ") + 2
            index2 = info_caplibros.find(':')
            tipo = clc(info_caplibros[index1:index2])
            #Tipo Artículo
            if tipo == "Capítulo de libro":
                tipo = "21"
            elif tipo == "Otro capítulo de libro publicado":
                tipo = "20"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Capítulos Libros.log")
            index1 = index2 + 2
            index2 = info_caplibros.find('\n', index1, len(info_caplibros))
            nombreart = clc(info_caplibros[index1:index2])
            index1 = index2 + 2
            index2 = info_caplibros.find(',', index1, len(info_caplibros))
            lugar = clc(info_caplibros[index1:index2])
            index1 = index2 + 1
            index2 = info_caplibros.find(',', index1, len(info_caplibros))
            anopub = clc(info_caplibros[index1:index2])
            index1 = index2 + 1
            index2 = info_caplibros.find(', ISBN', index1, len(info_caplibros))
            libroorigen = clc(info_caplibros[index1:index2])
            index1 = index2 + 7
            index2 = info_caplibros.find(', Vol.', index1, len(info_caplibros))
            ISSN = clc(info_caplibros[index1:index2])
            index1 = index2 + 6
            index2 = info_caplibros.find('págs:', index1, len(info_caplibros))
            vol = clc(info_caplibros[index1:index2])
            index1 = index2 + 5
            index2 = info_caplibros.find(', Ed.', index1, len(info_caplibros))
            pags = clc(info_caplibros[index1:index2])
            index = pags.find("-")
            pagsini = clc(pags[0:index])
            pagsfin = clc(pags[index + 2:len(pags)])
            index1 = index2 + 5
            index2 = info_caplibros.find('Autores:', index1, len(info_caplibros))
            editorial = clc(info_caplibros[index1:index2])
            index1 = index2 + 9
            index2 = info_caplibros.find('/br', index1, len(info_caplibros))
            autores = clc(info_caplibros[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "'" + lugar + "'," \
            + anopub + "," \
            + "null" + "," \
            + "'" + pags + "'," \
            + "'" + vol + "'," \
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
            + "" +";" \
            + pags +";" \
            + vol +";" \
            + editorial +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_BIB.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_BIB`(`CODGP_PROD_BIB`,`CODGP_PROD`,`Revista`,`Autor_Original`,`Nombre_Libro`,`ISBN/ISSN`,`Medio_de_Divulgación`,`URL`,`Fasciculos`,`Idioma_Original`,`Idioma_Traduccion`,`Edición`,`Serie`,`Página_Inicial`,`Página_Final`) VALUES"
            + "('" + str(codcolciencias) + "B" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "'" + libroorigen + "'," \
            + "'" + ISSN + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + pagsini + "," \
            + pagsfin \
            + ");\n")
            init.GP_PROD_BIB_CSV.append(str(codcolciencias) + "B" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + libroorigen +";" \
            + ISSN +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + pagsini +";" \
            + pagsfin +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene caplibros Asociados')
    contcaplibros = [COD_PRODUCTO]

def doctraextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contdoctra
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
        buscaarticulos = containers[a].td
        #print(buscaarticulos)
        try:
            if buscaarticulos.text == "Documentos de trabajo ":
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
            info_doctra = cont.text
            index1 = info_doctra.find("- ") + 2
            index2 = info_doctra.find(':')
            tipo = clc(info_doctra[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Documento de trabajo Working Paper":
                tipo = "27"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Documentos.log")
            index1 = index2 + 2
            index2 = info_doctra.find('\n', index1, len(info_doctra))
            nombreart = clc(info_doctra[index1:index2])
            index1 = index2 + 2
            index2 = info_doctra.find('Nro. Paginas:', index1, len(info_doctra))
            anopub = clc(info_doctra[index1:index2])
            index1 = index2 + 13
            index2 = info_doctra.find('Instituciones participantes:', index1, len(info_doctra)) - 19
            nro = clc(info_doctra[index1:index2])
            index1 = index2 + 47
            index2 = info_doctra.find('URL: ', index1, len(info_doctra)) - 18
            instituciones = clc(info_doctra[index1:index2])
            index1 = index2 + 23
            index2 = info_doctra.find('DOI:', index1, len(info_doctra)) -18
            URL = clc(info_doctra[index1:index2])
            index1 = index2 + 22
            index2 = info_doctra.find('Autores:', index1, len(info_doctra))
            DOI = clc(info_doctra[index1:index2])
            index1 = index2 + 9
            index2 = info_doctra.find('/br', index1, len(info_doctra))
            autores = clc(info_doctra[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "null" + "," \
            + anopub + "," \
            + "null" + "," \
            + "'" + nro + "'," \
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
            + nro +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + DOI +";" \
            + "" +";" \
            + instituciones +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_BIB.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_BIB`(`CODGP_PROD_BIB`,`CODGP_PROD`,`Revista`,`Autor_Original`,`Nombre_Libro`,`ISBN/ISSN`,`Medio_de_Divulgación`,`URL`,`Fasciculos`,`Idioma_Original`,`Idioma_Traduccion`,`Edición`,`Serie`,`Página_Inicial`,`Página_Final`) VALUES"
            + "('" + str(codcolciencias) + "B" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + URL + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_BIB_CSV.append(str(codcolciencias) + "B" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + URL +";" \
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
        logging.info(' El Grupo: ' + nombregi + 'no tiene doctra Asociados')
    contdoctra = [COD_PRODUCTO]

def otrapubdivextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contotrapubdiv
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
        buscaotrapubdiv = containers[a].td
        #print(buscaotrapubdiv)
        try:
            if buscaotrapubdiv.text == "Otra publicación divulgativa":
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
            info_otrapubdiv = cont.text
            index1 = info_otrapubdiv.find("- ") + 2
            index2 = info_otrapubdiv.find(':')
            tipo = clc(info_otrapubdiv[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Introducción":
                tipo = "31"
            elif tipo.strip() == "Prólogo":
                tipo = "32"
            elif tipo.strip() == "Epílogo":
                tipo = "33"
            elif tipo.strip() == "Otra":
                tipo = "34"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Eventos.log")
            index1 = index2 + 2
            index2 = info_otrapubdiv.find('\n', index1, len(info_otrapubdiv))
            nombreart = clc(info_otrapubdiv[index1:index2])
            index1 = index2 + 2
            index2 = info_otrapubdiv.find(',', index1, len(info_otrapubdiv))
            lugar = clc(info_otrapubdiv[index1:index2])
            index1 = index2 + 1
            index2 = info_otrapubdiv.find(',', index1, len(info_otrapubdiv))
            anopub = clc(info_otrapubdiv[index1:index2])
            index1 = info_otrapubdiv.find('vol. ') + 4
            index2 = info_otrapubdiv.find(',', index1, len(info_otrapubdiv))
            vol = clc(info_otrapubdiv[index1:index2])
            index1 = info_otrapubdiv.find('págs:') + 5
            index2 = info_otrapubdiv.find(',', index1, len(info_otrapubdiv))
            pags = clc(info_otrapubdiv[index1:index2])
            index1 = info_otrapubdiv.find('-', index2, len(info_otrapubdiv)) + 2
            index2 = info_otrapubdiv.find(',', index1, len(info_otrapubdiv))
            autorori = clc(info_otrapubdiv[index1:index2])
            index1 = info_otrapubdiv.find('Ed.', index2, len(info_otrapubdiv)) + 3
            index2 = info_otrapubdiv.find('Autores:', index1, len(info_otrapubdiv))
            editorial = clc(info_otrapubdiv[index1:index2])
            index1 = info_otrapubdiv.find('Autores:', index2, len(info_otrapubdiv)) + 9
            index2 = info_otrapubdiv.find('/br', index1, len(info_otrapubdiv))
            autores = clc(info_otrapubdiv[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "'" + lugar + "'," \
            + anopub + "," \
            + "null" + "," \
            + "'" + pags + "'," \
            + "'" + vol + "'," \
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
            + "" +";" \
            + pags +";" \
            + vol +";" \
            + editorial +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_BIB.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_BIB`(`CODGP_PROD_BIB`,`CODGP_PROD`,`Revista`,`Autor_Original`,`Nombre_Libro`,`ISBN/ISSN`,`Medio_de_Divulgación`,`URL`,`Fasciculos`,`Idioma_Original`,`Idioma_Traduccion`,`Edición`,`Serie`,`Página_Inicial`,`Página_Final`) VALUES"
            + "('" + str(codcolciencias) + "B" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "'" + autorori + "'," \
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
            init.GP_PROD_BIB_CSV.append(str(codcolciencias) + "B" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + autorori +";" \
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
        logging.info(' El Grupo: ' + nombregi + 'no tiene otrapubdiv Asociados')
    contotrapubdiv = [COD_PRODUCTO]

def otrosarticulosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contotrosarticulos
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
        buscaotrosarticulos = containers[a].td
        #print(buscaotrosarticulos)
        try:
            if buscaotrosarticulos.text == "Otros artículos publicados":
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
            info_otrosarticulos = cont.text
            index1 = info_otrosarticulos.find("- ") + 2
            index2 = info_otrosarticulos.find(':')
            tipo = clc(info_otrosarticulos[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Periódico de noticias":
               tipo = "22"
            elif tipo.strip() == "Revista de divulgación":
               tipo = "23"
            elif tipo.strip() == "Carta al editor":
               tipo = "24"
            elif tipo.strip() == "Reseñas de libros":
               tipo = "25"
            elif tipo.strip() == "Columna de opinión":
               tipo = "26"
            else:
               logging.critical('Añadir: ' + tipo)
               print ("ALERTA: Revisar el archivo Textos No Cientificos.log")
            index1 = index2 + 2
            index2 = info_otrosarticulos.find('\n', index1, len(info_otrosarticulos))
            nombreart = clc(info_otrosarticulos[index1:index2])
            index1 = index2 + 2
            index2 = info_otrosarticulos.find(',', index1, len(info_otrosarticulos))
            lugar = clc(info_otrosarticulos[index1:index2])
            index1 = index2 + 1
            index2 = info_otrosarticulos.find('ISSN:', index1, len(info_otrosarticulos))
            revista = clc(info_otrosarticulos[index1:index2])
            index1 = index2 + 5
            index2 = info_otrosarticulos.find(',', index1, len(info_otrosarticulos))
            ISSN = clc(info_otrosarticulos[index1:index2])
            index1 = index2 + 2
            index2 = info_otrosarticulos.find('vol:', index1, len(info_otrosarticulos))
            anopub = clc(info_otrosarticulos[index1:index2])
            index1 = info_otrosarticulos.find('vol:') + 4
            index2 = info_otrosarticulos.find('fasc', index1, len(info_otrosarticulos))
            vol = clc(info_otrosarticulos[index1:index2])
            index1 = info_otrosarticulos.find('fasc:') + 5
            index2 = info_otrosarticulos.find('págs', index1, len(info_otrosarticulos))
            fasc = clc(info_otrosarticulos[index1:index2])
            index1 = info_otrosarticulos.find('págs:') + 5
            index2 = info_otrosarticulos.find('\n', index1, len(info_otrosarticulos))
            pags = clc(info_otrosarticulos[index1:index2])
            index = pags.find("-")
            pagsini = clc(pags[0:index])
            pagsfin = clc(pags[index + 2:len(pags)])
            index1 = info_otrosarticulos.find('Autores:', index2, len(info_otrosarticulos)) + 9
            index2 = info_otrosarticulos.find('/br', index1, len(info_otrosarticulos))
            autores = clc(info_otrosarticulos[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "'" + lugar + "'," \
            + anopub + "," \
            + "null" + "," \
            + "'" + pags + "'," \
            + "'" + vol + "'," \
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
            + pags +";" \
            + vol +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_BIB.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_BIB`(`CODGP_PROD_BIB`,`CODGP_PROD`,`Revista`,`Autor_Original`,`Nombre_Libro`,`ISBN/ISSN`,`Medio_de_Divulgación`,`URL`,`Fasciculos`,`Idioma_Original`,`Idioma_Traduccion`,`Edición`,`Serie`,`Página_Inicial`,`Página_Final`) VALUES"
            + "('" + str(codcolciencias) + "B" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + revista + "'," \
            + "null" + "," \
            + "null" + "," \
            + "'" + ISSN + "'," \
            + "null" + "," \
            + "null" + "," \
            + "'" + fasc + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + pagsini + "," \
            + pagsfin \
            + ");\n")
            init.GP_PROD_BIB_CSV.append(str(codcolciencias) + "B" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + revista +";" \
            + "" +";" \
            + "" +";" \
            + ISSN +";" \
            + "" +";" \
            + "" +";" \
            + fasc +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + pagsini +";" \
            + pagsfin +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene otrosarticulos Asociados')
    contotrosarticulos = [COD_PRODUCTO]

def otroslibrosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contotroslibros
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
        buscaotroslibros = containers[a].td
        #print(buscaotroslibros)
        try:
            if buscaotroslibros.text == " Otros Libros publicados ":
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
            info_otroslibros = cont.text
            index1 = info_otroslibros.find("- ") + 2
            index2 = info_otroslibros.find(':')
            tipo = clc(info_otroslibros[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Libro resultado de investigación":
                tipo = "17"
            elif tipo.strip() == "Otro libro publicado":
                tipo = "18"
            elif tipo.strip() == "Libro pedagógico y/o de divulgación":
                tipo = "19"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Libros.log")
            index1 = index2 + 2
            index2 = info_otroslibros.find('\n', index1, len(info_otroslibros))
            nombreart = clc(info_otroslibros[index1:index2])
            index1 = index2 + 2
            index2 = info_otroslibros.find(',', index1, len(info_otroslibros))
            lugar = clc(info_otroslibros[index1:index2])
            index1 = index2 + 1
            index2 = info_otroslibros.find(', ISBN: ', index1, len(info_otroslibros))
            anopub = clc(info_otroslibros[index1:index2])
            index1 = index2 + 8
            index2 = info_otroslibros.find(' vol:', index1, len(info_otroslibros))
            ISSN = clc(info_otroslibros[index1:index2])
            index1 = info_otroslibros.find('vol:') + 4
            index2 = info_otroslibros.find('págs:', index1, len(info_otroslibros))
            vol = clc(info_otroslibros[index1:index2])
            index1 = info_otroslibros.find('págs:') + 5
            index2 = info_otroslibros.find(', Ed.', index1, len(info_otroslibros))
            pags = clc(info_otroslibros[index1:index2])
            index1 = index2 + 5
            index2 = info_otroslibros.find('\n', index1, len(info_otroslibros))
            editorial = clc(info_otroslibros[index1:index2])
            index1 = info_otroslibros.find('Autores:', index2, len(info_otroslibros)) + 9
            index2 = info_otroslibros.find('/br', index1, len(info_otroslibros))
            autores = clc(info_otroslibros[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "'" + lugar + "'," \
            + anopub + "," \
            + "null" + "," \
            + "'" + pags + "'," \
            + "'" + vol + "'," \
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
            + "" +";" \
            + pags +";" \
            + vol +";" \
            + editorial +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_PROD_BIB.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_BIB`(`CODGP_PROD_BIB`,`CODGP_PROD`,`Revista`,`Autor_Original`,`Nombre_Libro`,`ISBN/ISSN`,`Medio_de_Divulgación`,`URL`,`Fasciculos`,`Idioma_Original`,`Idioma_Traduccion`,`Edición`,`Serie`,`Página_Inicial`,`Página_Final`) VALUES"
            + "('" + str(codcolciencias) + "B" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + ISSN + "'," \
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
            init.GP_PROD_BIB_CSV.append(str(codcolciencias) + "B" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + ISSN +";" \
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
        logging.info(' El Grupo: ' + nombregi + 'no tiene otroslibros Asociados')
    contotroslibros = [COD_PRODUCTO]

def traduccionesextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global conttraducciones
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
        buscatraducciones = containers[a].td
        #print(buscatraducciones)
        try:
            if buscatraducciones.text == "Traducciones ":
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
            info_traducciones = cont.text
            index1 = info_traducciones.find("- ") + 2
            index2 = info_traducciones.find(':')
            tipo = clc(info_traducciones[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Artículo":
                tipo = "28"
            elif tipo.strip() == "Libro":
                tipo = "29"
            elif tipo.strip() == "Otra":
                tipo = "30"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Eventos.log")
            index1 = index2 + 2
            index2 = info_traducciones.find('\n', index1, len(info_traducciones))
            nombreart = clc(info_traducciones[index1:index2])
            index1 = index2 + 2
            index2 = info_traducciones.find(', Revista:', index1, len(info_traducciones))
            anopub = clc(info_traducciones[index1:index2])
            index1 = index2 + 10
            index2 = info_traducciones.find('ISSN', index1, len(info_traducciones))
            revista = clc(info_traducciones[index1:index2])
            index1 = index2 + 4
            index2 = info_traducciones.find(',', index1, len(info_traducciones))
            ISSN = clc(info_traducciones[index1:index2])
            index1 = info_traducciones.find('Libro:') + 6
            index2 = info_traducciones.find('ISBN', index1, len(info_traducciones))
            libroorigen = clc(info_traducciones[index1:index2])
            index1 = index2 + 4
            index2 = info_traducciones.find(',', index1, len(info_traducciones))
            ISBN = clc(info_traducciones[index1:index2])
            index1 = info_traducciones.find(', Medio de divulgación:') + 23
            index2 = info_traducciones.find('\n', index1, len(info_traducciones))
            medio = clc(info_traducciones[index1:index2])
            index1 = info_traducciones.find('Idioma del documento original:') + 30
            index2 = info_traducciones.find(',', index1, len(info_traducciones))
            idiomaorigen = clc(info_traducciones[index1:index2])
            index1 = info_traducciones.find('Idioma de la traducción:') + 24
            index2 = info_traducciones.find('\n', index1, len(info_traducciones))
            idiomatraduccion = clc(info_traducciones[index1:index2])
            index1 = info_traducciones.find('Edición: ') + 9
            index2 = info_traducciones.find(',', index1, len(info_traducciones))
            edicion = clc(info_traducciones[index1:index2])
            index1 = info_traducciones.find('Serie: ') + 7
            index2 = info_traducciones.find(',', index1, len(info_traducciones))
            serie = clc(info_traducciones[index1:index2])
            index1 = info_traducciones.find('Autor del documento original:') + 29
            index2 = info_traducciones.find('\n', index1, len(info_traducciones))
            autorori = clc(info_traducciones[index1:index2])
            index1 = info_traducciones.find('Autores:', index2, len(info_traducciones)) + 9
            index2 = info_traducciones.find('/br', index1, len(info_traducciones))
            autores = clc(info_traducciones[index1:index2])
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
            init.GP_PROD_BIB.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_BIB`(`CODGP_PROD_BIB`,`CODGP_PROD`,`Revista`,`Autor_Original`,`Nombre_Libro`,`ISBN/ISSN`,`Medio_de_Divulgación`,`URL`,`Fasciculos`,`Idioma_Original`,`Idioma_Traduccion`,`Edición`,`Serie`,`Página_Inicial`,`Página_Final`) VALUES"
            + "('" + str(codcolciencias) + "B" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "'" + autorori + "'," \
            + "'" + libroorigen + "'," \
            + "'" + ISBN + "'," \
            + "'" + medio + "'," \
            + "null" + "," \
            + "null" + "," \
            + "'" + idiomaorigen + "'," \
            + "'" + idiomatraduccion + "'," \
            + "'" + edicion + "'," \
            + "'" + serie + "'," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_PROD_BIB_CSV.append(str(codcolciencias) + "B" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + autorori +";" \
            + libroorigen +";" \
            + ISBN +";" \
            + medio +";" \
            + "" +";" \
            + "" +";" \
            + idiomaorigen +";" \
            + idiomatraduccion +";" \
            + edicion +";" \
            + serie +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene traducciones Asociados')
    conttraducciones = [COD_PRODUCTO]

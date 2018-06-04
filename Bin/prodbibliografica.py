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
    str = re.sub(r'[^A-Za-z0-9:=_?ÁÀÉÈÍÌÓÒÚÙéèáà,éñèíìúñùóò .\-/+]',r'',re.sub(' +',' ',str.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
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
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo Vincula Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + str(codcolciencias) + "," \
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
            "REPLACE INTO `uapa_db`.`GP_PROD_BIB`(`CODGP_PROD`,`Revista`,`Autor Original`,`Nombre Libro`,`ISBN/ISSN`,`Medio de Divulgación`,`URL`,`Fasciculos`,`Idioma Original`,`Idioma Traduccion`,`Edición`,`Serie`,`Página Inicial`,`Página Final`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
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
            + pagsfin + "," \
            + ");\n")
            init.GP_PROD_BIB_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
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

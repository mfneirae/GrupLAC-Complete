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

def obras_productosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contobras_productos
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
        buscaobras_productos = containers[a].td
        #print(buscaobras_productos)
        try:
            if buscaobras_productos.text == "Producción en arte, arquitectura y diseño":
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
            info_obras_productos = cont.text
            tipo = "113"
            index1 = info_obras_productos.find('Nombre del Producto:') + 20
            index2 = info_obras_productos.find('\n', index1, len(info_obras_productos))
            nombreart = clc(info_obras_productos[index1:index2])
            index1 = info_obras_productos.find('Fecha de creación:',index1,len(info_obras_productos))
            if index1 == -1:
                creacion = "";
            else:
                index1 = index1 + 18
                index2 = info_obras_productos.find('\n', index1, len(info_obras_productos))
                creacion = clc(info_obras_productos[index1:index2])
            anopub = clc(creacion[len(creacion)-4:len(creacion)])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""
            index1 = info_obras_productos.find('Disciplina o ámbito de origen:',index1,len(info_obras_productos))
            if index1 == -1:
                disciplina = "";
            else:
                index1 = index1 + 30
                index2 = info_obras_productos.find('\n', index1, len(info_obras_productos))
                disciplina = clc(info_obras_productos[index1:index2])
            index1 = info_obras_productos.find('Institución u organizació que tiene la licencia:',index1,len(info_obras_productos)) + 48
            index2 = info_obras_productos.find(',', index1, len(info_obras_productos))
            instituciones = clc(info_obras_productos[index1:index2])
            index1 = info_obras_productos.find('Fecha de otorgamiento:')
            if index1 == -1:
                otorgamiento = "";
            else:
                index1 = index1 + 22
                index2 = info_obras_productos.find(', Número de registro de la Dirección  Nacional de Derechos de Autor:', index1, len(info_obras_productos))
                otorgamiento = clc(info_obras_productos[index1:index2])
            index1 = info_obras_productos.find('Número de registro de la Dirección  Nacional de Derechos de Autor:') + 66
            index2 = info_obras_productos.find('\n', index1, len(info_obras_productos))
            registro = clc(info_obras_productos[index1:index2])
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
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            init.GP_OBRAS.append( \
            "REPLACE INTO `uapa_db`.`GP_OBRAS`(`CODGP_PROD_OBRAS`,`CODGP_PROD`,`Fecha_Creación`,`Disiplina_de_origen`,`Institución_Licencia`,`Fecha_Licencia`,`Distinciones`,`Selección_Distinción`,`Productos_Asociados`,`Número_Derechos_Autor/NIT`) VALUES"
            + "('" + str(codcolciencias) + "O" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + creacion + "'," \
            + "'" + disciplina + "'," \
            + "'" + otorgamiento+ "'," \
            + "'" + registro + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_OBRAS_CSV.append(str(codcolciencias) + "O" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + creacion +";" \
            + disciplina +";" \
            + otorgamiento +";" \
            + registro +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contobras_productos = [COD_PRODUCTO]

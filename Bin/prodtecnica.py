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
            index1 = info_cartas.find("- ") + 2
            index2 = info_cartas.find(':')
            tipo = clc(info_cartas[index1:index2])
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
            init.GP_PROD_BIB.append( \
            "REPLACE INTO `uapa_db`.`GP_PROD_TEC`(`CODGP_PROD`,`Tema`,`Nombre_Comerial`,`Nombre_Proyecto`,`Tipo_de_Ciclo`,`NIT`,`Fecha_de_Registro`,`Tiene_Productos`,`Disponibilidad`,`Objeto`,`Fecha_Publicación`,`Número_de_Contrato`,`Acto_Administrativo`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
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
            init.GP_PROD_BIB_CSV.append(str(codcolciencias) + str(COD_PRODUCTO) +";" \
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
        logging.info(' El Grupo: ' + nombregi + 'no tiene cartas Asociados')
    contcartas = [COD_PRODUCTO]

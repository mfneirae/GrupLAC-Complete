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
            else:
                logging.critical('Añadir: ' + tipo + ' a ediciones_apropiacion')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_ediciones_apropiacion.find('\n                ', index1, len(info_ediciones_apropiacion))
            nombreart = clc(info_ediciones_apropiacion[index1:index2])
            index1 = index2 + 17
            index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
            lugar = clc(info_ediciones_apropiacion[index1:index2])
            index1 = index2 + 2
            index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
            anopub = clc(info_ediciones_apropiacion[index1:index2])
            index1 = info_ediciones_apropiacion.find('Ambito:') + 7
            index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
            ambito = clc(info_ediciones_apropiacion[index1:index2])
            index1 = info_ediciones_apropiacion.find('Sitio web:') + 10
            index2 = info_ediciones_apropiacion.find('Institución financiadora:', index1, len(info_ediciones_apropiacion))
            DOI = clc(info_ediciones_apropiacion[index1:index2])
            index1 = info_ediciones_apropiacion.find('Disponibilidad:') + 15
            index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
            disponibilidad = clc(info_ediciones_apropiacion[index1:index2])
            index1 = info_ediciones_apropiacion.find('Objeto:') + 7
            index2 = info_ediciones_apropiacion.find('Institución financiadora:', index1, len(info_ediciones_apropiacion))
            objeto = clc(info_ediciones_apropiacion[index1:index2])
            index1 = info_ediciones_apropiacion.find('Fecha de publicación:') + 21
            index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
            fecha = clc(info_ediciones_apropiacion[index1:index2])
            index1 = info_ediciones_apropiacion.find('Institución financiadora:') + 25
            index2 = info_ediciones_apropiacion.find('Autores:', index1, len(info_ediciones_apropiacion))
            institucion = clc(info_ediciones_apropiacion[index1:index2])
            index1 = info_ediciones_apropiacion.find('Autores:', index2, len(info_ediciones_apropiacion)) + 9
            index2 = info_ediciones_apropiacion.find('/br', index1, len(info_ediciones_apropiacion))
            autores = clc(info_ediciones_apropiacion[index1:index2])
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
            + "'" + DOI + "," \
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

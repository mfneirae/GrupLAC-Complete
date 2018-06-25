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

def asesorias_programaextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contasesorias_programa
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
        buscaasesorias_programa = containers[a].td
        #print(buscaasesorias_programa)
        try:
            if buscaasesorias_programa.text == "Asesorías al Programa Ondas":
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
            info_asesorias_programa = cont.text
            tipo = "114"
            index1 = info_asesorias_programa.find("- ") + 2
            index2 = info_asesorias_programa.find('\n',index1,len(info_asesorias_programa))
            nombreart = clc(info_asesorias_programa[index1:index2])
            index1 = info_asesorias_programa.find(" en ") + 4
            lugar = clc(info_asesorias_programa[index1:index2])
            index1 = info_asesorias_programa.find(' desde ',index1,len(info_asesorias_programa)) + 7
            index2 = info_asesorias_programa.find(' hasta', index1, len(info_asesorias_programa))
            desde = clc(info_asesorias_programa[index1:index2])
            anopub = clc(info_asesorias_programa[index1:index1 + 4])
            index1 = info_asesorias_programa.find(' hasta ',index1,len(info_asesorias_programa)) + 7
            index2 = info_asesorias_programa.find(', \n', index1, len(info_asesorias_programa))
            hasta = clc(info_asesorias_programa[index1:index2])
            index1 = info_asesorias_programa.find('Nombre de las ferias:',index1,len(info_asesorias_programa)) + 21
            index2 = info_asesorias_programa.find('Institución:', index1, len(info_asesorias_programa))
            ferias = clc(info_asesorias_programa[index1:index2])
            index1 = info_asesorias_programa.find('Institución:',index1,len(info_asesorias_programa)) + 12
            index2 = info_asesorias_programa.find('\n', index1, len(info_asesorias_programa))
            institucion = clc(info_asesorias_programa[index1:index2])
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
            + institucion +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            init.GP_ACTIVIDADES.append( \
            "REPLACE INTO `uapa_db`.`GP_ACTIVIDADES`(`CODGP_PROD_ACT`,`CODGP_PROD`,`Nombre_de_Ferias`,`Fecha_Inicio_Curso`,`Tipo_Orientación`,`Nombre_Estudiante`,`Programa_Académico`,`Divulgacion`,`Valoración`,`Fecha_fin_Curso`,`Finalidad`,`Duración`) VALUES"
            + "('" + str(codcolciencias) + "X" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + ferias + "'," \
            + "'" + desde + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + hasta + "'," \
            + "null" + "," \
            + "null" \
            + ");\n")
            init.GP_ACTIVIDADES_CSV.append(str(codcolciencias) + "X" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + ferias +";" \
            + desde +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + hasta +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contasesorias_programa = [COD_PRODUCTO]

def cursos_corta_duracionextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contcursos_corta_duracion
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
        buscacursos_corta_duracion = containers[a].td
        #print(buscacursos_corta_duracion)
        try:
            if buscacursos_corta_duracion.text == "Curso de Corta Duración Dictados":
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
            info_cursos_corta_duracion = cont.text
            index1 = info_cursos_corta_duracion.find("- ") + 2
            index2 = info_cursos_corta_duracion.find(':')
            tipo = clc(info_cursos_corta_duracion[index1:index2])
            #Tipo Artículo
            if tipo.strip() == "Perfeccionamiento":
                tipo = "115"
            elif tipo.strip() == "Extensión extracurricular":
                tipo = "116"
            elif tipo.strip() == "Especialización":
                tipo = "122"
            elif tipo.strip() == "Otro":
                tipo = "118"
            else:
                logging.critical('Añadir: ' + tipo + ' a cursos_corta_duracion')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_cursos_corta_duracion.find('\n', index1, len(info_cursos_corta_duracion))
            nombreart = clc(info_cursos_corta_duracion[index1:index2])
            index1 = index2 + 2
            index2 = info_cursos_corta_duracion.find(',', index1, len(info_cursos_corta_duracion))
            lugar = clc(info_cursos_corta_duracion[index1:index2])
            index1 = index2 + 2
            index2 = info_cursos_corta_duracion.find(',', index1, len(info_cursos_corta_duracion))
            anopub = clc(info_cursos_corta_duracion[index1:index2])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""
            index1 = info_cursos_corta_duracion.find('Idioma: ',index1,len(info_cursos_corta_duracion)) + 8
            index2 = info_cursos_corta_duracion.find(',', index1, len(info_cursos_corta_duracion))
            idioma = clc(info_cursos_corta_duracion[index1:index2])
            index1 = info_cursos_corta_duracion.find('Medio de divulgación:',index1,len(info_cursos_corta_duracion)) + 21
            index2 = info_cursos_corta_duracion.find('\n', index1, len(info_cursos_corta_duracion))
            divulgacion = clc(info_cursos_corta_duracion[index1:index2])
            index1 = info_cursos_corta_duracion.find('Sitio web:') + 10
            index2 = info_cursos_corta_duracion.find(',', index1, len(info_cursos_corta_duracion))
            DOI = clc(info_cursos_corta_duracion[index1:index2])
            index1 = info_cursos_corta_duracion.find('Participación')
            if index1 == -1:
                pass
            else:
                index1 = index1 + 13
                index2 = info_cursos_corta_duracion.find(',', index1, len(info_cursos_corta_duracion))
                participacion = clc(info_cursos_corta_duracion[index1:index2])
            index1 = info_cursos_corta_duracion.find('Duración (semanas):') + 19
            index2 = info_cursos_corta_duracion.find('Finalidad:', index1, len(info_cursos_corta_duracion))
            duracion = clc(info_cursos_corta_duracion[index1:index2])
            index1 = info_cursos_corta_duracion.find('Finalidad:') + 10
            index2 = info_cursos_corta_duracion.find('\n', index1, len(info_cursos_corta_duracion))
            finalidad = clc(info_cursos_corta_duracion[index1:index2])
            index1 = info_cursos_corta_duracion.find('Institución financiadora:') + 25
            index2 = info_cursos_corta_duracion.find('Autores:', index1, len(info_cursos_corta_duracion))
            institucion = clc(info_cursos_corta_duracion[index1:index2])
            index1 = info_cursos_corta_duracion.find('Autores:') + 8
            index2 = info_cursos_corta_duracion.find('\n', index1, len(info_cursos_corta_duracion))
            autores = clc(info_cursos_corta_duracion[index1:index2])
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
            + "'" + DOI + "'," \
            + "'" + participacion + "'," \
            + "'" + institucion + "'," \
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
            + participacion +";" \
            + institucion +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_ACTIVIDADES.append( \
            "REPLACE INTO `uapa_db`.`GP_ACTIVIDADES`(`CODGP_PROD_ACT`,`CODGP_PROD`,`Nombre_de_Ferias`,`Fecha_Inicio_Curso`,`Tipo_Orientación`,`Nombre_Estudiante`,`Programa_Académico`,`Divulgacion`,`Valoración`,`Fecha_fin_Curso`,`Finalidad`,`Duración`) VALUES"
            + "('" + str(codcolciencias) + "X" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + finalidad + "'," \
            + "'" + duracion + "'" \
            + ");\n")
            init.GP_ACTIVIDADES_CSV.append(str(codcolciencias) + "X" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + finalidad +";" \
            + duracion +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contcursos_corta_duracion = [COD_PRODUCTO]

def trabajos_dirigidosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global conttrabajos_dirigidos
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
        buscatrabajos_dirigidos = containers[a].td
        #print(buscatrabajos_dirigidos)
        try:
            if buscatrabajos_dirigidos.text == "Trabajos dirigidos/turorías":
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
            info_trabajos_dirigidos = cont.text
            index1 = info_trabajos_dirigidos.find("- ") + 2
            index2 = info_trabajos_dirigidos.find(':')
            tipo = "117"
            index1 = index2 + 2
            index2 = info_trabajos_dirigidos.find('\n', index1, len(info_trabajos_dirigidos))
            nombreart = clc(info_trabajos_dirigidos[index1:index2])
            index1 = info_trabajos_dirigidos.find('Desde', index2, len(info_trabajos_dirigidos)) + 5
            index2 = info_trabajos_dirigidos.find('hasta', index1, len(info_trabajos_dirigidos))
            desde = clc(info_trabajos_dirigidos[index1:index2])
            index1 = info_trabajos_dirigidos.find('hasta', index2, len(info_trabajos_dirigidos)) + 5
            index2 = info_trabajos_dirigidos.find(', Tipo de orientación:', index1, len(info_trabajos_dirigidos))
            hasta = clc(info_trabajos_dirigidos[index1:index2])
            anopub = clc(desde[len(desde)-4:len(desde)])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""
            index1 = info_trabajos_dirigidos.find('Tipo de orientación:',index1,len(info_trabajos_dirigidos)) + 20
            index2 = info_trabajos_dirigidos.find('\n', index1, len(info_trabajos_dirigidos))
            orientacion = clc(info_trabajos_dirigidos[index1:index2])
            index1 = info_trabajos_dirigidos.find('Nombre del estudiante:',index1,len(info_trabajos_dirigidos)) + 22
            index2 = info_trabajos_dirigidos.find(',', index1, len(info_trabajos_dirigidos))
            estudiante = clc(info_trabajos_dirigidos[index1:index2])
            index1 = info_trabajos_dirigidos.find('Programa académico:',index1,len(info_trabajos_dirigidos)) + 19
            index2 = info_trabajos_dirigidos.find('\n', index1, len(info_trabajos_dirigidos))
            programa = clc(info_trabajos_dirigidos[index1:index2])
            index1 = info_trabajos_dirigidos.find('Número de páginas:',index1,len(info_trabajos_dirigidos)) + 18
            index2 = info_trabajos_dirigidos.find(',', index1, len(info_trabajos_dirigidos))
            paginas = clc(info_trabajos_dirigidos[index1:index2])
            index1 = info_trabajos_dirigidos.find('Valoración:',index1,len(info_trabajos_dirigidos)) + 11
            index2 = info_trabajos_dirigidos.find('\n', index1, len(info_trabajos_dirigidos))
            valoracion = clc(info_trabajos_dirigidos[index1:index2])
            index1 = info_trabajos_dirigidos.find('Institución:') + 12
            index2 = info_trabajos_dirigidos.find('Autores:', index1, len(info_trabajos_dirigidos))
            institucion = clc(info_trabajos_dirigidos[index1:index2])
            index1 = info_trabajos_dirigidos.find('Autores:') + 8
            index2 = info_trabajos_dirigidos.find('\n', index1, len(info_trabajos_dirigidos))
            autores = clc(info_trabajos_dirigidos[index1:index2])
            init.REL_GRUPO_PRODUCTO.append( \
            "REPLACE INTO `uapa_db`.`REL_GRUPO_PRODUCTO`(`CODGP_PROD`,`CODGP`,`GP_TIPO_PROD`,`Nombre_Producto`,`Lugar`,`Año`,`Idioma`,`Páginas`,`Volumen`,`Editorial`,`Ambito`,`DOI`,`Descripción`,`Instituciones`,`Tipo_Vincula_Institu`,`Autores`) VALUES"
            + "('" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + "'," \
            + tipo + "," \
            + "'" + nombreart + "'," \
            + "null" + "," \
            + anopub + "," \
            + "null" + "," \
            + "'" + paginas + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + institucion + "'," \
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
            + institucion +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_ACTIVIDADES.append( \
            "REPLACE INTO `uapa_db`.`GP_ACTIVIDADES`(`CODGP_PROD_ACT`,`CODGP_PROD`,`Nombre_de_Ferias`,`Fecha_Inicio_Curso`,`Tipo_Orientación`,`Nombre_Estudiante`,`Programa_Académico`,`Divulgacion`,`Valoración`,`Fecha_fin_Curso`,`Finalidad`,`Duración`) VALUES"
            + "('" + str(codcolciencias) + "X" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "'" + orientacion + "'," \
            + "'" + estudiante + "'," \
            + "'" + programa + "'," \
            + "null" + "," \
            + "'" + valoracion + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null"\
            + ");\n")
            init.GP_ACTIVIDADES_CSV.append(str(codcolciencias) + "X" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + orientacion +";" \
            + estudiante +";" \
            + programa +";" \
            + "" +";" \
            + valoracion +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    conttrabajos_dirigidos = [COD_PRODUCTO]

def jurado_comisionesextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contjurado_comisiones
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
        buscajurado_comisiones = containers[a].td
        #print(buscajurado_comisiones)
        try:
            if buscajurado_comisiones.text == "Jurado/Comisiones evaluadoras de trabajo de grado":
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
            info_jurado_comisiones = cont.text
            index1 = info_jurado_comisiones.find("- ") + 2
            index2 = info_jurado_comisiones.find(':')
            tipo = clc(info_jurado_comisiones[index1:index2])
            if tipo.strip() == "Pregrado":
                tipo = "85"
            elif tipo.strip() == "Especialización":
                tipo = "86"
            elif tipo.strip() == "Especialidad Médica":
                tipo = "87"
            elif tipo.strip() == "Maestría":
                tipo = "88"
            elif tipo.strip() == "Doctorado":
                tipo = "89"
            elif tipo.strip() == "Otra":
                tipo = "90"
            elif tipo.strip() == "Curso de perfeccionamiento/especialización":
                tipo = "91"
            else:
                logging.critical('Añadir: ' + tipo + ' a jurado_comisiones')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_jurado_comisiones.find('\n', index1, len(info_jurado_comisiones))
            nombreart = clc(info_jurado_comisiones[index1:index2])
            index1 = index2 + 2
            index2 = info_jurado_comisiones.find(',', index1, len(info_jurado_comisiones))
            lugar = clc(info_jurado_comisiones[index1:index2])
            index1 = index2 + 2
            index2 = info_jurado_comisiones.find(',', index1, len(info_jurado_comisiones))
            anopub = clc(info_jurado_comisiones[index1:index2])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""


            index1 = info_jurado_comisiones.find('Idioma:', index2, len(info_jurado_comisiones)) + 7
            index2 = info_jurado_comisiones.find(',', index1, len(info_jurado_comisiones))
            idioma = clc(info_jurado_comisiones[index1:index2])
            index1 = info_jurado_comisiones.find('Medio de divulgación:', index2, len(info_jurado_comisiones)) + 21
            index2 = info_jurado_comisiones.find('\n', index1, len(info_jurado_comisiones))
            divulgacion = clc(info_jurado_comisiones[index1:index2])
            index1 = info_jurado_comisiones.find('Sitio web:', index2, len(info_jurado_comisiones)) + 10
            index2 = info_jurado_comisiones.find(',', index1, len(info_jurado_comisiones))
            DOI = clc(info_jurado_comisiones[index1:index2])
            index1 = info_jurado_comisiones.find('Nombre del orientado:',index1,len(info_jurado_comisiones)) + 21
            index2 = info_jurado_comisiones.find('\n', index1, len(info_jurado_comisiones))
            estudiante = clc(info_jurado_comisiones[index1:index2])
            index1 = info_jurado_comisiones.find('Programa académico:',index1,len(info_jurado_comisiones)) + 19
            index2 = info_jurado_comisiones.find(',', index1, len(info_jurado_comisiones))
            programa = clc(info_jurado_comisiones[index1:index2])
            index1 = info_jurado_comisiones.find('Institución:') + 12
            index2 = info_jurado_comisiones.find('Autores:', index1, len(info_jurado_comisiones))
            institucion = clc(info_jurado_comisiones[index1:index2])
            index1 = info_jurado_comisiones.find('Autores:') + 8
            index2 = info_jurado_comisiones.find('\n', index1, len(info_jurado_comisiones))
            autores = clc(info_jurado_comisiones[index1:index2])
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
            + "'" + DOI + "'," \
            + "null" + "," \
            + "'" + institucion + "'," \
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
            + institucion +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_ACTIVIDADES.append( \
            "REPLACE INTO `uapa_db`.`GP_ACTIVIDADES`(`CODGP_PROD_ACT`,`CODGP_PROD`,`Nombre_de_Ferias`,`Fecha_Inicio_Curso`,`Tipo_Orientación`,`Nombre_Estudiante`,`Programa_Académico`,`Divulgacion`,`Valoración`,`Fecha_fin_Curso`,`Finalidad`,`Duración`) VALUES"
            + "('" + str(codcolciencias) + "X" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + estudiante + "'," \
            + "'" + programa + "'," \
            + "'" + divulgacion + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null"\
            + ");\n")
            init.GP_ACTIVIDADES_CSV.append(str(codcolciencias) + "X" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + estudiante +";" \
            + programa +";" \
            + divulgacion +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contjurado_comisiones = [COD_PRODUCTO]

def comites_evaluacionextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contcomites_evaluacion
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
        buscacomites_evaluacion = containers[a].td
        #print(buscacomites_evaluacion)
        try:
            if buscacomites_evaluacion.text == "Participación en comités de evaluación":
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
            info_comites_evaluacion = cont.text
            index1 = info_comites_evaluacion.find("- ") + 2
            index2 = info_comites_evaluacion.find(':')
            tipo = clc(info_comites_evaluacion[index1:index2])
            if tipo.strip() == "Profesor titular":
                tipo = "78"
            elif tipo.strip() == "Concurso docente":
                tipo = "79"
            elif tipo.strip() == "Jefe de cátedra":
                tipo = "80"
            elif tipo.strip() == "Evaluación de cursos":
                tipo = "81"
            elif tipo.strip() == "Acreditación de programas":
                tipo = "82"
            elif tipo.strip() == "Asignación de becas":
                tipo = "83"
            elif tipo.strip() == "Otra":
                tipo = "84"
            else:
                logging.critical('Añadir: ' + tipo + ' a comites_evaluacion')
                print ("ALERTA: Revisar el archivo Registros.log")
            index1 = index2 + 2
            index2 = info_comites_evaluacion.find('\n', index1, len(info_comites_evaluacion))
            nombreart = clc(info_comites_evaluacion[index1:index2])
            index1 = index2 + 2
            index2 = info_comites_evaluacion.find(',', index1, len(info_comites_evaluacion))
            lugar = clc(info_comites_evaluacion[index1:index2])
            index1 = index2 + 2
            index2 = info_comites_evaluacion.find(',', index1, len(info_comites_evaluacion))
            anopub = clc(info_comites_evaluacion[index1:index2])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""



            index1 = info_comites_evaluacion.find('Sitio web:', index2, len(info_comites_evaluacion)) + 10
            index2 = info_comites_evaluacion.find('Medio de divulgación:', index1, len(info_comites_evaluacion))
            DOI = clc(info_comites_evaluacion[index1:index2])
            index1 = info_comites_evaluacion.find('Medio de divulgación:', index2, len(info_comites_evaluacion)) + 21
            index2 = info_comites_evaluacion.find('\n', index1, len(info_comites_evaluacion))
            divulgacion = clc(info_comites_evaluacion[index1:index2])
            index1 = info_comites_evaluacion.find('Institución:') + 12
            index2 = info_comites_evaluacion.find('Autores:', index1, len(info_comites_evaluacion))
            institucion = clc(info_comites_evaluacion[index1:index2])
            index1 = info_comites_evaluacion.find('Autores:') + 8
            index2 = info_comites_evaluacion.find('\n', index1, len(info_comites_evaluacion))
            autores = clc(info_comites_evaluacion[index1:index2])
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
            + DOI +";" \
            + "" +";" \
            + institucion +";" \
            + "" +";" \
            + autores +";" \
            + "\n")
            init.GP_ACTIVIDADES.append( \
            "REPLACE INTO `uapa_db`.`GP_ACTIVIDADES`(`CODGP_PROD_ACT`,`CODGP_PROD`,`Nombre_de_Ferias`,`Fecha_Inicio_Curso`,`Tipo_Orientación`,`Nombre_Estudiante`,`Programa_Académico`,`Divulgacion`,`Valoración`,`Fecha_fin_Curso`,`Finalidad`,`Duración`) VALUES"
            + "('" + str(codcolciencias) + "X" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + divulgacion + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null"\
            + ");\n")
            init.GP_ACTIVIDADES_CSV.append(str(codcolciencias) + "X" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + divulgacion +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contcomites_evaluacion = [COD_PRODUCTO]

def demas_trabajosextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contdemas_trabajos
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
        buscademas_trabajos = containers[a].td
        #print(buscademas_trabajos)
        try:
            if buscademas_trabajos.text == "Demás trabajos":
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
            info_demas_trabajos = cont.text
            index1 = info_demas_trabajos.find("- ") + 2
            index2 = info_demas_trabajos.find(':')
            tipo = "70"
            index1 = index2 + 2
            index2 = info_demas_trabajos.find('\n', index1, len(info_demas_trabajos))
            nombreart = clc(info_demas_trabajos[index1:index2])
            index1 = index2 + 2
            index2 = info_demas_trabajos.find(',', index1, len(info_demas_trabajos))
            lugar = clc(info_demas_trabajos[index1:index2])
            index1 = index2 + 2
            index2 = info_demas_trabajos.find(',', index1, len(info_demas_trabajos))
            anopub = clc(info_demas_trabajos[index1:index2])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""



            index1 = info_demas_trabajos.find('Idioma:', index2, len(info_demas_trabajos)) + 7
            index2 = info_demas_trabajos.find(',', index1, len(info_demas_trabajos))
            idioma = clc(info_demas_trabajos[index1:index2])
            index1 = info_demas_trabajos.find('Medio de divulgación:', index2, len(info_demas_trabajos)) + 21
            index2 = info_demas_trabajos.find('\n', index1, len(info_demas_trabajos))
            divulgacion = clc(info_demas_trabajos[index1:index2])
            index1 = info_demas_trabajos.find('Autores:') + 8
            index2 = info_demas_trabajos.find('\n', index1, len(info_demas_trabajos))
            autores = clc(info_demas_trabajos[index1:index2])
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
            init.GP_ACTIVIDADES.append( \
            "REPLACE INTO `uapa_db`.`GP_ACTIVIDADES`(`CODGP_PROD_ACT`,`CODGP_PROD`,`Nombre_de_Ferias`,`Fecha_Inicio_Curso`,`Tipo_Orientación`,`Nombre_Estudiante`,`Programa_Académico`,`Divulgacion`,`Valoración`,`Fecha_fin_Curso`,`Finalidad`,`Duración`) VALUES"
            + "('" + str(codcolciencias) + "X" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + divulgacion + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null"\
            + ");\n")
            init.GP_ACTIVIDADES_CSV.append(str(codcolciencias) + "X" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + divulgacion +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contdemas_trabajos = [COD_PRODUCTO]

def proyectos_grupoextract():
    from settings import my_url, coduapa, codhermes, codcolciencias, nombregi, dnilider, my_url, COD_PRODUCTO
    import bs4, logging, sys, re, init
    global contproyectos_grupo
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
        buscaproyectos_grupo = containers[a].td
        #print(buscaproyectos_grupo)
        try:
            if buscaproyectos_grupo.text == "Proyectos":
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
            info_proyectos_grupo = cont.text
            index1 = info_proyectos_grupo.find("- ") + 2
            index2 = info_proyectos_grupo.find(':')
            tipo = "119"
            index1 = index2 + 2
            index2 = info_proyectos_grupo.find('\n', index1, len(info_proyectos_grupo))
            nombreart = clc(info_proyectos_grupo[index1:index2])
            index1 = index2 + 2
            index2 = info_proyectos_grupo.find(' - \n', index1, len(info_proyectos_grupo))
            desde = clc(info_proyectos_grupo[index1:index2])
            anopub = clc(desde[0:4])
            try:
                ano = int(anopub)
            except ValueError:
                anopub = ""

            index1 = index2
            index2 = len(info_proyectos_grupo)
            hasta = clc(info_proyectos_grupo[index1:index2])
            if len(hasta) > 10:
                hasta = "-"
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
            init.GP_ACTIVIDADES.append( \
            "REPLACE INTO `uapa_db`.`GP_ACTIVIDADES`(`CODGP_PROD_ACT`,`CODGP_PROD`,`Nombre_de_Ferias`,`Fecha_Inicio_Curso`,`Tipo_Orientación`,`Nombre_Estudiante`,`Programa_Académico`,`Divulgacion`,`Valoración`,`Fecha_fin_Curso`,`Finalidad`,`Duración`) VALUES"
            + "('" + str(codcolciencias) + "X" + str(COD_PRODUCTO) + "',"\
            + "'" + str(codcolciencias) + str(COD_PRODUCTO) + "',"\
            + "null" + "," \
            + "'" + desde + "'," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "null" + "," \
            + "'" + hasta + "'," \
            + "null" + "," \
            + "null"\
            + ");\n")
            init.GP_ACTIVIDADES_CSV.append(str(codcolciencias) + "X" + str(COD_PRODUCTO) +";" \
            + str(codcolciencias) + str(COD_PRODUCTO) +";" \
            + "" +";" \
            + desde +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + "" +";" \
            + hasta +";" \
            + "" +";" \
            + "" +";" \
            + "\n")
            COD_PRODUCTO += 1
    else:
        logging.info(' El Grupo: ' + nombregi + 'no tiene Esquemas de Cirduitos Trazados Asociados')
    contproyectos_grupo = [COD_PRODUCTO]

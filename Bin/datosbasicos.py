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
    import bs4, logging, sys, re
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
        anoinidatos = re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
        index1 = index2 + 2
        index2 = len(info_datos)
        mesinidatos = re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
        print(anoinidatos+nombregi)
        print(mesinidatos+nombregi)
    else:
        print(' El Grupo de Investigación ' + nombregi + ' no tiene datos Asociados')
        # logging.info(' El Grupo de Investigación ' + nombregi + ' no tiene datos Asociados')
    # contdatoss = [COD_PRODUCTO]

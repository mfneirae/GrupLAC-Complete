import bs4, logging, sys, re
global contdatoss
my_url = "http://scienti.colciencias.gov.co:8085/gruplac/jsp/visualiza/visualizagr.jsp?nro=00000000019540"
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
all = 0
a = 0
x = 0
y = 0
contdatoss = 0
auto = ""
vincula = ""
insti = ""
vinculain = ""
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


print(all)

def clc(str):
    import re
    str = re.sub(r'[^A-Za-z0-9:=_?ÁÀÉÈÍÌÓÒÚÙéèáàé,ñńèíìúùóò .\-/+]',r'',re.sub(' +',' ',str.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    return str;

containerb = containers[all]
container = containerb.findAll("tr")
cont = container[2]
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


#_________________________________________________________________________
index1 = index2 + 2
index2 = info_ediciones_apropiacion.find('\n                ', index1, len(info_ediciones_apropiacion))
nombreart = clc(info_ediciones_apropiacion[index1:index2])
index1 = index2 + 17
index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
fecha_publica = clc(info_ediciones_apropiacion[index1:index2])
index1 = index2 - 5
index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
anopub = clc(info_ediciones_apropiacion[index1:index2])
index1 = info_ediciones_apropiacion.find('Ambito:') + 7
index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
ambito = clc(info_ediciones_apropiacion[index1:index2])
index1 = info_ediciones_apropiacion.find('NIT:') + 4
index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
nit = clc(info_ediciones_apropiacion[index1:index2])
index1 = info_ediciones_apropiacion.find('Fecha de registro ante cámara:') + 30
index2 = info_ediciones_apropiacion.find('\n', index1, len(info_ediciones_apropiacion))
registrocamara = clc(info_ediciones_apropiacion[index1:index2])
index1 = index2 +2
index2 = info_ediciones_apropiacion.find('\n', index1, len(info_ediciones_apropiacion))
productos = clc(info_ediciones_apropiacion[index1:index2])
index1 = info_ediciones_apropiacion.find('Sitio web:') + 10
index2 = info_ediciones_apropiacion.find('Institución financiadora:', index1, len(info_ediciones_apropiacion))
DOI = clc(info_ediciones_apropiacion[index1:index2])
index1 = info_ediciones_apropiacion.find('Disponibilidad:') + 15
index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
disponibilidad = clc(info_ediciones_apropiacion[index1:index2])
index1 = info_ediciones_apropiacion.find('Objeto:') + 7
index2 = info_ediciones_apropiacion.find('Institución financiadora:', index1, len(info_ediciones_apropiacion))
objeto = clc(info_ediciones_apropiacion[index1:index2])
index1 = info_ediciones_apropiacion.find('Institución financiadora:') + 25
index2 = info_ediciones_apropiacion.find('Autores:', index1, len(info_ediciones_apropiacion))
institucion = clc(info_ediciones_apropiacion[index1:index2])
index1 = info_ediciones_apropiacion.find('Número del registro:') + 20
index2 = info_ediciones_apropiacion.find(',', index1, len(info_ediciones_apropiacion))
contrato = clc(info_ediciones_apropiacion[index1:index2])
index1 = info_ediciones_apropiacion.find('Nombre del titular:') + 19
index2 = info_ediciones_apropiacion.find('\n', index1, len(info_ediciones_apropiacion))
titular = clc(info_ediciones_apropiacion[index1:index2])
index1 = info_ediciones_apropiacion.find('Nombre del proyecto:') + 20
index2 = info_ediciones_apropiacion.find('Institución financiadora:', index1, len(info_ediciones_apropiacion))
proyecto = clc(info_ediciones_apropiacion[index1:index2])
index1 = info_ediciones_apropiacion.find('Nombre comercial:') + 17
index2 = info_ediciones_apropiacion.find('Nombre del proyecto:', index1, len(info_ediciones_apropiacion))
comercial = clc(info_ediciones_apropiacion[index1:index2])
index1 = info_ediciones_apropiacion.find('Sitio web:') + 10
index2 = info_ediciones_apropiacion.find('Nombre comercial:', index1, len(info_ediciones_apropiacion))
DOI = clc(info_ediciones_apropiacion[index1:index2])
index1 = info_ediciones_apropiacion.find('Autores:') + 9
index2 = info_ediciones_apropiacion.find('/n', index1, len(info_ediciones_apropiacion))
autores = clc(info_ediciones_apropiacion[index1:index2])

import bs4, logging, sys, re
global contdatoss
my_url = "http://scienti.colciencias.gov.co:8085/gruplac/jsp/visualiza/visualizagr.jsp?nro=00000000001785"
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
    buscadatoss = containers[a].td
    #print(buscadatoss)
    try:
        if buscadatoss.text == "Artículos publicados":
            all = a
            #print(all)
            break
    except AttributeError:
        pass


print(all)
def clc(str):
    import re
    str = re.sub(r'[^A-Za-z0-9:=_?ÁÀÉÈÍÌÓÒÚÙéèáàé,ñèíìúùóò .\-/+]',r'',re.sub(' +',' ',str.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    return str;

containerb = containers[all]
container = containerb.findAll("tr")
cont = container[426]
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
index1 = index2 + 5
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
index1 = index2 + 7
index2 = info_articulo.find('Autores:', index1, len(info_articulo))
DOI = clc(info_articulo[index1:index2])
index1 = index2 + 9
index2 = info_articulo.find('/br', index1, len(info_articulo))
autores = clc(info_articulo[index1:index2])

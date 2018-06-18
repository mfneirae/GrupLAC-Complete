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
    buscaesquemas_trazados = containers[a].td
    #print(buscaesquemas_trazados)
    try:
        if buscaesquemas_trazados.text == "Esquemas de trazados de circuito integrado":
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
cont = container[1]
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
#_________________________________________________________________________
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

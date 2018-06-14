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
    buscacartas = containers[a].td
    #print(buscacartas)
    try:
        if buscacartas.text == "Cartas, mapas o similares":
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

#_________________________________________________________________________
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

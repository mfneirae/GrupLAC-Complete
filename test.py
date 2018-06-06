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
    buscalibross = containers[a].td
    #print(buscalibross)
    try:
        if buscalibross.text == " Libros publicados ":
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
cont = container[2]
info_libros = cont.text
index1 = info_libros.find("- ") + 2
index2 = info_libros.find(':')
tipo = clc(info_libros[index1:index2])
#Tipo Artículo
if tipo.strip() == "Libro resultado de investigación":
    tipo = "17"
elif tipo.strip() == "Otro libro publicado":
    tipo = "18"
elif tipo.strip() == "Libro pedagógico y/o de divulgación":
    tipo = "19"
else:
    logging.critical('Añadir: ' + tipo)
    print ("ALERTA: Revisar el archivo Libros.log")

containerb = containers[all]
container = containerb.findAll("tr")
cont = container[1]
info_libros = cont.text
index1 = info_libros.find("- ") + 2
index2 = info_libros.find(':')
tipo = clc(info_libros[index1:index2])
#Tipo Artículo
if tipo.strip() == "Libro resultado de investigación":
    tipo = "17"
elif tipo.strip() == "Otro libro publicado":
    tipo = "18"
elif tipo.strip() == "Libro pedagógico y/o de divulgación":
    tipo = "19"
else:
    logging.critical('Añadir: ' + tipo)
    print ("ALERTA: Revisar el archivo Libros.log")

index1 = index2 + 2
index2 = info_libros.find('\n', index1, len(info_libros))
nombreart = clc(info_libros[index1:index2])
index1 = index2 + 2
index2 = info_libros.find(',', index1, len(info_libros))
lugar = clc(info_libros[index1:index2])
index1 = index2 + 1
index2 = info_libros.find(', ISBN', index1, len(info_libros))
anopub = clc(info_libros[index1:index2])
index1 = index2 + 8
index2 = info_libros.find('vol:', index1, len(info_libros))
ISSN = clc(info_libros[index1:index2])
index1 = index2 + 4
index2 = info_libros.find('págs:', index1, len(info_libros))
vol = clc(info_libros[index1:index2])
index1 = index2 + 5
index2 = info_libros.find(', Ed.', index1, len(info_libros))
pags = clc(info_libros[index1:index2])
index1 = index2 + 5
index2 = info_libros.find('Autores:', index1, len(info_libros))
editorial = clc(info_libros[index1:index2])
index1 = index2 + 9
index2 = info_libros.find('/br', index1, len(info_libros))
autores = clc(info_libros[index1:index2])

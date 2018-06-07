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
    buscadoctra = containers[a].td
    #print(buscadoctra)
    try:
        if buscadoctra.text == "Documentos de trabajo ":
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
info_doctra = cont.text
index1 = info_doctra.find("- ") + 2
index2 = info_doctra.find(':')
tipo = clc(info_doctra[index1:index2])
#Tipo Artículo
if tipo.strip() == "Documento de trabajo Working Paper":
    tipo = "27"
else:
    logging.critical('Añadir: ' + tipo)
    print ("ALERTA: Revisar el archivo Documentos.log")

containerb = containers[all]
container = containerb.findAll("tr")
cont = container[2]
info_doctra = cont.text
#_________________________________________________________________________
index1 = info_doctra.find("- ") + 2
index2 = info_doctra.find(':')
tipo = clc(info_doctra[index1:index2])
#Tipo Artículo
if tipo == "Capítulo de libro":
    tipo = "21"
elif tipo == "Otro capítulo de libro publicado":
    tipo = "20"
else:
    logging.critical('Añadir: ' + tipo)
    print ("ALERTA: Revisar el archivo Capítulos Libros.log")

index1 = index2 + 2
index2 = info_doctra.find('\n', index1, len(info_doctra))
nombreart = clc(info_doctra[index1:index2])
index1 = index2 + 2
index2 = info_doctra.find('Nro. Paginas:', index1, len(info_doctra))
anopub = clc(info_doctra[index1:index2])
index1 = index2 + 13
index2 = info_doctra.find('Instituciones participantes:', index1, len(info_doctra)) - 19
nro = clc(info_doctra[index1:index2])
index1 = index2 + 47
index2 = info_doctra.find('URL: ', index1, len(info_doctra)) - 18
instituciones = clc(info_doctra[index1:index2])
index1 = index2 + 23
index2 = info_doctra.find('DOI:', index1, len(info_doctra)) -18
URL = clc(info_doctra[index1:index2])
index1 = index2 + 22
index2 = info_doctra.find('Autores:', index1, len(info_doctra))
DOI = clc(info_doctra[index1:index2])
index1 = index2 + 9
index2 = info_doctra.find('/br', index1, len(info_doctra))
autores = clc(info_doctra[index1:index2])

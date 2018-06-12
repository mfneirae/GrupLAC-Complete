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
    buscaotrosarticulos = containers[a].td
    #print(buscaotrosarticulos)
    try:
        if buscaotrosarticulos.text == "Otros artículos publicados":
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
info_otrosarticulos = cont.text
index1 = info_otrosarticulos.find("- ") + 2
index2 = info_otrosarticulos.find(':')
tipo = clc(info_otrosarticulos[index1:index2])
#Tipo Artículo
if tipo.strip() == "Periódico de noticias":
   tipo = "22"
elif tipo.strip() == "Revista de divulgación":
   tipo = "23"
elif tipo.strip() == "Carta al editor":
   tipo = "24"
elif tipo.strip() == "Reseñas de libros":
   tipo = "25"
elif tipo.strip() == "Columna de opinión":
   tipo = "26"
else:
   logging.critical('Añadir: ' + tipo)
   print ("ALERTA: Revisar el archivo Textos No Cientificos.log")

#_________________________________________________________________________
index1 = info_otrosarticulos.find("- ") + 2
index2 = info_otrosarticulos.find(':')
tipo = clc(info_otrosarticulos[index1:index2])
index1 = index2 + 2
index2 = info_otrosarticulos.find('\n', index1, len(info_otrosarticulos))
nombreart = clc(info_otrosarticulos[index1:index2])
index1 = index2 + 2
index2 = info_otrosarticulos.find(',', index1, len(info_otrosarticulos))
lugar = clc(info_otrosarticulos[index1:index2])
index1 = index2 + 1
index2 = info_otrosarticulos.find('ISSN:', index1, len(info_otrosarticulos))
revista = clc(info_otrosarticulos[index1:index2])
index1 = index2 + 5
index2 = info_otrosarticulos.find(',', index1, len(info_otrosarticulos))
ISSN = clc(info_otrosarticulos[index1:index2])
index1 = index2 + 2
index2 = info_otrosarticulos.find('vol:', index1, len(info_otrosarticulos))
anopub = clc(info_otrosarticulos[index1:index2])
index1 = info_otrosarticulos.find('vol:') + 4
index2 = info_otrosarticulos.find('fasc', index1, len(info_otrosarticulos))
vol = clc(info_otrosarticulos[index1:index2])
index1 = info_otrosarticulos.find('fasc:') + 5
index2 = info_otrosarticulos.find('págs', index1, len(info_otrosarticulos))
fasc = clc(info_otrosarticulos[index1:index2])
index1 = info_otrosarticulos.find('págs:') + 5
index2 = info_otrosarticulos.find('\n', index1, len(info_otrosarticulos))
pags = clc(info_otrosarticulos[index1:index2])
index = pags.find("-")
pagsini = clc(pags[0:index])
pagsfin = clc(pags[index + 2:len(pags)])
index1 = info_otrosarticulos.find('Autores:', index2, len(info_otrosarticulos)) + 9
index2 = info_otrosarticulos.find('/br', index1, len(info_otrosarticulos))
autores = clc(info_otrosarticulos[index1:index2])

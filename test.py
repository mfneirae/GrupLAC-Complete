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
    buscatraducciones = containers[a].td
    #print(buscatraducciones)
    try:
        if buscatraducciones.text == "Traducciones ":
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
info_traducciones = cont.text
index1 = info_traducciones.find("- ") + 2
index2 = info_traducciones.find(':')
tipo = clc(info_traducciones[index1:index2])
#Tipo Artículo
if tipo.strip() == "Artículo":
    tipo = "28"
elif tipo.strip() == "Libro":
    tipo = "29"
elif tipo.strip() == "Otra":
    tipo = "30"
else:
    logging.critical('Añadir: ' + tipo)
    print ("ALERTA: Revisar el archivo Eventos.log")

#_________________________________________________________________________
index1 = index2 + 2
index2 = info_traducciones.find('\n', index1, len(info_traducciones))
nombreart = clc(info_traducciones[index1:index2])
index1 = index2 + 2
index2 = info_traducciones.find(', Revista:', index1, len(info_traducciones))
anopub = clc(info_traducciones[index1:index2])
index1 = index2 + 10
index2 = info_traducciones.find('ISSN', index1, len(info_traducciones))
revista = clc(info_traducciones[index1:index2])
index1 = index2 + 4
index2 = info_traducciones.find(',', index1, len(info_traducciones))
ISSN = clc(info_traducciones[index1:index2])
index1 = info_traducciones.find('Libro:') + 6
index2 = info_traducciones.find('ISBN', index1, len(info_traducciones))
libroorigen = clc(info_traducciones[index1:index2])
index1 = index2 + 4
index2 = info_traducciones.find(',', index1, len(info_traducciones))
ISBN = clc(info_traducciones[index1:index2])
index1 = info_traducciones.find(', Medio de divulgación:') + 23
index2 = info_traducciones.find('\n', index1, len(info_traducciones))
medio = clc(info_traducciones[index1:index2])
index1 = info_traducciones.find('Idioma del documento original:') + 30
index2 = info_traducciones.find(',', index1, len(info_traducciones))
idiomaorigen = clc(info_traducciones[index1:index2])
index1 = info_traducciones.find('Idioma de la traducción:') + 24
index2 = info_traducciones.find('\n', index1, len(info_traducciones))
idiomatraduccion = clc(info_traducciones[index1:index2])
index1 = info_traducciones.find('Edición: ') + 9
index2 = info_traducciones.find(',', index1, len(info_traducciones))
edicion = clc(info_traducciones[index1:index2])
index1 = info_traducciones.find('Serie: ') + 7
index2 = info_traducciones.find(',', index1, len(info_traducciones))
serie = clc(info_traducciones[index1:index2])
index1 = info_traducciones.find('Autor del documento original:') + 29
index2 = info_traducciones.find('\n', index1, len(info_traducciones))
autorori = clc(info_traducciones[index1:index2])
index1 = info_traducciones.find('Autores:', index2, len(info_traducciones)) + 9
index2 = info_traducciones.find('/br', index1, len(info_traducciones))
autores = clc(info_traducciones[index1:index2])

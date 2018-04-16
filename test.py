import bs4, logging, sys, re
global contdatoss
my_url = "http://scienti.colciencias.gov.co:8085/gruplac/jsp/visualiza/visualizagr.jsp?nro=00000000002066"
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
        if buscadatoss.text == "Datos básicos":
            all = a
            #print(all)
            break
    except AttributeError:
        pass


print(all)

containerb = containers[all]
container = containerb.findAll("tr")
cont = container[1]
info_datos = cont.text
index1 = info_datos.find("Año y mes de formación") + 22
index2 = info_datos.find(" -")
anoinidatos = re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
index1 = index2 + 2
index2 = len(info_datos)
mesinidatos = re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',info_datos[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))

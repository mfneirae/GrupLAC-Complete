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
        if buscadatoss.text == "Sectores de aplicación":
            all = a
            #print(all)
            break
    except AttributeError:
        pass


print(all)

containerb = containers[all]
container = containerb.findAll("tr")
cont = container[x]
info_sectores = cont.text
index1 = info_sectores.find('-') + 1
index2 = len(info_sectores)
institucion = re.sub(r'[^A-Za-z0-9ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/+]',r'',re.sub(' +',' ',info_sectores[index1:index2].replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))

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
        if buscadatoss.text == "Integrantes del grupo":
            all = a
            #print(all)
            break
    except AttributeError:
        pass


print(all)
def clc(str):
    import re
    str = re.sub(r'[^A-Za-z0-9:=_?ÁÀÉÈÍÌÓÒÚÙéèáàéñèíìúùóò .\-/+]',r'',re.sub(' +',' ',str.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r","")))
    return str;

containerb = containers[all]
container = containerb.findAll("tr")
cont = container[2]
info_integrantes = str(cont)

cont = container[2]
info_integrantes = str(cont)
#RH
index1 = info_integrantes.find('cod_rh=') + 7
index2 = info_integrantes.find('"',index1,len(info_integrantes))
cod_rh = clc(info_integrantes[index1:index2])
#csvs
index1 = info_integrantes.find('href="') + 6
index2 = info_integrantes.find('"',index1,len(info_integrantes))
linkcv = clc(info_integrantes[index1:index2])
#Nombre
index = index2
index1 = info_integrantes.find('blank">',index,len(info_integrantes)) + 7
index2 = info_integrantes.find('</a>',index1,len(info_integrantes))
nombre = clc(info_integrantes[index1:index2])
#Vinculación
index = index2
index1 = info_integrantes.find('">',index,len(info_integrantes)) + 2
index2 = info_integrantes.find('</td>',index1,len(info_integrantes))
tipvincula = clc(info_integrantes[index1:index2])
#HorasDedicación
index = index2
index1 = info_integrantes.find('">',index,len(info_integrantes)) + 2
index2 = info_integrantes.find('</td>',index1,len(info_integrantes))
horasdedic = clc(info_integrantes[index1:index2])
#Duración Vincula
index = index2
index1 = info_integrantes.find('">',index,len(info_integrantes)) + 2
index2 = info_integrantes.find('</td>',index1,len(info_integrantes))
index = index2
duravincula = clc(info_integrantes[index1:index2])
index2 = info_integrantes.find('-',index1,len(info_integrantes))
duravinculaini = clc(info_integrantes[index1:index2])
index1 = index2 + 2
index2 = index
duravinculafin = clc(info_integrantes[index1:index2])

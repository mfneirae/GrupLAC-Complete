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

containerb = containers[all]
container = containerb.findAll("tr")
cont = container[x]

index1 = info_integrantes.find('href="') + 6
index2 = info_integrantes.find('"',index1,len(info_integrantes))
linkcv = clc(info_integrantes[index1:index2])

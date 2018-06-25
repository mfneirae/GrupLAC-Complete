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
    buscaasesorias_programa = containers[a].td
    #print(buscaasesorias_programa)
    try:
        if buscaasesorias_programa.text == "Asesorías al Programa Ondas":
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
info_asesorias_programa = cont.text

tipo = "112"
#Tipo Artículo


#_________________________________________________________________________
index1 = info_asesorias_programa.find("- ") + 2
index2 = info_asesorias_programa.find('\n',index1,len(info_asesorias_programa))
nombreart = clc(info_asesorias_programa[index1:index2])
index1 = info_asesorias_programa.find(" en ") + 4
lugar = clc(info_asesorias_programa[index1:index2])
index1 = info_asesorias_programa.find(' desde ',index1,len(info_asesorias_programa)) + 7
index2 = info_asesorias_programa.find(' hasta', index1, len(info_asesorias_programa))
desde = clc(info_asesorias_programa[index1:index2])
anopub = clc(info_asesorias_programa[index1:index1 + 4])
index1 = info_asesorias_programa.find(' hasta ',index1,len(info_asesorias_programa)) + 7
index2 = info_asesorias_programa.find(', \n', index1, len(info_asesorias_programa))
hasta = clc(info_asesorias_programa[index1:index2])
index1 = info_asesorias_programa.find('Nombre de las ferias:',index1,len(info_asesorias_programa)) + 21
index2 = info_asesorias_programa.find('Institución:', index1, len(info_asesorias_programa))
ferias = clc(info_asesorias_programa[index1:index2])
index1 = info_asesorias_programa.find('Institución:',index1,len(info_asesorias_programa)) + 12
index2 = info_asesorias_programa.find('\n', index1, len(info_asesorias_programa))
institucion = clc(info_asesorias_programa[index1:index2])

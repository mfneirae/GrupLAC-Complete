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
    buscajurado_comisiones = containers[a].td
    #print(buscajurado_comisiones)
    try:
        if buscajurado_comisiones.text == "Proyectos":
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
info_proyectos_grupo = cont.text
index1 = info_proyectos_grupo.find("- ") + 2
index2 = info_proyectos_grupo.find(':')
tipo = clc(info_proyectos_grupo[index1:index2])

#Tipo Artículo
if tipo.strip() == "Profesor titular":
    tipo = "78"
elif tipo.strip() == "Concurso docente":
    tipo = "79"
elif tipo.strip() == "Jefe de cátedra":
    tipo = "80"
elif tipo.strip() == "Evaluación de cursos":
    tipo = "81"
elif tipo.strip() == "Acreditación de programas":
    tipo = "82"
elif tipo.strip() == "Asignación de becas":
    tipo = "83"
elif tipo.strip() == "Otra":
    tipo = "84"
else:
    logging.critical('Añadir: ' + tipo + ' a comites_evaluacion')
    print ("ALERTA: Revisar el archivo Registros.log")


#_________________________________________________________________________
index1 = index2 + 2
index2 = info_proyectos_grupo.find('\n', index1, len(info_proyectos_grupo))
nombreart = clc(info_proyectos_grupo[index1:index2])
index1 = index2 + 2
index2 = info_proyectos_grupo.find(' - \n', index1, len(info_proyectos_grupo))
desde = clc(info_proyectos_grupo[index1:index2])
anopub = clc(desde[0:4])
try:
    ano = int(anopub)
except ValueError:
    anopub = ""

index1 = index2 + 2
index2 = len(info_proyectos_grupo)
hasta = clc(info_proyectos_grupo[index1:index2])

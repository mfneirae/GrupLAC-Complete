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
    buscaempresas_base_tec = containers[a].td
    #print(buscaempresas_base_tec)
    try:
        if buscaempresas_base_tec.text == "Empresas de base tecnológica ":
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
info_empresas_base_tec = cont.text
index1 = info_empresas_base_tec.find("- ") + 2
index2 = info_empresas_base_tec.find(':')
tipo = clc(info_empresas_base_tec[index1:index2])
#Tipo Artículo
if tipo.strip() == "Spin-off":
   tipo = "68"
elif tipo.strip() == "Start-up":
   tipo = "69"
else:
    logging.critical('Añadir: ' + tipo + ' a empresas_base_tec')
    print ("ALERTA: Revisar el archivo Registros.log")


#_________________________________________________________________________
index1 = index2 + 2
index2 = info_empresas_base_tec.find('\n                ', index1, len(info_empresas_base_tec))
nombreart = clc(info_empresas_base_tec[index1:index2])
index1 = index2 + 17
index2 = info_empresas_base_tec.find(',', index1, len(info_empresas_base_tec))
fecha_publica = clc(info_empresas_base_tec[index1:index2])
index1 = index2 - 5
index2 = info_empresas_base_tec.find(',', index1, len(info_empresas_base_tec))
anopub = clc(info_empresas_base_tec[index1:index2])
index1 = info_empresas_base_tec.find('Ambito:') + 7
index2 = info_empresas_base_tec.find(',', index1, len(info_empresas_base_tec))
ambito = clc(info_empresas_base_tec[index1:index2])
index1 = info_empresas_base_tec.find('NIT:') + 4
index2 = info_empresas_base_tec.find(',', index1, len(info_empresas_base_tec))
nit = clc(info_empresas_base_tec[index1:index2])
index1 = info_empresas_base_tec.find('Fecha de registro ante cámara:') + 30
index2 = info_empresas_base_tec.find('\n', index1, len(info_empresas_base_tec))
registrocamara = clc(info_empresas_base_tec[index1:index2])
index1 = index2 +2
index2 = info_empresas_base_tec.find('\n', index1, len(info_empresas_base_tec))
productos = clc(info_empresas_base_tec[index1:index2])
index1 = info_empresas_base_tec.find('Sitio web:') + 10
index2 = info_empresas_base_tec.find('Institución financiadora:', index1, len(info_empresas_base_tec))
DOI = clc(info_empresas_base_tec[index1:index2])
index1 = info_empresas_base_tec.find('Disponibilidad:') + 15
index2 = info_empresas_base_tec.find(',', index1, len(info_empresas_base_tec))
disponibilidad = clc(info_empresas_base_tec[index1:index2])
index1 = info_empresas_base_tec.find('Objeto:') + 7
index2 = info_empresas_base_tec.find('Institución financiadora:', index1, len(info_empresas_base_tec))
objeto = clc(info_empresas_base_tec[index1:index2])
index1 = info_empresas_base_tec.find('Institución financiadora:') + 25
index2 = info_empresas_base_tec.find('Autores:', index1, len(info_empresas_base_tec))
institucion = clc(info_empresas_base_tec[index1:index2])
index1 = info_empresas_base_tec.find('Número del registro:') + 20
index2 = info_empresas_base_tec.find(',', index1, len(info_empresas_base_tec))
contrato = clc(info_empresas_base_tec[index1:index2])
index1 = info_empresas_base_tec.find('Nombre del titular:') + 19
index2 = info_empresas_base_tec.find('\n', index1, len(info_empresas_base_tec))
titular = clc(info_empresas_base_tec[index1:index2])
index1 = info_empresas_base_tec.find('Nombre del proyecto:') + 20
index2 = info_empresas_base_tec.find('Institución financiadora:', index1, len(info_empresas_base_tec))
proyecto = clc(info_empresas_base_tec[index1:index2])
index1 = info_empresas_base_tec.find('Nombre comercial:') + 17
index2 = info_empresas_base_tec.find('Nombre del proyecto:', index1, len(info_empresas_base_tec))
comercial = clc(info_empresas_base_tec[index1:index2])
index1 = info_empresas_base_tec.find('Sitio web:') + 10
index2 = info_empresas_base_tec.find('Nombre comercial:', index1, len(info_empresas_base_tec))
DOI = clc(info_empresas_base_tec[index1:index2])
index1 = info_empresas_base_tec.find('Autores:') + 9
index2 = info_empresas_base_tec.find('/n', index1, len(info_empresas_base_tec))
autores = clc(info_empresas_base_tec[index1:index2])

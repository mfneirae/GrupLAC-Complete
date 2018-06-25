#
#
# #############################################################################
#       Copyright (c) 2018 Universidad Nacional de Colombia All Rights Reserved.
#
#             This work was made as a development to improve data collection
#       for self-assessment and accreditation processes in the Vicedeanship
#       of academic affairs in the Engineering Faculty of the Universidad
#       Nacional de Colombia and is licensed under a Creative Commons
#       Attribution-NonCommercial - ShareAlike 4.0 International License
#       and MIT Licence.
#
#       by Manuel Embus.
#
#       For more information write me to jai@mfneirae.com
#       Or visit my webpage at https://mfneirae.com/
# #############################################################################
#
#
def inicio():
    global GP_DATOS_BASE
    global GP_DATOS_BASE_CSV
    global GP_DATOS_INSTITUCIONES
    global GP_DATOS_INSTITUCIONES_CSV
    global GP_DATOS_LINEAS
    global GP_DATOS_LINEAS_CSV
    global GP_DATOS_SECTORES
    global GP_DATOS_SECTORES_CSV
    global GP_DATOS_INTEGRANTES
    global GP_DATOS_INTEGRANTES_CSV
    global REL_GRUPO_PRODUCTO
    global REL_GRUPO_PRODUCTO_CSV
    global GP_PROD_BIB
    global GP_PROD_BIB_CSV
    global GP_PROD_TEC
    global GP_PROD_TEC_CSV
    global GP_APROPIACION
    global GP_APROPIACION_CSV
    global GP_OBRAS
    global GP_OBRAS_CSV
    global GP_ACTIVIDADES
    global GP_ACTIVIDADES_CSV
    global v_colciencias_tipo_producto
    global inv_colciencias_tipo_producto

    GP_DATOS_BASE = []
    GP_DATOS_INSTITUCIONES = []
    GP_DATOS_LINEAS = []
    GP_DATOS_SECTORES = []
    GP_DATOS_INTEGRANTES = []
    REL_GRUPO_PRODUCTO = []
    GP_PROD_BIB = []
    GP_PROD_TEC = []
    GP_APROPIACION = []
    GP_OBRAS = []
    GP_ACTIVIDADES = []

    GP_PROD_BIB_CSV=["CODGP_PROD_BIB; \
CODGP_PROD:\
Revista; \
Autor Original; \
Nombre Libro; \
ISBN/ISSN; \
Medio de Divulgación; \
URL; \
Fasciculos; \
Idioma Original; \
Idioma Traduccion; \
Edición; \
Serie; \
Página Inicial; \
Página Final    ; \
\n"]

    GP_PROD_TEC_CSV=["CODGP_PROD_TEC; \
CODGP_PROD; \
Tema; \
Nombre Comerial; \
Nombre Proyecto; \
Tipo de Ciclo; \
NIT; \
Fecha de Registro; \
Tiene Productos; \
Disponibilidad; \
Objeto; \
Fecha Publicación; \
Número de Contrato; \
Acto Administrativo; \
\n"]

    GP_APROPIACION_CSV=["CODGP_PROD_APROPIACION; \
CODGP_PROD; \
Tipos de Participación; \
Fecha Inicio; \
Fecha Fin; \
Proyecto de Inv; \
Medio de publicación; \
Emisora; \
Número de Participantes; \
\n"]

    GP_OBRAS_CSV=["CODGP_PROD_OBRAS; \
CODGP_PROD; \
Fecha Creación; \
Disiplina de origen; \
Institución Licencia; \
Fecha Licencia; \
Distinciones; \
Selección Distinción; \
Productos Asociados; \
Número Derechos Autor/NIT; \
\n"]

    GP_ACTIVIDADES_CSV=["CODGP_PROD_FORM; \
CODGP_PROD; \
Nombre de Ferias; \
Fecha Inicio Curso; \
Tipo Orientación; \
Nombre Estudiante; \
Programa Académico; \
Valoración; \
Fecha fin Curso; \
Finalidad; \
Duración; \
\n"]

    REL_GRUPO_PRODUCTO_CSV =["CODGP_PROD; \
CODGP; \
GP_TIPO_PROD; \
Nombre Producto; \
Lugar; \
Año; \
Idioma; \
Páginas; \
Volumen; \
Editorial; \
Ambito; \
DOI; \
Descripción; \
Instituciones; \
Tipo Vincula Institu; \
Autores\n"]

    GP_DATOS_BASE_CSV = ["CODGP;\
Año Formación;\
Mes Formación;\
Lugar;\
Nombre Lider;\
Información Certificada;\
Página Web;\
Correo;\
Clasificación;\
Área del Conocimiento;\
Programa Nacional;\
Programa Nacional 2;\
Plan de trabajo;\
Estado del Arte;\
Objetivos;\
Retos;\
Visión\n"]

    GP_DATOS_INSTITUCIONES_CSV = ["CODGP_INSTI;\
CODGP;\
Nombre Institución\n"]

    GP_DATOS_LINEAS_CSV = ["CODGP_LINEA;\
CODGP;\
Línea de Investigación\n"]

    GP_DATOS_SECTORES_CSV = ["CODGP_SECTOR;\
CODGP;\
Sector\n"]

    GP_DATOS_INTEGRANTES_CSV = ["CODGP_INTEGRANTE;\
CODGP;\
COD_RG;\
CVLAC;\
NOMBRE COMPLETO;\
Tipo Vinculación;\
Horas de Dedicación;\
Duración Vinculación;\
Inicio Vinculación;\
Fin Vinculación;\
Fin Vinculación\n"]

    v_colciencias_tipo_producto = [ "COD_TIPO_PRODUCTO; \
TIPO_PRODUCTO_COL; \
SUB_TIPO_PRODUCTO_COL; \
TIPO_UAPA\n\
0; \
Evento sin producto asociado; \
Evento sin producto asociado; \
Evento sin producto asociado\n\
1; \
Redes de conocimiento; \
Redes de conocimiento; \
Redes de conocimiento\n\
2; \
Producción bibliográfica - Trabajos en eventos (Capítulos de memoria) - Completo; \
Capítulos de memoria; \
Capítulos de memoria\n\
3; \
Producción técnica - Presentación de trabajo - Comunicación; \
Presentación de trabajo; \
Trabajo de Comunicación\n\
4; \
Demás trabajos - Demás trabajos - Póster; \
Demás trabajos; \
Poster\n\
5; \
Producción técnica - Presentación de trabajo - Conferencia; \
Presentación de trabajo; \
Conferencia\n\
6; \
Producción técnica - Presentación de trabajo - Ponencia; \
Presentación de trabajo; \
Ponencia\n\
7; \
Estrategias pedagógicas para el fomento a la CTI; \
Estrategias pedagógicas; \
Estrategias pedagógicas\n\
8; \
Producción bibliográfica - Artículo - Publicado en revista especializada; \
Publicado en revista especializada; \
Artículo\n\
9; \
Producción bibliográfica - Artículo - Corto (Resumen); \
Corto (Resumen); \
Artículo\n\
10; \
Estrategias pedagógicas para el fomento a la CTI; \
Estrategias pedagógicas; \
Estrategias pedagógicas\n\
11; \
Producción bibliográfica - Artículo - Caso clínico; \
Caso Clínico; \
Artículo\n\
12; \
Producción bibliográfica - Trabajos en eventos (Capítulos de memoria) - Resumen; \
Capítulo de Memoria; \
Resumen\n\
13; \
Producción técnica - Presentación de trabajo - Congreso; \
Congreso; \
Congreso\n\
14; \
Producción técnica - Presentación de trabajo - Simposio; \
Simposio; \
Simposio\n\
15; \
Producción técnica - Presentación de trabajo - Seminario; \
Seminario; \
Seminario\n\
16; \
Producción técnica - Presentación de trabajo - Otro; \
Otro; \
Otro\n\
17; \
Producción bibliográfica - Libro - Libro resultado de investigación; \
Libro resultado de investigación; \
Libro\n\
18; \
Producción bibliográfica - Libro - Otro libro publicado; \
Otro libro publicado; \
Libro - Otro\n\
19; \
Producción bibliográfica - Libro - Libro pedagógico y/o de divulgación; \
Libro pedagógico y/o de divulgación; \
Libro - pedagógico\n\
20; \
Otro capítulo de libro publicado; \
Otro capítulo de libro; \
Capítulo de libro - Otro\n\
21; \
Capítulo de libro; \
Capítulo de libro; \
Capítulo de libro\n\
22; \
Producción bibliográfica - Otro artículo publicado - Periódico de noticias; \
Periódico de noticias; \
Otro\n\
23; \
Producción bibliográfica - Otro artículo publicado - Revista de divulgación; \
Revista de divulgación; \
Otro\n\
24; \
Producción bibliográfica - Otro artículo publicado - Cartas al editor; \
Cartas al editor; \
Otro\n\
25; \
Producción bibliográfica - Otro artículo publicado - Reseñas de libros; \
Reseñas de libros; \
Otro\n\
26; \
Producción bibliográfica - Otro artículo publicado - Columna de opinión; \
Columnas de opinión; \
Otro\n\
27; \
Producción bibliográfica - Documento de trabajo (Working Paper); \
Documento de trabajo (Working Paper); \
Otro\n\
28; \
Producción bibliográfica - Traducciones - Artículo; \
Traducciones - Artículo; \
Traducciones\n\
29; \
Producción bibliográfica - Traducciones - Libro; \
Traducciones - Libro; \
Traducciones\n\
30; \
Producción bibliográfica - Traducciones - Otra; \
Traducciones - Otra; \
Traducciones\n\
31; \
Producción bibliográfica - Otra producción bibliográfica - Introducción; \
Introducción; \
Otro\n\
32; \
Producción bibliográfica - Otra producción bibliográfica - Prólogo; \
Prólogo; \
Otro\n\
33; \
Producción bibliográfica - Otra producción bibliográfica - Epílogo; \
Epílogo; \
Otro\n\
34; \
Producción bibliográfica - Otra producción bibliográfica - Otra; \
Otra; \
Otro\n\
35; \
Producción técnica - Softwares - Computacional; \
Software; \
Software\n\
36; \
Producción técnica - Productos tecnológicos - Gen Clonado; \
Productos tecnológicos - Gen Clonado; \
Productos tecnológicos\n\
37; \
Producción técnica - Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada; \
Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada; \
Productos tecnológicos\n\
38; \
Producción técnica - Productos tecnológicos - Otro; \
Productos tecnológicos - Otro; \
Productos tecnológicos\n\
39; \
Producción técnica - Productos tecnológicos - Base de datos de referencia para investigación; \
Productos tecnológicos - Base de datos de referencia para investigación; \
Productos tecnológicos\n\
40; \
Producción técnica - Diseño Industrial; \
Diseño Industrial; \
Otro\n\
41; \
Producción técnica - Esquema de circuito integrado; \
Esquema de circuito integrado; \
Otro\n\
42; \
Producción técnica - Innovaciones generadas de producción empresarial - Organizacional; \
Innovaciones generadas de producción empresarial - Organizacional; \
Innovaciones\n\
43; \
Producción técnica - Innovaciones generadas de producción empresarial - Empresarial; \
Innovaciones generadas de producción empresarial - Empresarial; \
Innovaciones\n\
44; \
Producción técnica - Variedad animal; \
Variedad animal; \
Otro\n\
45; \
Producción técnica - Innovación de proceso o procedimiento; \
Innovación de proceso o procedimiento; \
Innovación\n\
46; \
Producción técnica - Cartas, mapas o similares - Aerofotograma; \
Aerofotograma; \
Otro\n\
47; \
Producción técnica - Cartas, mapas o similares - Carta; \
Carta; \
Otro\n\
48; \
Producción técnica - Cartas, mapas o similares - Fotograma; \
Fotograma; \
Otro\n\
49; \
Producción técnica - Cartas, mapas o similares - Mapa; \
Mapa; \
Otro\n\
50; \
Producción técnica - Cartas, mapas o similares - Otra; \
Otra; \
Otro\n\
51; \
Producción técnica - Variedad vegetal; \
Variedad vegetal; \
Otro\n\
52; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Servicios de proyectos de IDI; \
Servicios de proyectos de IDI; \
Otro\n\
53; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Comercialización de tecnología; \
Comercialización de tecnología; \
Otro\n\
54; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Análisis de competitividad; \
Análisis de competitividad; \
Otro\n\
55; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Informe técnico; \
Informe técnico; \
Otro\n\
56; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Otro; \
Otro; \
Otro\n\
57; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Acciones de transferencia tecnológica; \
Acciones de transferencia tecnológica; \
Otro\n\
58; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Desarrollo de productos; \
Desarrollo de productos; \
Otro\n\
59; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Implementación de sistemas de análisis; \
Implementación de sistemas de análisis; \
Otro\n\
60; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Consultoría en artes,arquitectura y diseño; \
Consultoría en artes,arquitectura y diseño; \
Otro\n\
61; \
Producción técnica - Regulación, norma, reglamento o legislación - Ambiental o de Salud; \
Regulación, norma, reglamento o legislación - Ambiental o de Salud; \
Otro\n\
62; \
Producción técnica - Regulación, norma, reglamento o legislación - Educativa; \
Regulación, norma, reglamento o legislación - Educativa; \
Otro\n\
63; \
Producción técnica - Regulación, norma, reglamento o legislación - Social; \
Regulación, norma, reglamento o legislación - Social; \
Otro\n\
64; \
Producción técnica - Regulación, norma, reglamento o legislación - Técnica; \
Regulación, norma, reglamento o legislación - Técnica; \
Otro\n\
65; \
Producción técnica - Regulación, norma, reglamento o legislación - Guía de práctica clínica; \
Regulación, norma, reglamento o legislación - Guía de práctica clínica; \
Otro\n\
66; \
Producción técnica - Regulación, norma, reglamento o legislación - Proyecto de ley; \
Regulación, norma, reglamento o legislación - Proyecto de ley; \
Otro\n\
67; \
Producción técnica - Reglamento Técnico; \
Reglamento Técnico; \
Otro\n\
68; \
Producción técnica - Empresa de base tecnológica - Spin-off; \
Empresa de base tecnológica - Spin-off; \
Otro\n\
69; \
Producción técnica - Empresa de base tecnológica - Start-up; \
Empresa de base tecnológica - Start-up; \
Otro\n\
70; \
Demás trabajos - Demás trabajos; \
Demás trabajos; \
Otro\n\
71; \
Producción técnica - Signos; \
Signos; \
Otro\n\
72; \
Producción técnica - Softwares - Multimedia; \
Multimedia; \
Software\n\
73; \
Producción técnica - Softwares - Otra; \
Softwares - Otra; \
Software\n\
74; \
Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Básica; \
Técnica - Básica; \
Otro\n\
75; \
Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Ensayo; \
Técnica - Ensayo; \
Otro\n\
76; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Servicios de Proyectos de I+D+I; \
Servicios de Proyectos de I+D+I; \
Otro\n\
77; \
Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Proceso; \
Técnica - Proceso; \
Otro\n\
78; \
Datos complementarios - Participación en comités de evaluación - Profesor titular; \
Participación en comités de evaluación - Profesor titular; \
Comités\n\
79; \
Datos complementarios - Participación en comités de evaluación - Concurso docente; \
Participación en comités de evaluación - Concurso docente; \
Comités\n\
80; \
Datos complementarios - Participación en comités de evaluación - Jefe de cátedra; \
Participación en comités de evaluación - Jefe de cátedra; \
Comités\n\
81; \
Datos complementarios - Participación en comités de evaluación - Evaluación de cursos; \
Participación en comités de evaluación - Evaluación de cursos; \
Comités\n\
82; \
Datos complementarios - Participación en comités de evaluación - Acreditación de programas; \
Participación en comités de evaluación - Acreditación de programas; \
Comités\n\
83; \
Datos complementarios - Participación en comités de evaluación - Asignación de becas; \
Participación en comités de evaluación - Asignación de becas; \
Comités\n\
84; \
Datos complementarios - Participación en comités de evaluación - Otra; \
Participación en comités de evaluación - Otra; \
Comités\n\
85; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Pregrado; \
Jurado Pregrado; \
Comités\n\
86; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Especialización; \
Jurado Especialización; \
Comités\n\
87; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Especialidad Médica; \
Jurado Especialidad Médica; \
Comités\n\
88; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Maestría; \
Jurado Maestría; \
Comités\n\
89; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Doctorado; \
Jurado Doctorado; \
Comités\n\
90; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Otra; \
Jurado Otra; \
Comités\n\
91; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Curso de perfeccionamiento/especialización; \
Jurado Especializaciones; \
Comités\n\
96; \
Producción técnica - Signos Distintivos - Nombres comerciales; \
Signos Distintivos - Nombres comerciales; \
Nombres comerciales\n\
92; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Curso de perfeccionamiento/especialización; \
Jurado Especializaciones; \
Comités\n\
93; \
Producción técnica - Plantas piloto - Planta piloto; \
Plantas piloto - Planta piloto; \
Planta piloto\n\
94; \
Producción técnica - Prototipo - Industrial; \
Prototipo - Industrial; \
Industrial\n\
95; \
Producción técnica - Signos Distintivos - Marcas; \
Signos Distintivos - Marcas; \
Marcas\n\
96; \
Producción técnica - Signos Distintivos - Nombres comerciales; \
Signos Distintivos - Nombres comerciales; \
Nombres comerciales\n\
97; \
Apropiación social y circularción del conocimiento - Ediciones - Anales; \
Ediciones - Anales; \
Analess\n\
98; \
Apropiación social y circularción del conocimiento - Ediciones - Libro; \
Ediciones - Libro; \
Libro\n\
92; \
Producción técnica - Prototipo - Servicios; \
Prototipo - Servicios; \
Servicios\n"]

#***************************************************************************
#Insert
#***************************************************************************
    inv_colciencias_tipo_producto = [ "REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`cod_tipo_producto`,\
`tipo_producto_col`,\
`sub_tipo_producto_col`,\
`tipo_uapa`) VALUES (\
0,\
'Evento sin producto asociado',\
'Evento sin producto asociado',\
'Evento sin producto asociado');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
1,\
'Redes de conocimiento',\
'Redes de conocimiento',\
'Redes de conocimiento');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
2,\
'Producción bibliográfica - Trabajos en eventos (Capítulos de memoria) - Completo',\
'Capítulos de memoria',\
'Capítulos de memoria');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
3,\
'Producción técnica - Presentación de trabajo - Comunicación',\
'Presentación de trabajo',\
'Trabajo de Comunicación');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
4,\
'Demás trabajos - Demás trabajos - Póster',\
'Demás trabajos',\
'Poster');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
5,\
'Producción técnica - Presentación de trabajo - Conferencia',\
'Presentación de trabajo',\
'Conferencia');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
6,\
'Producción técnica - Presentación de trabajo - Ponencia',\
'Presentación de trabajo',\
'Ponencia');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
7,\
'Estrategias pedagógicas para el fomento a la CTI',\
'Estrategias pedagógicas',\
'Estrategias pedagógicas');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
8,\
'Producción bibliográfica - Artículo - Publicado en revista especializada',\
'Publicado en revista especializada',\
'Artículo');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
9,\
'Producción bibliográfica - Artículo - Corto (Resumen)',\
'Corto (Resumen)',\
'Artículo');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
10,\
'Estrategias pedagógicas para el fomento a la CTI',\
'Estrategias pedagógicas',\
'Estrategias pedagógicas');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
11,\
'Producción bibliográfica - Artículo - Caso clínico',\
'Caso Clínico',\
'Artículo');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
12,\
'Producción bibliográfica - Trabajos en eventos (Capítulos de memoria) - Resumen',\
'Capítulo de Memoria',\
'Resumen');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
13,\
'Producción técnica - Presentación de trabajo - Congreso',\
'Congreso',\
'Congreso');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
14,\
'Producción técnica - Presentación de trabajo - Simposio',\
'Simposio',\
'Simposio');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
15,\
'Producción técnica - Presentación de trabajo - Seminario',\
'Seminario',\
'Seminario');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
16,\
'Producción técnica - Presentación de trabajo - Otro',\
'Otro',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
17,\
'Producción bibliográfica - Libro - Libro resultado de investigación',\
'Libro resultado de investigación',\
'Libro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
18,\
'Producción bibliográfica - Libro - Otro libro publicado',\
'Otro libro publicado',\
'Libro - Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
19,\
'Producción bibliográfica - Libro - Libro pedagógico y/o de divulgación',\
'Libro pedagógico y/o de divulgación',\
'Libro - pedagógico');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
20,\
'Otro capítulo de libro publicado',\
'Otro capítulo de libro',\
'Capítulo de libro - Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
21,\
'Capítulo de libro',\
'Capítulo de libro',\
'Capítulo de libro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
22,\
'Producción bibliográfica - Otro artículo publicado - Periódico de noticias',\
'Periódico de noticias',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
23,\
'Producción bibliográfica - Otro artículo publicado - Revista de divulgación',\
'Revista de divulgación',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
24,\
'Producción bibliográfica - Otro artículo publicado - Cartas al editor',\
'Cartas al editor',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
25,\
'Producción bibliográfica - Otro artículo publicado - Reseñas de libros',\
'Reseñas de libros',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
26,\
'Producción bibliográfica - Otro artículo publicado - Columna de opinión',\
'Columnas de opinión',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
27,\
'Producción bibliográfica - Documento de trabajo (Working Paper)',\
'Documento de trabajo (Working Paper)',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
28,\
'Producción bibliográfica - Traducciones - Artículo',\
'Traducciones - Artículo',\
'Traducciones');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
29,\
'Producción bibliográfica - Traducciones - Libro',\
'Traducciones - Libro',\
'Traducciones');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
30,\
'Producción bibliográfica - Traducciones - Otra',\
'Traducciones - Otra',\
'Traducciones');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
31,\
'Producción bibliográfica - Otra producción bibliográfica - Introducción',\
'Introducción',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
32,\
'Producción bibliográfica - Otra producción bibliográfica - Prólogo',\
'Prólogo',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
33,\
'Producción bibliográfica - Otra producción bibliográfica - Epílogo',\
'Epílogo',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
34,\
'Producción bibliográfica - Otra producción bibliográfica - Otra',\
'Otra',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
35,\
'Producción técnica - Softwares - Computacional',\
'Software',\
'Software');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
36,\
'Producción técnica - Productos tecnológicos - Gen Clonado',\
'Productos tecnológicos - Gen Clonado',\
'Productos tecnológicos');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
37,\
'Producción técnica - Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada',\
'Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada',\
'Productos tecnológicos');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
38,\
'Producción técnica - Productos tecnológicos - Otro',\
'Productos tecnológicos - Otro',\
'Productos tecnológicos');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
39,\
'Producción técnica - Productos tecnológicos - Base de datos de referencia para investigación',\
'Productos tecnológicos - Base de datos de referencia para investigación',\
'Productos tecnológicos');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
40,\
'Producción técnica - Diseño Industrial',\
'Diseño Industrial',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
41,\
'Producción técnica - Esquema de circuito integrado',\
'Esquema de circuito integrado',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
42,\
'Producción técnica - Innovaciones generadas de producción empresarial - Organizacional',\
'Innovaciones generadas de producción empresarial - Organizacional',\
'Innovaciones');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
43,\
'Producción técnica - Innovaciones generadas de producción empresarial - Empresarial',\
'Innovaciones generadas de producción empresarial - Empresarial',\
'Innovaciones');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
44,\
'Producción técnica - Variedad animal',\
'Variedad animal',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
45,\
'Producción técnica - Innovación de proceso o procedimiento',\
'Innovación de proceso o procedimiento',\
'Innovación');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
46,\
'Producción técnica - Cartas, mapas o similares - Aerofotograma',\
'Aerofotograma',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
47,\
'Producción técnica - Cartas, mapas o similares - Carta',\
'Carta',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
48,\
'Producción técnica - Cartas, mapas o similares - Fotograma',\
'Fotograma',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
49,\
'Producción técnica - Cartas, mapas o similares - Mapa',\
'Mapa',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
50,\
'Producción técnica - Cartas, mapas o similares - Otra',\
'Otra',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
51,\
'Producción técnica - Variedad vegetal',\
'Variedad vegetal',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
52,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Servicios de proyectos de IDI',\
'Servicios de proyectos de IDI',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
53,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Comercialización de tecnología',\
'Comercialización de tecnología',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
54,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Análisis de competitividad',\
'Análisis de competitividad',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
55,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Informe técnico',\
'Informe técnico',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
56,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Otro',\
'Otro',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
57,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Acciones de transferencia tecnológica',\
'Acciones de transferencia tecnológica',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
58,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Desarrollo de productos',\
'Desarrollo de productos',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
59,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Implementación de sistemas de análisis',\
'Implementación de sistemas de análisis',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
60,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Consultoría en artes,arquitectura y diseño',\
'Consultoría en artes,arquitectura y diseño',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
61,\
'Producción técnica - Regulación, norma, reglamento o legislación - Ambiental o de Salud',\
'Regulación, norma, reglamento o legislación - Ambiental o de Salud',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
62,\
'Producción técnica - Regulación, norma, reglamento o legislación - Educativa',\
'Regulación, norma, reglamento o legislación - Educativa',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
63,\
'Producción técnica - Regulación, norma, reglamento o legislación - Social',\
'Regulación, norma, reglamento o legislación - Social',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
64,\
'Producción técnica - Regulación, norma, reglamento o legislación - Técnica',\
'Regulación, norma, reglamento o legislación - Técnica',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
65,\
'Producción técnica - Regulación, norma, reglamento o legislación - Guía de práctica clínica',\
'Regulación, norma, reglamento o legislación - Guía de práctica clínica',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
66,\
'Producción técnica - Regulación, norma, reglamento o legislación - Proyecto de ley',\
'Regulación, norma, reglamento o legislación - Proyecto de ley',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
67,\
'Producción técnica - Reglamento Técnico',\
'Reglamento Técnico',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
68,\
'Producción técnica - Empresa de base tecnológica - Spin-off',\
'Empresa de base tecnológica - Spin-off',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
69,\
'Producción técnica - Empresa de base tecnológica - Start-up',\
'Empresa de base tecnológica - Start-up',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
70,\
'Demás trabajos - Demás trabajos',\
'Demás trabajos',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
71,\
'Producción técnica - Signos',\
'Signos',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
72,\
'Producción técnica - Softwares - Multimedia',\
'Multimedia',\
'Software');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
73,\
'Producción técnica - Softwares - Otra',\
'Softwares - Otra',\
'Software');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
74,\
'Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Básica',\
'Técnica - Básica',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
75,\
'Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Ensayo',\
'Técnica - Ensayo',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
76,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Servicios de Proyectos de I+D+I',\
'Servicios de Proyectos de I+D+I',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
77,\
'Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Proceso',\
'Técnica - Proceso',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
78,\
'Datos complementarios - Participación en comités de evaluación - Profesor titular',\
'Participación en comités de evaluación - Profesor titular',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
79,\
'Datos complementarios - Participación en comités de evaluación - Concurso docente',\
'Participación en comités de evaluación - Concurso docente',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
80,\
'Datos complementarios - Participación en comités de evaluación - Jefe de cátedra',\
'articipación en comités de evaluación - Jefe de cátedra',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
81,\
'Datos complementarios - Participación en comités de evaluación - Evaluación de cursos',\
'Participación en comités de evaluación - Evaluación de cursos',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
82,\
'Datos complementarios - Participación en comités de evaluación - Acreditación de programas',\
'Participación en comités de evaluación - Acreditación de programas',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
83,\
'Datos complementarios - Participación en comités de evaluación - Asignación de becas',\
'Participación en comités de evaluación - Asignación de becas',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
84,\
'Datos complementarios - Participación en comités de evaluación - Otra',\
'Participación en comités de evaluación - Otra',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
85,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Pregrado',\
'Jurado Pregrado',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
86,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Especialización',\
'Jurado Especialización',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
87,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Especialidad Médica',\
'Jurado Especialidad Médica',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
88,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Maestría',\
'Jurado Maestría',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
89,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Doctorado',\
'Jurado Doctorado',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
90, \
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Otra',\
'Jurado Otra',\
'Comités');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
92, \
'Producción técnica - Prototipo - Servicios',\
'Prototipo - Servicios',\
'Servicios');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
93, \
'Producción técnica - Plantas piloto - Planta piloto',\
'Plantas piloto - Planta piloto',\
'Planta piloto');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
94, \
'Producción técnica - Prototipo - Industrial',\
'Prototipo - Industrial',\
'Industrial');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
95, \
'Producción técnica - Signos Distintivos - Marcas',\
'Signos Distintivos - Marcas',\
'Marcas');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
96, \
'Producción técnica - Signos Distintivos - Nombres comerciales',\
'Signos Distintivos - Nombres comerciales',\
'Nombres comerciales');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
97, \
'Apropiación - Eventos Cientificos - Otro',\
'Eventos Cientificos -  Otro',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
98, \
'Apropiación - Eventos Cientificos - Taller',\
'Eventos Cientificos -  Taller',\
'Taller');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
99, \
'Apropiación - Eventos Cientificos - Congreso',\
'Eventos Cientificos -  Congreso',\
'Congreso');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
100, \
'Apropiación - Eventos Cientificos - Encuentro',\
'Eventos Cientificos -  Encuentro',\
'Encuentro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
101, \
'Apropiación - Eventos Cientificos - Seminario',\
'Eventos Cientificos -  Seminario',\
'Seminario');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
102, \
'Apropiación - Eventos Cientificos - Simposio',\
'Eventos Cientificos -  Simposio',\
'Simposio');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
103, \
'Apropiación - Eventos Cientificos - Informes de investigación',\
'Eventos Cientificos -  Informes de investigación',\
'Informes de investigación');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
104, \
'Apropiación - Impresos - Manual',\
'Impresos - Manual',\
'Manual');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
105, \
'Apropiación - Impresos - Boletín',\
'Impresos - Boletín',\
'Boletín');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
106, \
'Apropiación - Contenido Multimedia - Comentario',\
'Contenido Multimedia - Comentario',\
'Comentario');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
107, \
'Apropiación - Contenido Multimedia - Entrevista',\
'Contenido Multimedia - Entrevista',\
'Entrevista');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
108, \
'Apropiación - Contenido Virtual - Página Web',\
'Contenido Virtual - Página Web',\
'Página Web');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
109, \
'Apropiación - Estrategias de Comunicación - Estrategias de Comunicación',\
'Estrategias de Comunicación - Estrategias de Comunicación',\
'Estrategias de Comunicación');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
110, \
'Apropiación - Estrategias Pedagógicas - Estrategias Pedagógicas para el fomento a la CTI',\
'Estrategias Pedagógicas - Estrategias Pedagógicas para el fomento a la CTI',\
'Estrategias Pedagógicas para el fomento a la CTI');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
111, \
'Apropiación - Participación Ciudadana - Participación Ciudadana en Proyectos de CTI',\
'Participación Ciudadana - Participación Ciudadana en Proyectos de CTI',\
'Participación Ciudadana en Proyectos de CTI');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
112, \
'Apropiación - Participación Ciudadana - Espacios de Participación Ciudadana',\
'Participación Ciudadana - Espacios de Participación Ciudadana',\
'Espacios de Participación Ciudadana');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
113, \
'Producción en arte, arquitectura y diseño - Obras o productos - Obras o productos',\
'Obras o productos - Obras o productos',\
'Obras o productos');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
114, \
'Actividades de Formación - Actividades de Formación - Asesorías al Programa Ondas',\
'Actividades de Formación - Asesorías al Programa Ondas',\
'Asesorías al Programa Ondas');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
115, \
'Actividades de Formación - Curso de Corta Duración Dictados - Perfeccionamiento',\
'Curso de Corta Duración Dictados - Perfeccionamiento',\
'Perfeccionamiento');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
116, \
'Actividades de Formación - Curso de Corta Duración Dictados - Extensión Extracurricular',\
'Curso de Corta Duración Dictados - Extensión Extracurricular',\
'Extensión Extracurricular');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
117, \
'Actividades de Formación - Trabajos dirigidos/turorías - Monografía de conclusión de curso',\
'Trabajos dirigidos/turorías - Monografía de conclusión de curso',\
'Monografía de conclusión de curso');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
118, \
'Actividades de Formación - Curso de Corta Duración Dictados - Otro',\
'Curso de Corta Duración Dictados - Otro',\
'Otro');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
119, \
'Proyectos - Investigación, desarrollo e innovación - Proyectos',\
'Investigación, desarrollo e innovación - Proyectos',\
'Proyectos');\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`) VALUES (\
91, \
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Curso de perfeccionamiento/especialización',\
'Jurado Especial',\
'Comités');\n"]

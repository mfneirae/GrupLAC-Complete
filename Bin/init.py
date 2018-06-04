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
    global GP_ACTIVIDADES_FORM
    global GP_ACTIVIDADES_FORM_CSV

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
    GP_ACTIVIDADES_FORM = []

    GP_PROD_BIB_CSV=["CODGP_PROD; \
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

    GP_PROD_TEC_CSV=["CODGP_PROD; \
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

    GP_APROPIACION_CSV=["CODGP_PROD; \
Tipos de Participación; \
Fecha Inicio; \
Fecha Fin; \
Proyecto de Inv; \
Medio de publicación; \
Emisora; \
Número de Participantes; \
\n"]

    GP_OBRAS_CSV=["CODGP_PROD; \
Fecha Creación; \
Disiplina de origen; \
Institución Licencia; \
Fecha Licencia; \
Distinciones; \
Selección Distinción; \
Productos Asociados; \
Número Derechos Autor/NIT; \
\n"]

    GP_ACTIVIDADES_FORM_CSV=["CODGP_PROD; \
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
TIPO_UAPA; \
TIPO_PREGRADO; \
TIPO_POSGRADO\n\
0; \
Evento sin producto asociado; \
Evento sin producto asociado; \
Evento sin producto asociado; \
;\
;\n\
1; \
Redes de conocimiento; \
Redes de conocimiento; \
Redes de conocimiento; \
;\
;\n\
2; \
Producción bibliográfica - Trabajos en eventos (Capítulos de memoria) - Completo; \
Capítulos de memoria; \
Capítulos de memoria; \
;\
;\n\
3; \
Producción técnica - Presentación de trabajo - Comunicación; \
Presentación de trabajo; \
Trabajo de Comunicación; \
;\
;\n\
4; \
Demás trabajos - Demás trabajos - Póster; \
Demás trabajos; \
Poster; \
;\
;\n\
5; \
Producción técnica - Presentación de trabajo - Conferencia; \
Presentación de trabajo; \
Conferencia; \
;\
;\n\
6; \
Producción técnica - Presentación de trabajo - Ponencia; \
Presentación de trabajo; \
Ponencia; \
;\
;\n\
7; \
Estrategias pedagógicas para el fomento a la CTI; \
Estrategias pedagógicas; \
Estrategias pedagógicas; \
;\
;\n\
8; \
Producción bibliográfica - Artículo - Publicado en revista especializada; \
Publicado en revista especializada; \
Artículo; \
;\
;\n\
9; \
Producción bibliográfica - Artículo - Corto (Resumen); \
Corto (Resumen); \
Artículo; \
;\
;\n\
10; \
Estrategias pedagógicas para el fomento a la CTI; \
Estrategias pedagógicas; \
Estrategias pedagógicas; \
;\
;\n\
11; \
Producción bibliográfica - Artículo - Caso clínico; \
Caso Clínico; \
Artículo; \
;\
;\n\
12; \
Producción bibliográfica - Trabajos en eventos (Capítulos de memoria) - Resumen; \
Capítulo de Memoria; \
Resumen; \
;\
;\n\
13; \
Producción técnica - Presentación de trabajo - Congreso; \
Congreso; \
Congreso; \
;\
;\n\
14; \
Producción técnica - Presentación de trabajo - Simposio; \
Simposio; \
Simposio; \
;\
;\n\
15; \
Producción técnica - Presentación de trabajo - Seminario; \
Seminario; \
Seminario; \
;\
;\n\
16; \
Producción técnica - Presentación de trabajo - Otro; \
Otro; \
Otro; \
;\
;\n\
17; \
Producción bibliográfica - Libro - Libro resultado de investigación; \
Libro resultado de investigación; \
Libro; \
;\
;\n\
18; \
Producción bibliográfica - Libro - Otro libro publicado; \
Otro libro publicado; \
Libro - Otro; \
;\
;\n\
19; \
Producción bibliográfica - Libro - Libro pedagógico y/o de divulgación; \
Libro pedagógico y/o de divulgación; \
Libro - pedagógico; \
;\
;\n\
20; \
Otro capítulo de libro publicado; \
Otro capítulo de libro; \
Capítulo de libro - Otro; \
;\
;\n\
21; \
Capítulo de libro; \
Capítulo de libro; \
Capítulo de libro; \
;\
;\n\
22; \
Producción bibliográfica - Otro artículo publicado - Periódico de noticias; \
Periódico de noticias; \
Otro; \
;\
;\n\
23; \
Producción bibliográfica - Otro artículo publicado - Revista de divulgación; \
Revista de divulgación; \
Otro; \
;\
;\n\
24; \
Producción bibliográfica - Otro artículo publicado - Cartas al editor; \
Cartas al editor; \
Otro; \
;\
;\n\
25; \
Producción bibliográfica - Otro artículo publicado - Reseñas de libros; \
Reseñas de libros; \
Otro; \
;\
;\n\
26; \
Producción bibliográfica - Otro artículo publicado - Columna de opinión; \
Columnas de opinión; \
Otro; \
;\
;\n\
27; \
Producción bibliográfica - Documento de trabajo (Working Paper); \
Documento de trabajo (Working Paper); \
Otro; \
;\
;\n\
28; \
Producción bibliográfica - Traducciones - Artículo; \
Traducciones - Artículo; \
Traducciones; \
;\
;\n\
29; \
Producción bibliográfica - Traducciones - Libro; \
Traducciones - Libro; \
Traducciones; \
;\
;\n\
30; \
Producción bibliográfica - Traducciones - Otra; \
Traducciones - Otra; \
Traducciones; \
;\
;\n\
31; \
Producción bibliográfica - Otra producción bibliográfica - Introducción; \
Introducción; \
Otro; \
;\
;\n\
32; \
Producción bibliográfica - Otra producción bibliográfica - Prólogo; \
Prólogo; \
Otro; \
;\
;\n\
33; \
Producción bibliográfica - Otra producción bibliográfica - Epílogo; \
Epílogo; \
Otro; \
;\
;\n\
34; \
Producción bibliográfica - Otra producción bibliográfica - Otra; \
Otra; \
Otro; \
;\
;\n\
35; \
Producción técnica - Softwares - Computacional; \
Software; \
Software; \
;\
;\n\
36; \
Producción técnica - Productos tecnológicos - Gen Clonado; \
Productos tecnológicos - Gen Clonado; \
Productos tecnológicos; \
;\
;\n\
37; \
Producción técnica - Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada; \
Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada; \
Productos tecnológicos; \
;\
;\n\
38; \
Producción técnica - Productos tecnológicos - Otro; \
Productos tecnológicos - Otro; \
Productos tecnológicos; \
;\
;\n\
39; \
Producción técnica - Productos tecnológicos - Base de datos de referencia para investigación; \
Productos tecnológicos - Base de datos de referencia para investigación; \
Productos tecnológicos; \
;\
;\n\
40; \
Producción técnica - Diseño Industrial; \
Diseño Industrial; \
Otro; \
;\
;\n\
41; \
Producción técnica - Esquema de circuito integrado; \
Esquema de circuito integrado; \
Otro; \
;\
;\n\
42; \
Producción técnica - Innovaciones generadas de producción empresarial - Organizacional; \
Innovaciones generadas de producción empresarial - Organizacional; \
Innovaciones; \
;\
;\n\
43; \
Producción técnica - Innovaciones generadas de producción empresarial - Empresarial; \
Innovaciones generadas de producción empresarial - Empresarial; \
Innovaciones; \
;\
;\n\
44; \
Producción técnica - Variedad animal; \
Variedad animal; \
Otro; \
;\
;\n\
45; \
Producción técnica - Innovación de proceso o procedimiento; \
Innovación de proceso o procedimiento; \
Innovación; \
;\
;\n\
46; \
Producción técnica - Cartas, mapas o similares - Aerofotograma; \
Aerofotograma; \
Otro; \
;\
;\n\
47; \
Producción técnica - Cartas, mapas o similares - Carta; \
Carta; \
Otro; \
;\
;\n\
48; \
Producción técnica - Cartas, mapas o similares - Fotograma; \
Fotograma; \
Otro; \
;\
;\n\
49; \
Producción técnica - Cartas, mapas o similares - Mapa; \
Mapa; \
Otro; \
;\
;\n\
50; \
Producción técnica - Cartas, mapas o similares - Otra; \
Otra; \
Otro; \
;\
;\n\
51; \
Producción técnica - Variedad vegetal; \
Variedad vegetal; \
Otro; \
;\
;\n\
52; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Servicios de proyectos de IDI; \
Servicios de proyectos de IDI; \
Otro; \
;\
;\n\
53; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Comercialización de tecnología; \
Comercialización de tecnología; \
Otro; \
;\
;\n\
54; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Análisis de competitividad; \
Análisis de competitividad; \
Otro; \
;\
;\n\
55; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Informe técnico; \
Informe técnico; \
Otro; \
;\
;\n\
56; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Otro; \
Otro; \
Otro; \
;\
;\n\
57; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Acciones de transferencia tecnológica; \
Acciones de transferencia tecnológica; \
Otro; \
;\
;\n\
58; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Desarrollo de productos; \
Desarrollo de productos; \
Otro; \
;\
;\n\
59; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Implementación de sistemas de análisis; \
Implementación de sistemas de análisis; \
Otro; \
;\
;\n\
60; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Consultoría en artes,arquitectura y diseño; \
Consultoría en artes,arquitectura y diseño; \
Otro; \
;\
;\n\
61; \
Producción técnica - Regulación, norma, reglamento o legislación - Ambiental o de Salud; \
Regulación, norma, reglamento o legislación - Ambiental o de Salud; \
Otro; \
;\
;\n\
62; \
Producción técnica - Regulación, norma, reglamento o legislación - Educativa; \
Regulación, norma, reglamento o legislación - Educativa; \
Otro; \
;\
;\n\
63; \
Producción técnica - Regulación, norma, reglamento o legislación - Social; \
Regulación, norma, reglamento o legislación - Social; \
Otro; \
;\
;\n\
64; \
Producción técnica - Regulación, norma, reglamento o legislación - Técnica; \
Regulación, norma, reglamento o legislación - Técnica; \
Otro; \
;\
;\n\
65; \
Producción técnica - Regulación, norma, reglamento o legislación - Guía de práctica clínica; \
Regulación, norma, reglamento o legislación - Guía de práctica clínica; \
Otro; \
;\
;\n\
66; \
Producción técnica - Regulación, norma, reglamento o legislación - Proyecto de ley; \
Regulación, norma, reglamento o legislación - Proyecto de ley; \
Otro; \
;\
;\n\
67; \
Producción técnica - Reglamento Técnico; \
Reglamento Técnico; \
Otro; \
;\
;\n\
68; \
Producción técnica - Empresa de base tecnológica - Spin-off; \
Empresa de base tecnológica - Spin-off; \
Otro; \
;\
;\n\
69; \
Producción técnica - Empresa de base tecnológica - Start-up; \
Empresa de base tecnológica - Start-up; \
Otro; \
;\
;\n\
70; \
Demás trabajos - Demás trabajos; \
Demás trabajos; \
Otro; \
;\
;\n\
71; \
Producción técnica - Signos; \
Signos; \
Otro; \
;\
;\n\
72; \
Producción técnica - Softwares - Multimedia; \
Multimedia; \
Software; \
;\
;\n\
73; \
Producción técnica - Softwares - Otra; \
Softwares - Otra; \
Software; \
;\
;\n\
74; \
Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Básica; \
Técnica - Básica; \
Otro; \
;\
;\n\
75; \
Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Ensayo; \
Técnica - Ensayo; \
Otro; \
;\
;\n\
76; \
Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Servicios de Proyectos de I+D+I; \
Servicios de Proyectos de I+D+I; \
Otro; \
;\
;\n\
77; \
Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Proceso; \
Técnica - Proceso; \
Otro; \
;\
;\n\
78; \
Datos complementarios - Participación en comités de evaluación - Profesor titular; \
Participación en comités de evaluación - Profesor titular; \
Comités; \
;\
;\n\
79; \
Datos complementarios - Participación en comités de evaluación - Concurso docente; \
Participación en comités de evaluación - Concurso docente; \
Comités; \
;\
;\n\
80; \
Datos complementarios - Participación en comités de evaluación - Jefe de cátedra; \
Participación en comités de evaluación - Jefe de cátedra; \
Comités; \
;\
;\n\
81; \
Datos complementarios - Participación en comités de evaluación - Evaluación de cursos; \
Participación en comités de evaluación - Evaluación de cursos; \
Comités; \
;\
;\n\
82; \
Datos complementarios - Participación en comités de evaluación - Acreditación de programas; \
Participación en comités de evaluación - Acreditación de programas; \
Comités; \
;\
;\n\
83; \
Datos complementarios - Participación en comités de evaluación - Asignación de becas; \
Participación en comités de evaluación - Asignación de becas; \
Comités; \
;\
;\n\
84; \
Datos complementarios - Participación en comités de evaluación - Otra; \
Participación en comités de evaluación - Otra; \
Comités; \
;\
;\n\
85; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Pregrado; \
Jurado Pregrado; \
Comités; \
;\
;\n\
86; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Especialización; \
Jurado Especialización; \
Comités; \
;\
;\n\
87; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Especialidad Médica; \
Jurado Especialidad Médica; \
Comités; \
;\
;\n\
88; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Maestría; \
Jurado Maestría; \
Comités; \
;\
;\n\
89; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Doctorado; \
Jurado Doctorado; \
Comités; \
;\
;\n\
90; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Otra; \
Jurado Otra; \
Comités; \
;\
;\n\
91; \
Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Curso de perfeccionamiento/especialización; \
Jurado Especializaciones; \
Comités; \
;\
;\n"]

#***************************************************************************
#Insert
#***************************************************************************
    inv_colciencias_tipo_producto = [ "REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`cod_tipo_producto`,\
`tipo_producto_col`,\
`sub_tipo_producto_col`,\
`tipo_uapa`,\
`tipo_pregrado`,\
`tipo_posgrado`) VALUES (\
0,\
'Evento sin producto asociado',\
'Evento sin producto asociado',\
'Evento sin producto asociado',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
1,\
'Redes de conocimiento',\
'Redes de conocimiento',\
'Redes de conocimiento',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
2,\
'Producción bibliográfica - Trabajos en eventos (Capítulos de memoria) - Completo',\
'Capítulos de memoria',\
'Capítulos de memoria',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
3,\
'Producción técnica - Presentación de trabajo - Comunicación',\
'Presentación de trabajo',\
'Trabajo de Comunicación',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
4,\
'Demás trabajos - Demás trabajos - Póster',\
'Demás trabajos',\
'Poster',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
5,\
'Producción técnica - Presentación de trabajo - Conferencia',\
'Presentación de trabajo',\
'Conferencia',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
6,\
'Producción técnica - Presentación de trabajo - Ponencia',\
'Presentación de trabajo',\
'Ponencia',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
7,\
'Estrategias pedagógicas para el fomento a la CTI',\
'Estrategias pedagógicas',\
'Estrategias pedagógicas',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
8,\
'Producción bibliográfica - Artículo - Publicado en revista especializada',\
'Publicado en revista especializada',\
'Artículo',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
9,\
'Producción bibliográfica - Artículo - Corto (Resumen)',\
'Corto (Resumen)',\
'Artículo',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
10,\
'Estrategias pedagógicas para el fomento a la CTI',\
'Estrategias pedagógicas',\
'Estrategias pedagógicas',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
11,\
'Producción bibliográfica - Artículo - Caso clínico',\
'Caso Clínico',\
'Artículo',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
12,\
'Producción bibliográfica - Trabajos en eventos (Capítulos de memoria) - Resumen',\
'Capítulo de Memoria',\
'Resumen',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
13,\
'Producción técnica - Presentación de trabajo - Congreso',\
'Congreso',\
'Congreso',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
14,\
'Producción técnica - Presentación de trabajo - Simposio',\
'Simposio',\
'Simposio',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
15,\
'Producción técnica - Presentación de trabajo - Seminario',\
'Seminario',\
'Seminario',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
16,\
'Producción técnica - Presentación de trabajo - Otro',\
'Otro',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
17,\
'Producción bibliográfica - Libro - Libro resultado de investigación',\
'Libro resultado de investigación',\
'Libro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
18,\
'Producción bibliográfica - Libro - Otro libro publicado',\
'Otro libro publicado',\
'Libro - Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
19,\
'Producción bibliográfica - Libro - Libro pedagógico y/o de divulgación',\
'Libro pedagógico y/o de divulgación',\
'Libro - pedagógico',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
20,\
'Otro capítulo de libro publicado',\
'Otro capítulo de libro',\
'Capítulo de libro - Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
21,\
'Capítulo de libro',\
'Capítulo de libro',\
'Capítulo de libro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
22,\
'Producción bibliográfica - Otro artículo publicado - Periódico de noticias',\
'Periódico de noticias',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
23,\
'Producción bibliográfica - Otro artículo publicado - Revista de divulgación',\
'Revista de divulgación',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
24,\
'Producción bibliográfica - Otro artículo publicado - Cartas al editor',\
'Cartas al editor',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
25,\
'Producción bibliográfica - Otro artículo publicado - Reseñas de libros',\
'Reseñas de libros',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
26,\
'Producción bibliográfica - Otro artículo publicado - Columna de opinión',\
'Columnas de opinión',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
27,\
'Producción bibliográfica - Documento de trabajo (Working Paper)',\
'Documento de trabajo (Working Paper)',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
28,\
'Producción bibliográfica - Traducciones - Artículo',\
'Traducciones - Artículo',\
'Traducciones',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
29,\
'Producción bibliográfica - Traducciones - Libro',\
'Traducciones - Libro',\
'Traducciones',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
30,\
'Producción bibliográfica - Traducciones - Otra',\
'Traducciones - Otra',\
'Traducciones',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
31,\
'Producción bibliográfica - Otra producción bibliográfica - Introducción',\
'Introducción',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
32,\
'Producción bibliográfica - Otra producción bibliográfica - Prólogo',\
'Prólogo',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
33,\
'Producción bibliográfica - Otra producción bibliográfica - Epílogo',\
'Epílogo',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
34,\
'Producción bibliográfica - Otra producción bibliográfica - Otra',\
'Otra',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
35,\
'Producción técnica - Softwares - Computacional',\
'Software',\
'Software',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
36,\
'Producción técnica - Productos tecnológicos - Gen Clonado',\
'Productos tecnológicos - Gen Clonado',\
'Productos tecnológicos',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
37,\
'Producción técnica - Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada',\
'Productos tecnológicos - Coleccion biologica de referencia con informacion sistematizada',\
'Productos tecnológicos',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
38,\
'Producción técnica - Productos tecnológicos - Otro',\
'Productos tecnológicos - Otro',\
'Productos tecnológicos',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
39,\
'Producción técnica - Productos tecnológicos - Base de datos de referencia para investigación',\
'Productos tecnológicos - Base de datos de referencia para investigación',\
'Productos tecnológicos',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
40,\
'Producción técnica - Diseño Industrial',\
'Diseño Industrial',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
41,\
'Producción técnica - Esquema de circuito integrado',\
'Esquema de circuito integrado',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
42,\
'Producción técnica - Innovaciones generadas de producción empresarial - Organizacional',\
'Innovaciones generadas de producción empresarial - Organizacional',\
'Innovaciones',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
43,\
'Producción técnica - Innovaciones generadas de producción empresarial - Empresarial',\
'Innovaciones generadas de producción empresarial - Empresarial',\
'Innovaciones',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
44,\
'Producción técnica - Variedad animal',\
'Variedad animal',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
45,\
'Producción técnica - Innovación de proceso o procedimiento',\
'Innovación de proceso o procedimiento',\
'Innovación',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
46,\
'Producción técnica - Cartas, mapas o similares - Aerofotograma',\
'Aerofotograma',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
47,\
'Producción técnica - Cartas, mapas o similares - Carta',\
'Carta',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
48,\
'Producción técnica - Cartas, mapas o similares - Fotograma',\
'Fotograma',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
49,\
'Producción técnica - Cartas, mapas o similares - Mapa',\
'Mapa',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
50,\
'Producción técnica - Cartas, mapas o similares - Otra',\
'Otra',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
51,\
'Producción técnica - Variedad vegetal',\
'Variedad vegetal',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
52,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Servicios de proyectos de IDI',\
'Servicios de proyectos de IDI',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
53,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Comercialización de tecnología',\
'Comercialización de tecnología',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
54,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Análisis de competitividad',\
'Análisis de competitividad',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
55,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Informe técnico',\
'Informe técnico',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
56,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Otro',\
'Otro',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
57,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Acciones de transferencia tecnológica',\
'Acciones de transferencia tecnológica',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
58,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Desarrollo de productos',\
'Desarrollo de productos',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
59,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Implementación de sistemas de análisis',\
'Implementación de sistemas de análisis',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
60,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Consultoría en artes,arquitectura y diseño',\
'Consultoría en artes,arquitectura y diseño',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
61,\
'Producción técnica - Regulación, norma, reglamento o legislación - Ambiental o de Salud',\
'Regulación, norma, reglamento o legislación - Ambiental o de Salud',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
62,\
'Producción técnica - Regulación, norma, reglamento o legislación - Educativa',\
'Regulación, norma, reglamento o legislación - Educativa',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
63,\
'Producción técnica - Regulación, norma, reglamento o legislación - Social',\
'Regulación, norma, reglamento o legislación - Social',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
64,\
'Producción técnica - Regulación, norma, reglamento o legislación - Técnica',\
'Regulación, norma, reglamento o legislación - Técnica',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
65,\
'Producción técnica - Regulación, norma, reglamento o legislación - Guía de práctica clínica',\
'Regulación, norma, reglamento o legislación - Guía de práctica clínica',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
66,\
'Producción técnica - Regulación, norma, reglamento o legislación - Proyecto de ley',\
'Regulación, norma, reglamento o legislación - Proyecto de ley',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
67,\
'Producción técnica - Reglamento Técnico',\
'Reglamento Técnico',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
68,\
'Producción técnica - Empresa de base tecnológica - Spin-off',\
'Empresa de base tecnológica - Spin-off',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
69,\
'Producción técnica - Empresa de base tecnológica - Start-up',\
'Empresa de base tecnológica - Start-up',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
70,\
'Demás trabajos - Demás trabajos',\
'Demás trabajos',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
71,\
'Producción técnica - Signos',\
'Signos',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
72,\
'Producción técnica - Softwares - Multimedia',\
'Multimedia',\
'Software',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
73,\
'Producción técnica - Softwares - Otra',\
'Softwares - Otra',\
'Software',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
74,\
'Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Básica',\
'Técnica - Básica',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
75,\
'Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Ensayo',\
'Técnica - Ensayo',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
76,\
'Producción técnica - Consultoría Científico Tecnológica e Informe Técnico - Servicios de Proyectos de I+D+I',\
'Servicios de Proyectos de I+D+I',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
77,\
'Producción técnica - Regulación, norma, reglamento o legislación - Técnica - Proceso',\
'Técnica - Proceso',\
'Otro',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
78,\
'Datos complementarios - Participación en comités de evaluación - Profesor titular',\
'Participación en comités de evaluación - Profesor titular',\
'Comités',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
79,\
'Datos complementarios - Participación en comités de evaluación - Concurso docente',\
'Participación en comités de evaluación - Concurso docente',\
'Comités',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
80,\
'Datos complementarios - Participación en comités de evaluación - Jefe de cátedra',\
'articipación en comités de evaluación - Jefe de cátedra',\
'Comités',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
81,\
'Datos complementarios - Participación en comités de evaluación - Evaluación de cursos',\
'Participación en comités de evaluación - Evaluación de cursos',\
'Comités',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
82,\
'Datos complementarios - Participación en comités de evaluación - Acreditación de programas',\
'Participación en comités de evaluación - Acreditación de programas',\
'Comités',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
83,\
'Datos complementarios - Participación en comités de evaluación - Asignación de becas',\
'Participación en comités de evaluación - Asignación de becas',\
'Comités',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
84,\
'Datos complementarios - Participación en comités de evaluación - Otra',\
'Participación en comités de evaluación - Otra',\
'Comités',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
85,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Pregrado',\
'Jurado Pregrado',\
'Comités',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
86,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Especialización',\
'Jurado Especialización',\
'Comités',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
87,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Especialidad Médica',\
'Jurado Especialidad Médica',\
'Comités',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
88,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Maestría',\
'Jurado Maestría',\
'Comités',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
89,\
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Doctorado',\
'Jurado Doctorado',\
'Comités',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
90, \
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Otra',\
'Jurado Otra',\
'Comités',\
null,\
null);\n\
REPLACE INTO `uapa_db`.`v_colciencias_tipo_producto` ( \
`COD_TIPO_PRODUCTO`,\
`TIPO_PRODUCTO_COL`,\
`SUB_TIPO_PRODUCTO_COL`,\
`TIPO_UAPA`,\
`TIPO_PREGRADO`,\
`TIPO_POSGRADO`) VALUES (\
91, \
'Datos complementarios - Jurado/Comisiones evaluadoras de trabajo de grado - Curso de perfeccionamiento/especialización',\
'Jurado Especial',\
'Comités',\
null,\
null);\n"]

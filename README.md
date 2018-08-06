<!--

#############################################################################
        Copyright (c) 2018 by Manuel Embus. All Rights Reserved.

            This work is licensed under a Creative Commons
      Attribution - NonCommercial - ShareAlike 4.0
      International License.

      For more information write me to jai@mfneirae.com
      Or visit my webpage at https://mfneirae.com/
#############################################################################

 -->
# GrupLAC to BD - UAPA - UNAL

This project corresponds to an open source tool to webscraping GrupLAC - Colciencias Page with self-assessment and accreditation purpuses.

The entire project is associated to the
[Unidad de Apoyo a Procesos de Autoevaluación y Acreditación](http://ingenieria.unal.edu.co/dependencias/vicedecanatura-academica/autoevaluacion) of the [Universidad Nacional de Colombia](http://unal.edu.co/).


## Instructions
1. Requirements:
  * Windows 8 or higher / Ubuntu 14 or higher.
  * Python 3.6.
  * Internet Access.
  * Any Text Editor (I used Atom 3).
2. Install:
  * Copy this repository to your machine.
  * install bs4
  ```
    pip install bs4
  ```  
  * install openpyxl
  ```
    pip install openpyxl
  ```  
3. Usage:
  * Locate the list of GrupLAC that you want to use and place it in the file \Input\Base.xslx in this way:
      * COD_UAPA
      * COD_HERMES
      * COD_COLCIENCIAS
      * Nombre_GI
      * DNI_Lider
      * GrupLAC

  * Save the file and open bash or a command prompt (terminal if you are on Linux OS)
  * Run:
  ```
    python main.py
  ```  
  * That is all, now you can get all your data stored in the \Resultados folder.

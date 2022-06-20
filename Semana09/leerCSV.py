# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 09:48:26 2022
@author: Andres Vera
"""

#Para este ejercicio, se necesita descargar el archivo csv
#del siguiente link https://www.google.com/covid19/mobility/

#Importamos librerias basicas para leer archivos csv
import csv

#Abrimos archivo, indicando el PATH y enconding
with open('Global_Mobility_Report.csv', encoding="utf8") as f:
    datos = csv.reader(f,delimiter=',')
    for fila in datos:
        if fila[0]=="PE" and fila[2]=="Puno":
            print(f"{fila[0]}\t{fila[1]}\t{fila[2]}\t{fila[3]}\t"
                  f"{fila[4]}\t{fila[5]}\t{fila[6]}\t{fila[7]}\t"
                  f"{fila[8]}\t{fila[9]}\t{fila[10]}\t")
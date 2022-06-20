# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:45:50 2022

@author: Andres Vera
"""

archivo = open("archivo_de_prueba.txt","wt")
contenido = "Linea1 hola amigos como estan\nLinea2 Bienvenidos."
archivo.write(contenido)
archivo.close()

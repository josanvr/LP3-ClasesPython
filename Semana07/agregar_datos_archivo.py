# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:47:49 2022
@author: Andres Vera
"""

archivo = open("noticia.txt","at")
#\n agrega el contenido en una linea al final
contenido ="\nFuente:RPP"

archivo.write(contenido)
archivo.close()
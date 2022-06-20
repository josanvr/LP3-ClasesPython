# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 09:26:21 2022
@author: Andres Vera
"""

noticia = open("noticia.txt", "rt", encoding='utf-8-sig')
datos_noticia = noticia.read()
lista = datos_noticia.split()
print(datos_noticia)
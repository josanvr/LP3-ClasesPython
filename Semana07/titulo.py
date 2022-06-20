# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:03:49 2022
@author: Andres Vera
"""

"""
Problema1: tenemos una cadena y se desea que se muestre en formato de titulo.
"""

import camelcase


nombre = "jose andres vera rodriguez"
print(nombre.upper())
print(nombre.title())

"""
Si pidiera que no se muestre en formato titulo todo, necesitamos utilizar un
modulo(libreria) llamada camelcase

en consola:  pip install camelcase
"""

#Creamos objeto cam
cam = camelcase.CamelCase()
print("Con camelcase....")

#Imprimimos el nombre en formato titulo
print(cam.hump(nombre))

#Imprimimos el nombre en formato titulo, definiendo algunas que no
cam2 = camelcase.CamelCase('jose','vera')
print(cam2.hump(nombre))
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 09:05:11 2022
@author: Andres Vera
"""

import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")

consulta = """INSERT INTO pais(nombre, estado)
                VALUES('ARGENTINA','A')
            """
            
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()

conexion.close()
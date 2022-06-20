# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:36:34 2022
@author: Andres Vera
"""

import sqlite3

conexion=sqlite3.connect("bdbiblioteca.db")
cursor=conexion.cursor()

consulta =""" UPDATE editorial
                SET
                    nombre = 'Editorial Imprenta Unión'
                WHERE
                    ideditorial = 1
          """
          
cursor= conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()
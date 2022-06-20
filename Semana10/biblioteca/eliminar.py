# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:27:15 2022
@author: Andres Vera
"""

import sqlite3

conexion=sqlite3.connect("bdbiblioteca.db")
cursor=conexion.cursor()

consulta =""" DELETE FROM editorial
                WHERE
                    ideditorial = 5
          """
          
cursor= conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 08:59:01 2022

@author: Andres Vera
"""
#Dado el total, calcular IGV y subtotal
import financieros

total = 1000.49
print(f"Subtotal: {financieros.obtenerSubtotalconTotal(total): .2f}")
print(f"IGV: {financieros.obtenerIGVconTotal(total): .2f}")
print(f"Total: {total}")


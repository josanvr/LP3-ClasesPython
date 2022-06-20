# -*- coding: utf-8 -*-

"""
Created on Mon May 30 08:59:01 2022

@author: Andres Vera
"""
#Dado el suhtotal, calcular IGV y Total

import financieros

subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVconSubtotal(subtotal): .2f}")
print(f"Total: {financieros.obtenerTotalconSubtotal(subtotal): .2f}")
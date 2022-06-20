# -*- coding: utf-8 -*-
"""
Created on Mon May 30 08:59:01 2022

@author: Andres Vera
"""
"""

Tema 7: MODULOS
Los modulos permiten crear librerias de funcionalidades que 
puedas utilizar o reutilizar en cualquier momento en un proyecto
"""
igv = 0.18

def obtenerIGVconSubtotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    # subtotal + igv * subtotal
    # subtotal * (1+0.18)
    return subtotal*(1+igv)

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)
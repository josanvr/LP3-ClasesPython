# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 09:26:41 2022
@author: Andres Vera
"""

try:
    numerador = float(input("Numerador: "))
    denominador = float(input("Denominador: "))
    resultado = numerador/denominador
    print(f"\nResultado = {resultado}")
except ZeroDivisionError:
    print("\nNo puedes dividir entre 0 (CERO) ...")
except:
    print("\nHubo un error...")
else:
    print("\nLa división se realizó correctamente...")
finally:
    print("\n*****La operación terminó*****")

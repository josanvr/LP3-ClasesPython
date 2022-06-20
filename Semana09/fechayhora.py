# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 09:23:04 2022
@author: Andres Vera
"""

from datetime import datetime

fechayhora = datetime.now()

print(f"Hoy: {fechayhora}")

print(fechayhora.year)
print(fechayhora.month)
print(fechayhora.day)
print(fechayhora.hour)
print(fechayhora.minute)
print(fechayhora.second)
print(fechayhora.microsecond)
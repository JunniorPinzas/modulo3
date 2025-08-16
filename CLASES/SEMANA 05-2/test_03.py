""" USO DE LIBRERÍA DE FECHA Y TIEMPO"""
from datetime import datetime
fecha_1=datetime(2025,8,25)
fecha_2=datetime(2025,8,28)

if fecha_1>fecha_2:
    print("El niño 2 es mayor que el niño 1")
elif fecha_1==fecha_2:
    print("Los niños nacieron el mismo día")
else:
    print("El niño 1 es mayor que el niño 2")
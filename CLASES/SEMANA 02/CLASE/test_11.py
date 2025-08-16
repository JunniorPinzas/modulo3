"""
Operadores comunes
Operador suma
"""

var_1 = "7000"
var_2 = 35000
var_3 = 40.85

suma_1 = var_1 + str(var_2)
print(suma_1)

nombre = "Carmen"
apellido = "Gutierrez"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

print("________________________________")
suma_2 = int(var_1) + var_2
print(suma_2)

print("________________________________")
suma_3 = var_2 + var_3
print(suma_3)

print("_______________________________")
suma_4 = var_1 + str(var_2) + str(var_3)
print("El valor de mi suma_4 es: {}".format(suma_4))
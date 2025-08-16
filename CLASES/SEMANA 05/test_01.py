#Error por división entre 0
# x=500/0

#Error que no se puede sumar números más strings
# suma=100+"Hola"


#Manejo de errores
#Estructura y uso
"""
try:
    camino exitoso
    bloque de código 1
except 'Excepción 1:
    bloque de código 2
else:
    bloque de código 3
"""

def division(a,b):
    try:
        resultado=a/b
        print("El resultado es válido")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    else:print("Resultado: {}".format(resultado))

# division(100,0)
division(40,5)
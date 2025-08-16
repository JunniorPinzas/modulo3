# Nombres y apellidos: Oliver Junnior Pinzas Ayala


# 1. Crear 2 variables enteras, 2 variables flotantes, 2 variable string, 1 variables string con contenido netamente
# numérico y una variable boolean
print(
    """Mis variables creadas son la siguientes:
x1 = 25
x2 = 69
x3 = 36.97361
x4 = 750.458
x5 = "Junnior"
x6 = "Pinzas"
x7 = "123456789"
x8 =True""")
x1 = 25
x2 = 69
x3 = 36.97361
x4 = 750.458
x5 = "Junnior"
x6 = "Pinzas"
x7 = "123456789"
x8 =True

print("")
# 2. Obtener y mostrar la suma de una variable entera con la variable string numérica
# (Conversiones, realizarla si fuera necesario)

#Conversión de la variable str a int
x9 = int(x7)
#Determinación de la variable que guarda la suma de enteros
x10 = x9 + x1
print("La suma de una variable entera x1 y la variable x7 transformada en entera es",x10)

print("")
# 3. Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica y la variable flotantes
x11 = x1 + x2 + x9 + x3 +x4
print("La suma de las 2 variables enteras (x1 y x2) más la variable string numérica transformada (x7) y la variable flotantes (x3 y x4) es",x11)

print("")
# 4. Obtener y mostrar el módulo de las variables enteras: %
x12 = x2 % x1
print("El módulo de las variables enteras x2 y x1 es",x12)

print("")
# 5. Obtener y mostrar el resultado o la parte entera de las 2 variables int: //
x13 = x2 // x1
print("La parte entera de la división de las 2 variables enteras (x2 y x1) es",x13)

print("")
# 6. Obtener una potencia usando una de las variables flotantes como base y la variable entera como potencia
x14 = pow(x3,x1)
print("El resultado de la potencia que tiene como base a x3 y exponente a x1 es",x14)
cadena="Mi mamá me mima"

#Convertir a mayúsculas todas las letras
x=cadena.upper()
print(x)

#Convertir a minúsculas todas lasletras
y=x.lower()
print(y)

#Convertir cada primera letra de cada palabra a mayúscula
z=cadena.title()
print(z)

#Reemplazar los valores
print(cadena.replace("mamá","papá"))
print(cadena.replace(cadena[:7],"Mi tía"))

# RECORDANDO
#Para saber cuáles son las funciones que tienen los strings puedo usar el comando dir, y recordar que todas las funciones
# aplicables al stirng serán las que no llevan _
# print(dir(cadena))
#Para saber que implica o significa cada función, puedo ayudarme de la función help y el comando de interés SIN PARÉNTESIS
# print(help(cadena.lstrip))
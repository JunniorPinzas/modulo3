from statistics import median

x1=12.56
x2=34.78
x3=62.10
x4=29.98
x5=95.65
lista=[x1,x2,x3,x4,x5]
suma=sum(lista)
cant=len(lista)
media=suma/cant
print("El promedio de las variables elegidas es {}".format(media))
print("media: es el promedio de las variables y es de tipo: {}".format(type(media)))

#print("La media de 5 variables seleccionadas es {}".format(media))
#print("El tipo de variable de la media es {}".format(type(media)))
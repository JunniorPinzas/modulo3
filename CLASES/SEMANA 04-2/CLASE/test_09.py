#Forma de escribir para strings

x=input("Ingrese nombre: ")
y=input("Ingrese ciudad: ")

print("Usted se llama {nombre} y es de {ciudad}".format(nombre=x,ciudad=y))

#Lo que me permite este tipo de estructuración para mostrar string es PODER ESCRIBIR SIN UN ORDEN ESTABLECIDO
#La forma es definir variables dentro de los corchetes, y en la parte de format igualar esas variables a las que tienen datos guaradados
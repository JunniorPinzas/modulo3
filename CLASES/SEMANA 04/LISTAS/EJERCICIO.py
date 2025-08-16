lista1=[]
lista1.append("Junnior")
lista1.append("Pinzas")
lista1.append("25")
lista1.append("Ingeniería de minas")

lista2=[]
lista2.append("Onil")
lista2.append("Pinzas")
lista2.append("17")
lista2.append("Chef")

#Suma de edades de ambas personas
suma=int(lista1[2])+int(lista2[2])
print("La suma de edades de las dos personas es {}".format(suma))

#Suma de listas
suma_list=lista1+lista2
print("La suma de listas es:",suma_list)

#Inversa de listas
suma_list.reverse()
print("La lista al revés es:",suma_list)

#Nueva lista
suma_list.pop(6)
suma_list.pop(2)
print("La nueva lista eliminando la edad de la primera y el apellido del segundo es:",suma_list)

#Actualiza profesión del segundo usuario
suma_list[0]="Reportero"
print("Lista actualizada con profesión del segundo es:",suma_list)

lista=[]
lista.append("Perú")
lista.append("Argentina")
lista.append("Colombia")
lista.append("Chile")
lista.append("Bolivia")
lista.append("Guatemala")
lista.append("Ecuador")

lista.pop(1)
print("Mi lista tiene los siguientes elementos: {}".format(lista))

lista.pop()
print("Mi lista tiene los siguientes elementos: {}".format(lista))

del lista[2]
print(lista)
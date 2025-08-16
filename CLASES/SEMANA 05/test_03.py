"""- Crear una función la cuál va a evaluar una lista y un índice
- Habrá una excepción dentro de la función donde se va a considerar una lista con 4 valores
- Cuando se va a modificar una de las posiciones no existentes
crear un nuevo índice y darle un valor de 0
- Mostrar la lista final"""

def evaluar(lista,i):
    if len(lista)>3:
        print(lista[:4])
        # try:
        #     print(lista)
        # except IndexError:
        #     lista[i]=0
        #     print(lista)


x=[2,4,8,9,12,4,8,6]
evaluar(x,6)
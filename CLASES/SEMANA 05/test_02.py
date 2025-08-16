def operaciones(a,b):
    try:
        resultado1=a+b
        resultado2=a/b
    except TypeError:
        print("No se pueden sumar strings con enteros")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    else:
        print("El resultado es: ",resultado1)
        print("El resultado es: ", resultado2)

# operaciones(40,6)
operaciones(50,0)
"""Funciones"""

"""
Crear una función que recibirá una frase y retornará la cantidad de letras 
que tiene cada palabra dentro de la frase 
"""
# print(help(str.split))

x="Hola papá"
print(x.split())

def contador_palabras(frase):
    palabras = frase.split()
    resultado = []
    for palabra in palabras:
        resultado.append(f"{palabra}: {len(palabra)}")
    return resultado

print(contador_palabras("Hola mundo con Python"))

print(contador_palabras("Tu nuevo mundo de éxitos con Python"))

#sorted: obtener los nombres de los keys (llaves) de un diccionario
#Por ejemplo se puede usar para hacer la lectura de las cabeceras de las base de datos en excel
estudiante={"nombre":"Junnior","edad":28,"padres":["Luis Pinzas","María Ayala"],"notas":[12,18,15,20],"cursos actuales":["cálculo", "geología","mineralogía"]}
keys=sorted(estudiante)
print(keys)

#values: obtener los nombres de los valores de un diccionario
estudiante={"nombre":"Junnior","edad":28,"padres":["Luis Pinzas","María Ayala"],"notas":[12,18,15,20],"cursos actuales":["cálculo", "geología","mineralogía"]}
valores=estudiante.values()
list(valores)
print(valores)
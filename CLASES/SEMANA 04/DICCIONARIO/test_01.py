estudiante={"nombre":"Junnior","edad":28,"promedio":17}


#Cundo queremos cambiar algún valor usamos los corchetes y se cambia
estudiante["nombre"]="Fiorella"

#Si queremos añadir alguna llave y valor, lo hacemos con corchetes también
estudiante["aprobado"]=True
estudiante["apellido"]="Flores"


# Los corchetes sirven para cambiar en caso exista la llave, o añadir en caso no existe la llave
print(estudiante)
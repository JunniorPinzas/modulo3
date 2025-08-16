# Intervención:
# Requisitos:
# - Dentro de una empresa se vaa solicitar pedir el nombre y apellido del empleado (input)
# - Distrito de residencia ingresado por teclado
# - Sueldo y cálculo del bono final de año, que será el triple del sueldo mensual menos el 10% del sueldo
# - Todos estos datos se van a ingresar a un diccionario
# - Asignar a 3 variables los valores del diccionario
# - Mostrar por la terminal (output) el mensaje de: "'Nombre' 'Apellido', recibirá 'bono' soles de fin de año"


nombre=input("Ingrese nu nombre: ")
apellido=input("Ingrese su apellido: ")
distrito="San Miguel"
sueldo=2000
bono=3*sueldo-(0.1*sueldo)

datos={"nombre":nombre,"apellido":apellido,"bono":bono}

print("{}{} recibirá {} soles a fin de año".format(datos["nombre"],datos["apellido"],datos["bono"]))

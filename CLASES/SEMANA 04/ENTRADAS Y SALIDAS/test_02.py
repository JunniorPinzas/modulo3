#Condicional if
from xml.dom.minidom import ProcessingInstruction

edad=int(input("Ingrese su edad: "))
if 0<edad<18:
    print("Usted es menor de edad")
elif 18<=edad<100:
    print("Usted es mayor de edad")
else:
    print("Usted ingresó mal su edad")
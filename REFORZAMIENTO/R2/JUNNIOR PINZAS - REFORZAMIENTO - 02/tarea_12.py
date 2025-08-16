nombre=input("Ingrese su nombre: ")
nom_pro=input("Ingrese el producto a comprar: ")
#precio=input("Ingrese el precio: ")
cant=input("Ingrese la cantidad que desea pedir: ")
precio=50.50
cant2=int(cant)
preciototal=precio*cant2

print("")
print("""Buen día {}, el detalle de su compra es el siguiente:

- Producto: {}
- Precio unitario: 50.50
- Cantidad: {}
- Total a pagar: {}

""".format(nombre,nom_pro,cant,preciototal))
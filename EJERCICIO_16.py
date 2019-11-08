#Hallar el nuevo precio
precio,descuento,nuevo_precio=0.0,0.0,0.0

#Asignacion de valores
precio=float(input("ingrese el precio: "))
descuento=float(input("ingrese el descuento: "))

#Calculo
nuevo_precio=precio-((descuento/100)*precio)

#Verificadores
existe=bool(precio!=(descuento/100))

#Mostrar valores
print("precio:",precio)
print("descuento:",descuento)
print("El nuevo precio es:",nuevo_precio)
print("existe descuento?: "+str(existe))

# Hallar el area de un cuadrado y su perimetro
lado,area,perimetro=0.0,0.0,0.0

# asignacion de valores
lado=float(input("ingrese el lado"))

# Calculo
area=lado**2
perimetro=lado*4

# Verificadores
existe=bool(lado!=0)


# Mostrar valores
print("Lado:",lado)
print("Area:",area)
print("Perimetro:",perimetro)
print("existe el area?: "+str(existe))
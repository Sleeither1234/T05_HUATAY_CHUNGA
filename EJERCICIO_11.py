# Hallar el area de un rectangulo
area,base,altura=0.0,0.0,0.0

# Asignacion de valores
base=float(input("ingrese la base: "))
altura=float(input("ingrese la altura: "))

# Calculo
Area=base*altura

# Verificadores
existe=bool(base!=0 and altura!=0)


# Mostrar valores
print("base:",base)
print("altura:",altura)
print("Area:",Area)
print("existe el area?: "+str(existe))

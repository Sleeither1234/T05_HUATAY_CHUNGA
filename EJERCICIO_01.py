# CALCULO DEL AREA DE UN TRIANGULO
base,altura=0.0,0.0

# ASIGNACION DE LOS VALORES
base=int(input("ingrese la base: "))
altura=int(input("ingrese la altura: "))

# CALCULO
area_del_triangulo=(base*altura)/2

#VERIFICADORESS
es_isoceles=bool(area_del_triangulo>50)


# MOSTRAR VALORES
print("La base del triangulo es: "+str(base))
print("La altura del triangulo es: "+str(altura))
print("El area del triangulo es: "+str(area_del_triangulo))
print("El area del triangulo es un isoceles?: "+str(es_isoceles))












































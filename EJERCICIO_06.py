# CALCULO DE LA PENDIENTE
abscisa,ordenada=0.0,0.0

# ASIGNACION DE VALORES
abscisa=int(input("ingrese la abscisa: "))
ordenada=int(input("ingrese la ordenada: "))

# CALCULO
pendiente=ordenada/abscisa

# VERIFICADORES
existe=bool(ordenada!=0)


# MOSTRAR VALORES
print("El valor de la abscisa es: "+str(abscisa))
print("El valor de la ordenada es: "+str(ordenada))
print("La pendiente tiene valor de: "+str(pendiente))
print("La pendiente existe?: "+str(existe))
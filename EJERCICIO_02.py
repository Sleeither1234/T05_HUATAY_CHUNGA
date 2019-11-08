# CALCULO DE LA FUERZA DE UN OBJETO
masa,aceleracion=0.0,0.0

# ASIGNACION DE VALORES
masa=float(input("ingrese la masa: "))
aceleracion=float(input("ingrese la aceleracion: "))

# CALCULO
Fuerza=masa*aceleracion

# VERIFICADORES
es_positiva=bool(Fuerza>0)


# MOSTRAR VALORES
print("La masa del objeto es: "+str(masa))
print("La aceleracion del objeto es: "+str(aceleracion))
print("La fuerza del objeto es: "+str(Fuerza))
print("La fuerza es positiva?: "+str(es_positiva))

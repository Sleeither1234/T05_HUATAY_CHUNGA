# CALCULO DEL AREA DEL CIRCULO
radio,pi=0.0,0.0

# ASIGNACION DE VALORES
radio=float(input("INGRESE EL RADIO DE LA CINRCUNFERENCIA: "))
pi=float(input("INGRESE EL VALOR DE PI"))

# CALCULO
area_del_circulo=(pi*(radio**2))

# VERIFICADORES
area_existe=bool(area_del_circulo>0)


# MOSTRAR VALORES
print("El radio de la circunferencia es: "+str(radio))
print("El valor de pi es: "+str(pi))
print("El area del circulo es: "+str(area_del_circulo))
print("El area del circulo existe?: "+str(area_existe))


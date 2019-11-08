# CALCULO DE LA PRESION EJERCIDA DE UN OBJETO
FUERZA,AREA=0.0,0.0

# ASIGNACION DE VALORES
FUERZA=float(input("ingrese la fuerza: "))
AREA=float(input("ingrese el area: "))

# CALCULO
presion=FUERZA/AREA

#VERIFICADORES
existe=bool(AREA!=0)


# MOSTRAR VALORES
print("La fuerza ejercida por el objeto es: "+str(FUERZA))
print("El area ejercida por el objeto es: "+str(AREA))
print("La presion que se ejerce sobre el objeto es: "+str(presion))
print("la presion sobre un objeto existe?:"+str(existe))


# CALCULO DE LA DENSIDAD DE UN OBJETO
MASA,VOLUMEN=0.0,0.0

# ASIGNACION DE VALORES
MASA=float(input("ingrese la masa: "))
VOLUMEN=(float(input("ingrese el volumen")))/1000
# el volumen lo dividimos entre mil ya que esta expresado en mililitros

# CALCULO
densidad=MASA/VOLUMEN

# VERIFICADORES
existe=bool(VOLUMEN!=0)



# MOSTRAR VALORES
print("La masa del objeto es: "+str(MASA))
print("El volumen del objeto es: "+str(VOLUMEN))
print("LA densidad del objeto es: "+str(densidad)+"ml")
print("LA densidad existe?: "+str(existe))





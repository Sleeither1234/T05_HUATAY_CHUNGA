# CALCULO DE LA VELOCIDAD FINAL
velocidad_inicial_1,gravedad_1,ALTURA=0.0,0.0,0.0

# ASIGNACION DE VALORES
velocidad_inicial_1=float(input("ingrese la velocidad inicial: "))
gravedad_1=float(input("ingrese la gravedad: "))
ALTURA=float(input("ingese la altura"))

# CALCULO
import  math
velocidad_final=math.sqrt((velocidad_inicial_1**2)+2*(gravedad_1*ALTURA))

# VERIFICADORES
complejo=bool(velocidad_final<0)


# MOSTRAR VALORES
print("La velocidad inicial del objeto es: "+str(velocidad_inicial_1))
print("La gravedad es: "+str(gravedad_1))
print("La altura es: "+str(ALTURA))
print("La velocidad final del vehiculo es: "+str(velocidad_final))
print("la velocidad es un numero complejo?: "+str(complejo))


#Hallar la distancia del movil
velocidad,tiempo,distancia=0.0,0.0,0.0

#Asignacion de valores
velocidad=float(input("ingrese la velocidad: "))
tiempo=float(input("ingrese el tiempo: "))

#Calculo
distancia=velocidad*tiempo

#Verificador
existe=bool(distancia>0)

#Mostrar valores
print("Velocidad:",velocidad)
print("tiempo:",tiempo)
print("Distancia:",distancia)
print("existe distancia?: "+str(existe))

# CALCULO DEL TRABAJO REALIZADO DE UN OBJETO
fuerza,distancia=0.0,0.0

# ASIGNACION DE  LOS VALORES
fuerza=float(input("ingrese la fuerza: "))
distancia=float(input("ingrese la distancia: "))

# CALCULO
trabajo=distancia*fuerza

# VERIFICADORES
hay_trabajo=bool(distancia!=0)


# MOSTRAR VALORES
print("La fuerza del objeto es: "+str(fuerza))
print("La distancia recorrida por el objeto es: "+str(fuerza))
print("El trabajo realizado por un objeto es: "+str(trabajo))
print("Se realiza trabajo?: "+str(hay_trabajo))

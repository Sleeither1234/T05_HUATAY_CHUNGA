# CALCULO DE LA EFICIENCIA DE UNA MAQUINA
energia_total,energia_perdida,energia_util=0.0,0.0,0.0

# ASIGNACION DE VALORES
energia_total=float(input("ingrese la energia suministrada: "))
energia_perdida=float(input("ingrese la energia perdida: "))

# CALCULO
energia_util=energia_total-energia_perdida
eficiencia_de_una_maquina=(energia_util/energia_total)*100

#VERIFICADORES
perdio=bool(energia_util!=energia_total)

# MOSTRAR VALORES
print("La energia total de una maquina es: "+str(energia_total))
print("La energia perdida de una maquina es: "+str(energia_perdida))
print("La energia util de una maquina es: "+str(energia_util))
print("La eficiencia de una maquina es: "+str(eficiencia_de_una_maquina))
print("Perdio energia?: "+str(perdio))

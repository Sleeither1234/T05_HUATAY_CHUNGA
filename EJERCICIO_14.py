#Hallar pago de trabajador
precio_de_hora,horas,pago=0.0,0.0,0.0

#Asignacion de valores
precio_de_hora=float(input("ingrese el precio de hora: "))
horas=int(input("ingrese las horas: "))

#Calculo
pago=precio_de_hora*horas

#Verificadores
trabaja=bool(horas!=0)

print("Precio por hora:",precio_de_hora)
print("cantidad de horas trabajadas:",horas)
print("Pago del trabajador:",pago)
print("trabaja?: ",trabaja)

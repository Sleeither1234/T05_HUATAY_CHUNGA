#Costo de una casa
mano_de_obra,metros_cuadrados,costo=0.0,0.0,0.0

#Asignacion de valores
mano_de_obra=float(input("ingrese el precio de la mano de obra: "))
metros_cuadrados=float(input("ingrese los metros cuadrados"))

#Calculo
costo=mano_de_obra*metros_cuadrados

#Verificadores
existe=bool(metros_cuadrados!=0)

#Mostrar valores
print("Costo de mano de obra:",mano_de_obra)
print("Metros cuadrados:",metros_cuadrados)
print("Costo para hacer la casa:",costo)
print("existe el area para realizar el trabajo?: ",existe)
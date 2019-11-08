#Pago anual de un trabajador
pago_mensual,meses,pago=0.0,0.0,0.0

#Asignacion de valores
pago_mensual=float(input("ingrese el pago mensual: "))
meses=float(input("ingrese los meeses de trabajo: "))

#Calculo
pago=pago_mensual*meses

#Verificadores
trabaja=bool(meses!=0)

#Mostrar valores
print("El pago mensual es:",pago_mensual)
print("Los meses trabajados son:",meses)
print("El pago anual es:",pago)
print("trabajo?: ",str(trabaja))


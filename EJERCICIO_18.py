#Suma de tres numeros
num1,num2,num3,suma=0.0,0.0,0.0,0.0

#Asignacion de valores
num1=float(input("ingrese el primer numero: "))
num2=float(input("ingrese el segundo numero: "))
num3=float(input("ingrese el tercer numero: "))

#Calculo
suma=num2+num1+num3

#Verificadores
centenario=bool(suma>=100 and suma<1000)

#Mostrar valores
print("Primer numero",num1)
print("Segundo numero:",num2)
print("Tercer numero:",num3)
print("La suma es:",suma)
print("es centenario?: ",str(centenario))

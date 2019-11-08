#Area de una circunferencia
area,radio,Pi=0.0,0.0,3.14

#Asignacion de valores
radio=float(input("ingrese el radio: "))

#Calculo
area=Pi*(radio**2)

#Verificadores
existe=bool(radio!=0)


#Mostrar valores
print("Radio:",radio)
print("Pi:",Pi)
print("Area de la circuferencia:",area)
print("Existe el area?: "+str(existe))

#Promedio de tres alumnos
nota1,nota2,nota3,promedio=0.0,0.0,0.0,0.0

#Asignacion de valores
nota1=float(input("ingrese la nota 1: "))
nota2=float(input("ingrese la nota 2: "))
nota3=float(input("ingrese la nota 3: "))

#Calculo
promedio=(nota1+nota2+nota3)/3

#Verificadores
aprueba=bool(promedio>=10.5)

#Mostrar valores
print("Nota del primer alumno:",nota1)
print("Nota del segundo alumno:",nota2)
print("Nota del tercer alumno:",nota3)
print("Promedio de los tres alumnos:",promedio)
print("Aprueba?: "+str(aprueba))

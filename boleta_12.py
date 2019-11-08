# BOLETA PRODUCTOS LACTEOS
primer_producto=input("INGRESE EL NOMBRE DEL PRIMER PRODUCTO: ")
segundo_producto=input("INGRESE EL NOMBRE DEL SEGUNDO PRODUCTO: ")
P_U_1=float(input("INGRESE EL PRECIO DEL PRIMER PRODUCTO LACTEO: "))
P_U_2=float(input("INGRESE EL PRECIO DEL SEGUNDO PRODUCTO LACTEO: "))
unidades_1=int(input("INGRESE EL NUMERO DE UNIDADES DEL PRIMER PRODUCTO: "))
unidades_2=int(input("INGRESE EL NUMERO DE UNIDADES DEL SEGUNDO PRODUCTO: "))
total=P_U_1*unidades_1+P_U_2*unidades_2

print("##########################################################")
print("#             BODEGA ´´LA LACTOSA´´  ´                   #")
print("#")
print("# PRODUCTOS: "+primer_producto+", "+segundo_producto)
print("# P.U 1: "+str(P_U_1))
print("# P.U 2: "+str(P_U_2))
print("# UNIDADES 1 Y 2: "+str(unidades_1)+", "+str(unidades_2))
print("# TOTAL $ : "+str(total))
print("#")
print("#########################################################")

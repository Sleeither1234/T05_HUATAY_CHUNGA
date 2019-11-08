# BOLETA DE VENTA DE ROPA
CLIENTE=input("INGRESE EL NOMBRE DEL CLIENTE: ")
nombre_del_producto=input("INGRESE EL NOMBRE DE LA ROPA: ")
P_U=float(input("INGRESE EL PRECIO DEL PRODUCTO: "))
unidades=int(input("INGRESE EL NUMERO DE UNIDADES: "))
IGV=print("CALCULANDO....")
IGV=P_U*0.18
TOTAL=P_U*unidades+IGV

print("##############################################################")
print("#                   TIENDA  ´´REAL PLAZA´´                   #")
print("#")
print("# CLIENTE: "+CLIENTE)
print("# NOMBRE_PRODUCTO: "+nombre_del_producto)
print("# P_U: "+str(P_U))
print("# TOTAL: "+str(TOTAL))
print("#")
print("##############################################################")


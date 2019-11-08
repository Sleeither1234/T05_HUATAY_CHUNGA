# BOLETA DE VENTA DE MEDICAMENTOS
cliente=input("INGRESE EL NOMBRE DEL CLIENTE: ")
nombre_del_medicamento=input("INGRESE EL NOMBRE DEL MEDICAMENTO: ")
precio_unitario=float(input("INGRESE EL PRECIO DEL PRODUCTO: "))
unidades=int(input("INGRESE EL NUMERO DE UNIDADES: "))
total=precio_unitario*unidades

print("####################################################")
print("#           BOTICA   ´´EL ARCANGEL´´               #")
print("#")
print("# CLIENTE: "+cliente)
print("# NOMBRE_MEDICAMENTO: "+nombre_del_medicamento)
print("# P.U :"+str(precio_unitario))
print("# UNIDADES : "+str(unidades))
print("# TOTAL : "+str(total))
print("#")
print("####################################################")



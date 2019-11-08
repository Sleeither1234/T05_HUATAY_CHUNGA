# BOLETA DE VENTA DE UNA TIENDA TECNOLOGIDCA
producto_1=input("INGRESE EL NOMBRE DEL PRODUCTO: ")
P_U=float(input("INGRESE EL PRECIO UNITARIO DEL PRODUCTO: "))
unidades=int("INGRESE EL NUMERO DE UNIDADES DE SU PRODUCTO")
NOMBRE=input("INGRESE EL NOMBRE DEL CLIENTE: ")
TOTAL=P_U*unidades
IGV=print("CALCULANDO....")
IGV=TOTAL*0.18

print("###########################################################")
print("#            TIENDA ´´ELECKTROMAC´´                       #")
print("#")
print("# CLIENTE: "+NOMBRE)
print("# PRODUCTO: "+producto_1)
print("# P.U: "+str(P_U))
print("# UNIDADES: "+str(unidades))
print("# IGV: "+str(IGV))
print("# TOTAL: "+str(TOTAL))
print("#")
print("###########################################################")
# BOLETA DE VENTA  DE UN CONCIERTO
tipo_de_entrada_1=input("INGRESE EL TIPO DE ENTRADA (VIP O GENERAL): ")
ripo_De_entrada_2=input("INGRESE EL TIPO DE ENTRADA: ")
precio_vip=float(input("INGRESE EL PRECIO DE LA ENTRADA VIP: "))
precio_general=float(input("INGRESE EL PRECIO DE LA ENTRADA GENERAL: "))
unidades_vip=int(input("INGRESE EL NUMERO DE ENTRADAS VIP: "))
unidades_general=int(input("INGRESE EL NUMERO DE ENTRADAS GENERAL: "))
TOTAL=precio_vip*precio_vip+precio_general*unidades_general

print("#################################################################")
print("#                     CONCIERTO  ´´ALL STARS´´                  #")
print("#                                                               #")
print("# ENTRADAS :           VIP             GENERAL                  #")
print("# UNIDADES: "+"           "+str(unidades_vip)+"                   "+str(unidades_general)+"                    #")
print("# PRECIO: "+"             "+str(precio_vip)+"                     "+str(precio_general)+"                      #")
print("#")
print("#")
print("# TOTAL A PAGAR: "+str(TOTAL))
print("#")
print("#")
print("##################################################################")


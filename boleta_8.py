# BOLETA DE UN RESTAURANTE
cliente=input("INGRESE EL NOMBRE DEL CLIENTE: ")
plato_de_carta=input("INGRESE EL PLATO DE LA CARTA ESCOJIDO: ")
unidades_de_plato_carta=int(input("INGRESE LAS UNIDADES DEL PLATO A LA CARTA ESCGIDO: "))
precio_unitario_de_plato_a_la_carta=float(input("INGRESE EL PRECIO UNITARIO DEL PLATO A LA CARTA ESCOGIDO: "))
igv=print("CALCULANDO.........")
igv=(precio_unitario_de_plato_a_la_carta*unidades_de_plato_carta)*0.18
TOTAL=(precio_unitario_de_plato_a_la_carta*unidades_de_plato_carta)+igv


print("##############################################################")
print("#              RESTAURANTE ´´LA CABAÑITA´´                   #")
print("#")
print("# CLIENTE: "+cliente)
print("# PLATO A LA CARTA: "+plato_de_carta)
print("# UNIDADES: "+str(unidades_de_plato_carta))
print("# P.U: "+str(precio_unitario_de_plato_a_la_carta))
print("# IGV: "+str(igv))
print("# TOTAL A PAGAR: "+str(TOTAL))
print("#")
print("##############################################################")
# TICKET DE CINE
cliente=input("INGRESE EL NOMBRE DEL CLIENTE: ")
pelicula=input("INGRESE EL NOMBRE DE LA PELICULA: ")
precio=float(input("INGRESE EL PRECIO DEL TINKET: "))
unidades=int("INGRESE LA CANTIDAD DE LAS UNIDADES: ")
total=precio*unidades

print("#########################################################")
print("#                      CINEMARK                         #")
print("#")
print("# CLIENTE: "+cliente)
print("# PELICULA: "+pelicula)
print("# P.U: "+str(precio))
print("# UNIDADES: "+str(unidades))
print("# TOTAL: "+str(total))
print("#")
print("#########################################################")

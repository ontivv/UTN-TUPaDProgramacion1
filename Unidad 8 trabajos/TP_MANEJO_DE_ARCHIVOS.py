#EJERCICIO 1

with open("productos.txt" , "w") as archivo:
    linea1 = archivo.write("Nombre:Chocolate,Precio:1200,Cantidad:10\n")
    linea2 = archivo.write("Nombre:Medialunas,Precio:900,Cantidad:20\n")
    linea3 = archivo.write("Nombre:Masa de empanadas,Precio:1300,Cantidad:30\n")

#EJERCICIO 2

with open("productos.txt" , "r") as archivo:
    lineas_del_archivo = archivo.readlines()
    
        
    for linea in lineas_del_archivo:
        partes = linea.strip().split(",")
        print(f"Productos: {partes}")

#EJERCICIO 3

with open("productos.txt" , "a") as archivo:
    linea4 = archivo.write(input("Ingrese un nuevo producto (Nombre, Precio, Cantidad): ").title().strip())
    print()

with open("productos.txt" , "r") as archivo:
    lineas_archivo = archivo.readlines()
    for linea in lineas_archivo:
        partes = linea.strip().split(",")
        print(f"Productos: {partes}")

#EJERCICIO 4
print()
lista_productos = []

for lineas in lineas_archivo:
    producto_dict = {}
    pares = lineas.strip().split(",")
    
    for par in pares:
        partes = par.strip().split(":")
    
        clave = partes[0]
        valor = partes[1]
        producto_dict[clave] = valor
    lista_productos.append(producto_dict)

print(f"Lista: {lista_productos}")
print()

#EJERCICIO 5

consulta = input("Producto para buscar: ").capitalize()
cont = 0
encontrado = False

for diccionario in lista_productos:
    
    if diccionario["Nombre"] == consulta:
        encontrado = True
        break
    else:
        cont += 1

if encontrado:
    print()
    print(f"""PRODUCTO: {lista_productos[cont]["Nombre"]} 
        PRECIO: ${lista_productos[cont]["Precio"]}
        CANTIDAD: {lista_productos[cont]["Cantidad"]} Unidades en stock 
            """)
else:
    print()
    print("PRODUCTO NO ENCONTRADO.")

#EJERCICIO 6

lineas_para_guardar = []

for diccionario in lista_productos:
    pares_clave_valor = []
    for clave,valor in diccionario.items():
        pares_clave_valor.append(f"{clave}:{valor}")

    linea_guardado = ",".join(pares_clave_valor) + "\n"
    lineas_para_guardar.append(linea_guardado)

with open("productos.txt" , "w") as archivo:
    archivo.writelines(lineas_para_guardar)

print("✅ Archivo productos.txt sobrescrito con los datos actualizados.")
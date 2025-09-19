#EJERCICIO 1

lista = [0 for _ in range(100)]

for i in range(0,100,1) :
    
    lista[i] = i + 1

print("Multiplos de 4 entre 1 y 100:")

for i in range(0,100,1) :
    
    if lista[i] % 4 == 0 :
        print(lista[i])




#----------------------------------------------------------------------------
#EJERCICIO 2

lista = [1,2,3,4,5]

print(lista[-2])


#----------------------------------------------------------------------------
#EJERCICIO 3


lista = []

for i in range(3):
    
    palabra = input("Ingrese una palabra: ")
    lista.append(palabra)


print("")
print(lista)




#----------------------------------------------------------------------------
#EJERCICIO 4

animales = ["perro", "gato", "conejo", "pez"]

print("LISTA NORMAL: ")
print(animales)

print("")

animales[1] = input("Reemplazo para segundo elemento de la lista: ")
animales[-1] = input("Reemplazo para el último elemento de la lista: ")

print("")
print("LISTA MODIFICADA: ")
print(animales)




#----------------------------------------------------------------------------
#EJERCICIO 5

numeros = [8,15,3,22,7]

numeros.remove(max(numeros))

print(numeros)

#El código lo que hace es remover el valor más grande de la lista con la funcion .remove




#----------------------------------------------------------------------------
#EJERCICIO 6

largo_lista = 0

for i in range(10,31,5):
    
    largo_lista += 1


lista = [0 for _ in range(largo_lista)]

lista_valores = []

for i in range(10,31,5) :
    
    lista_valores.append(i)


for i in range(len(lista_valores)) :
    
    lista[i] = lista_valores [i]


for i in range(2) : 
    print(lista[i])





#----------------------------------------------------------------------------
#EJERCICIO 7

autos = ["sedan" , "polo" , "suran" , "gol"]

autos[1] = input("Ingrese otro nombre: ")
autos[2] = input("Ingrese otro nombre: ")

print(autos)


#----------------------------------------------------------------------------
#EJERCICIO 8

dobles = []



for i in range(3) :
    
    if i == 0 :
        dobles.append(5*2)
    
    elif i == 1:
        dobles.append(10*2)
    
    else : 
        dobles.append(15*2)


print(dobles)


#----------------------------------------------------------------------------
#EJERCICIO 9

compras = [["pan" , "leche"] , ["arroz" , "fideos" , "salsa"] , ["agua"]]

compras_cliente1 = [["pan" , "leche"] , ["arroz" , "fideos" , "salsa"] , ["agua"]]

compras_cliente2 = [["pan" , "leche"] , ["arroz" , "fideos" , "salsa"] , ["agua"]]

compras_cliente3 = [["pan" , "leche"] , ["arroz" , "fideos" , "salsa"] , ["agua"]]


#a)
compras_cliente3[2].append("jugo")

#b)
compras_cliente2[1][1] = "tallarines"

#c)
compras_cliente1[0].remove("pan")


filas_cliente1 = len(compras_cliente1)
filas_cliente2 = len(compras_cliente2)
filas_cliente3 = len(compras_cliente3)

elem = 3

#d)
print(f"LISTA COMPRAS CLIENTE 1:")

for filas_cliente1 in compras_cliente1 :
    for elem in filas_cliente1 :
        print(f"{elem:3}",end= "  ")
    print()


print("")
print(f"LISTA COMPRAS CLIENTE 2:")

for filas_cliente2 in compras_cliente2 :
    for elem in filas_cliente2 :
        print(f"{elem:3}",end= "  ")
    print()


print("")
print(f"LISTA COMPRAS CLIENTE 3:")

for filas_cliente3 in compras_cliente3 :
    for elem in filas_cliente3 :
        print(f"{elem:3}",end= "  ")
    print()




#----------------------------------------------------------------------------
#EJERCICIO 10

lista_anidada = [[15] , [True] , [[25.5] , [57.9] , [30.6]] , [False]]

print(lista_anidada)
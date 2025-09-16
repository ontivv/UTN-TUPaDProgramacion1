#EJERCICIO 1

for i in range(0,100+1,1):
    
    print (i)

#-----------------------------------------------------------------
#EJERCICIO 2

continuar = 1

while continuar == 1 :
    num = int(input("Ingrese un número: "))
    
    cant_digitos = len(str(num))
    
    if cant_digitos <= 1 :
        print(f"La cantidad de dígitos del número ingresado es: {cant_digitos}")
        if num<0 :
            print("(incluyendo el símbolo)")
    
    
    else:
        print(f"La cantidad de dígitos del número ingresado son: {cant_digitos}")
        if num<0 :
            print("(incluyendo el símbolo)")

    continuar = int(input("""¿Desea repetir la operación?
                            
                            (1) SI
                            (0) NO
                            
                            """))





#-----------------------------------------------------------------
#EJERCICIO 3


num1 = int(input("Ingrese el primer número: "))

print("")

num2 = int(input("Ingrese el segundo número: "))

print("")
print("")
print("SUMA DE TODOS LOS VALORES ENTRE AMBOS NÚMEROS (excluyendo a los ingresados): ")

suma = 0
iterador = num2 + 1

if num1 > num2 :
    
    iterador = num2 + 1
    
    for i in range(iterador,num1-1,1) :
        
        print(f"{i} + {i+1} = {i+(i+1)}")
        
        suma += (i + (i+1))

if num2 > num1 :
    
    iterador = num1 + 1
    for i in range(iterador,num2-1,1) :
        
        print(f"{i} + {i+1} = {i+(i+1)}")
        suma += (i + (i+1))

print("")
print(f"EL TOTAL DE LAS SUMAS ES: {suma}")



#-----------------------------------------------------------------
#EJERCICIO 4

num = int(input("Ingrese un número: "))

suma = 0


while num != 0 :
    
    num = int(input("Ingrese otro número: "))
    suma += num


print("")
print(f"La suma de todos los números ingresados es: {suma}")





#-----------------------------------------------------------------
#EJERCICIO 5


import random

num = random.randint(0,9)

num_usuario = int(input("Adivine el número: "))

intentos = 1

while num_usuario != num_usuario :
    
    num_usuario = int(input("Número equivocado, ingrese nuevamente: "))
    intentos += 1

print("")
print("")

print("CORRECTO!")
print(f"Cantidad de intentos: {intentos}")



#-----------------------------------------------------------------
#EJERCICIO 6

for i in range(100,0,-1) : 
    
    if i % 2 == 0 :
        print(i)







#-----------------------------------------------------------------
#EJERCICIO 7

num = int(input("Ingrese un número: "))

print("")
print("")
print("SUMA DE TODOS LOS VALORES ENTRE 0 Y EL NÚMERO INGRESADO ES: ")

suma = 0

for i in range(0,num,1) :
        
    print(f"{i} + {i+1} = {i+(i+1)}")
        
    suma += (i + (i+1))

print("")
print(f"EL TOTAL DE LAS SUMAS ES: {suma}")




#-----------------------------------------------------------------
#EJERCICIO 8

cant_num = 100

numeros = [0 for _ in range(cant_num)]

num_pares = 0
num_impares = 0
num_negativos = 0
num_positivos = 0

for i in range(cant_num) :
    
    numeros[i] = int(input("Ingrese números enteros: "))
    
    if numeros[i] % 2 == 0 :
        
        num_pares += 1
        
        
        if numeros[i] < 0 :
        
            num_negativos += 1
    
        elif numeros[i] > 0 :
            
            num_positivos += 1




    elif numeros[i] % 2 != 0 :
        
        num_impares += 1
        
        
        if numeros[i] < 0 :
        
            num_negativos += 1
        
        elif numeros[i] > 0 :
            
            num_positivos += 1

print("")
print("")

print(f"""Dados los números ingresados: 
        
        Hay {num_pares} números pares.
        Hay {num_impares} números impares.
        Hay {num_negativos} números negativos.
        Hay {num_positivos} números positivos.
        
        """)






#-----------------------------------------------------------------
#EJERCICIO 9


cant_numeros_lista = 10

numeros = [0 for _ in range (cant_numeros_lista)]
suma = 0
cant_numeros = 0


for i in range(cant_numeros_lista) :
    
    numeros[i] = int(input("Ingrese algún número: "))
    
    suma += numeros[i]
    cant_numeros += 1

media_numeros = suma/cant_numeros

print("")
print("")

print(f"La media de los números ingresados es de {media_numeros}")




#-----------------------------------------------------------------
#EJERCICIO 10

num = int(input("Ingrese un número: "))

numero = [int(_) for _ in str(num)]

long_num = len(numero)

print("Número invertido:", end = "  ")

for i in range(long_num-1,-1,-1) :
    
    print(numero[i], end = "")
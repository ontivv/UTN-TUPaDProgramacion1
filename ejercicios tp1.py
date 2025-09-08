#-----------------------------------------------------------------
#                    EJERCICIO 1

print("PRIMER EJERCICIO")

print("Hola mundo!")



#-----------------------------------------------------------------
#                    EJERCICIO 2



nombre = input("Ingresa tu nombre: ")

print(f"¡Bienvenido,",nombre,"!")



#-----------------------------------------------------------------
#                    EJERCICIO 3




nombre = input("Ingresa tu nombre: ")
apellido= input("Ingresa tu apellido: ")
edad= int(input("Ingresa tu edad: "))
residencia= input("Ingresa tu país de residencia: ")

print("Hola, soy",nombre,apellido,", tengo ",edad,"años y vivo en",residencia,".")








#-----------------------------------------------------------------
#                    EJERCICIO 4


import math

radio= int(input("Ingresa el radio del circulo: "))

area= math.pi * radio**2

perimetro= 2 * math.pi * radio

print("")
print("El área del circulo según el radio ingresado es:",area)
print("")
print("El perímetro del circulo según el radio ingresado es:",perimetro)






#-----------------------------------------------------------------
#                    EJERCICIO 5



segundos= int(input("Ingresa una cantidad de segundos: "))

horas= segundos // 3600

print("La cantidad de segundos ingresada equivale a: ",horas," horas.")






#-----------------------------------------------------------------
#                    EJERCICIO 6



numero= int(input("Ingrese el número del cual quiere saber la tabla: "))

print(numero," x 1 = ", numero*1)
print(numero," x 2 = ", numero*2)
print(numero," x 3 = ", numero*3)
print(numero," x 4 = ", numero*4)
print(numero," x 5 = ", numero*5)
print(numero," x 6 = ", numero*6)
print(numero," x 7 = ", numero*7)
print(numero," x 8 = ", numero*8)
print(numero," x 9 = ", numero*9)
print(numero," x 10 =", numero*10)





#-----------------------------------------------------------------
#                    EJERCICIO 7




numero1 = int(input("Ingrese el primer número: "))
print("")
numero2 = int(input("Ingrese el segundo número: "))
print("")
print("")

print("Suma:",numero1,"+",numero2,"=",numero1+numero2)
print("Resta: ",numero1,"-",numero2,"=",numero1-numero2)
print("Multiplicación: ",numero1,"*",numero2,"=",numero1*numero2)
print("División: ",numero1,"/",numero2,"=",numero1/numero2)





#-----------------------------------------------------------------
#                    EJERCICIO 8




peso= int(input("Ingresa tu peso en Kilogramos: "))
altura= float(input("Ingresa tu altura en Metros: "))

IMC= peso/altura**2

print("Su índice de masa corporal es: ",IMC)





#-----------------------------------------------------------------
#                    EJERCICIO 9




temp_celsius= float(input("Ingrese una temperatura en grados Celsius: "))

temp_fahrenheit= (9/5) * temp_celsius + 32

print("")

print("La temperatura ingresada convertida a grados Fahrenheit es: ",temp_fahrenheit)






#-----------------------------------------------------------------
#                    EJERCICIO 10

num1= int(input("Ingresa el primer número: "))
num2= int(input("Ingresa el segundo número: "))
num3= int(input("Ingresa el tercer número: "))

print("")

promedio= (num1+num2+num3)/3 

print("El promedio de los 3 números ingresados es de:", promedio)
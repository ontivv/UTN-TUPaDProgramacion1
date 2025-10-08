#EJERCICIO 1
def imprimir_HolaMundo(): 
    print("Hola Mundo")

imprimir_HolaMundo()

#-----------------------------------------------------
#EJERCICIO 2

def saludar_usuario(x):
    
    print(f"¡Hola {x}!")

saludar_usuario(input("Ingresa tu nombre: "))

#-----------------------------------------------------
#EJERCICIO 3

def informacion_personal(nombre, apellido, edad, residencia):
    print()
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre_y_apellido = input("Ingresa tu nombre y tu apellido (SEPARAR CON ESPACIO) : ")
nombre,apellido = nombre_y_apellido.split(" ")

edad= input("Ingresa tu edad en números: ")
residencia= input("Ingresa tu residencia: ")

informacion_personal(nombre,apellido,edad,residencia)

#-----------------------------------------------------
#EJERCICIO 4

import math

def calcular_area_circulo(r):
    
    area = math.pi * (r*r)
    return area

def calcular_perimetro_circulo(r):
    
    perimetro = 2 * r * math.pi
    return perimetro

radio = float(input("Ingrese el radio del circulo: "))

print()
print(f"El área del círculo es {round(calcular_area_circulo(radio),2)} y el perímetro es {round(calcular_perimetro_circulo(radio),2)}")

#-----------------------------------------------------
#EJERCICIO 5

def segundos_a_horas(s):
    
    horas = s/3600
    return horas

segundos = int(input("Ingresa una cantidad de segundos: "))

print(f"{segundos} segundos equivalen a {int(segundos_a_horas(segundos))} horas")

#-----------------------------------------------------
#EJERCICIO 6

def tabla_numero(n):
    print()
    print(f"TABLA DEL {n}:")
    for i in range(1,11,1):
        print(f"{n} x {i} = {n*i}")

tabla_numero(int(input("Ingrese un número: ")))

#-----------------------------------------------------
#EJERCICIO 7

def operaciones_basicas(a,b):
    op = (a+b , a-b , a*b , a/b)
    
    print()
    print(f"""OPERACIONES: 
            
            SUMA: {a} + {b} = {op[0]}
            RESTA: {a} - {b} = {op[1]}
            MULTIPLICACIÓN: {a} * {b} = {op[2]}
            DIVISIÓN: {a} / {b} = {op[3]}
            
            """)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

operaciones_basicas(num1,num2)

#-----------------------------------------------------
#EJERCICIO 8

def calcular_IMC(p,a):
    
    IMC = p/(a**2)
    return IMC

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

print(f"Su índice de masa corporal (IMC) es: {round(calcular_IMC(peso,altura),2)}")

#-----------------------------------------------------
#EJERCICIO 9

def celsius_a_fahrenheit(c):
    
    f = (c*1.8) + 32
    return f

celsius = float(input("Ingrese una temperatura en grados celsius: "))

print(f"{celsius}° CELSIUS pasados a FAHRENHEIT es: {celsius_a_fahrenheit(celsius)}° FAHRENHEIT")

#-----------------------------------------------------
#EJERCICIO 10

def promedio(a,b,c):
    
    promedio = (a+b+c)/3
    return promedio

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

print()
print(f"Su promedio es: {promedio(nota1,nota2,nota3)}")
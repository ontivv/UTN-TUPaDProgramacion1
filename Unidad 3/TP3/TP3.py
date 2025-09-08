#EJERCICIO 1

edad= int(input("Ingrese su edad: "))

if edad>=18 :
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")




#-------------------------------------------------------------------    
#EJERCICIO 2

nota_alumno= float(input("Ingrese su nota: "))

if nota_alumno>=6 :
    print("Usted está aprobado.")
else:
    print("Usted está desaprobado.")



#-------------------------------------------------------------------    
#EJERCICIO 3

num= int(input("Ingrese un número par: "))

if num % 2==0:
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar, ingrese nuevamente.")


#-------------------------------------------------------------------    
#EJERCICIO 4

edad= int(input("Ingrese su edad: "))

if edad<12:
    print("Usted es un/a niño/a.")
    
elif edad>=12 and edad<18:
    print("Usted es adolescente.")

elif edad>=18 and edad<30:
    print("Usted es un/a Adulto/a joven")

else:
    print("Usted es un/a adulto/a")



#-------------------------------------------------------------------    
#EJERCICIO 5


contra= input("Ingrese su contraseña: ")

longitud_contr= len(contra)

if longitud_contr>=8 and longitud_contr<=14:
    print("Contraseña correcta!")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")




#-------------------------------------------------------------------    
#EJERCICIO 6

import random
import statistics

numeros_aleatorios= [random.randint(1,100) for i in range(50)]

media= statistics.mean(numeros_aleatorios) 
mediana= statistics.median(numeros_aleatorios)
moda= statistics.mode(numeros_aleatorios)

print(f"""SEGÚN LOS NÚMEROS DE LA LISTA:
    
    La media de los números es: {media}
    La mediana de los números es: {mediana}
    La moda de los números es: {moda}
    
        """)

if media==mediana and mediana==moda:
    print("Sin Sesgo.")

elif media>mediana and mediana>moda:
    print("Sesgo positivo o a la derecha.")

elif media<mediana and mediana<moda:
    print("Sesgo negativo o a la izquierda.")
    
else: 
    print("No hay sesgo típico. Puede ser irregular o influenciado por valores extremos.")
    #respecto al else, me dio curiosidad saber cómo se describía si no se cumplían ninguna
    #de las 3 condiciones.




#-------------------------------------------------------------------    
#EJERCICIO 7


palabra= input("Ingrese una palabra= ")

vocales= "aeiouAEIOU"

ultima_l= palabra[len(palabra)-1]

if ultima_l in vocales:
    print(f"{palabra}!")
else:
    print(palabra)


#-------------------------------------------------------------------    
#EJERCICIO 8


nombre= input("Escribe tu nombre: ")

decision= int(input("""¿""Qúe deseas?
                    
                    
                        (1) Quiere su nombre en mayúsculas (EJEMPLO: JUAN)
                        (2) Quiere su nombre en minúsculas (EJEMPLO: juan)
                        (3) Quiere la letra inicial en mayúscula (EJEMPLO: Juan)
                    
                    """))


if decision == 1:
    print(nombre.upper())
elif decision == 2:
    print(nombre.lower())
elif decision == 3:
    print(nombre.title())
else:
    print("Opción incorrecta.")


#-------------------------------------------------------------------    
#EJERCICIO 9


magnitud= float(input("Ingrese la magnitud del terremoto: "))


print("")
print("CLASIFICACIÓN SEGÚN LA ESCALA DE RITCHER: ")

if magnitud<3:
    print("Muy leve (imperceptible).")

elif magnitud>=3 and magnitud<4:
    print("Leve (ligeramente perceptible).")

elif magnitud>=4 and magnitud<5:
    print( "Moderado (sentido por personas, pero generalmente no causa daños).")

elif magnitud>=5 and magnitud<6:
    print("Fuerte (puede causar daños en estructuras débiles).")

elif magnitud>=6 and magnitud<7:
    print("Muy fuerte (puede causar daños significativos).")

elif magnitud>=7:
    print("Extremo (puede causar graves daños a gran escala).")


#-------------------------------------------------------------------    
#EJERCICIO 10


hemisferio= input("""Ingrese en cúal hemisferio se encuentra:

                    (N) Norte
                    (S) Sur

                    """).upper()

dia= int(input("Ingrese el día de hoy en números dia: "))
mes= input("Ingrese el mes en palabras: ").title()


#Todos los meses de cada estación
mes_1= ["Diciembre", "Enero", "Febrero", "Marzo"]
mes_2= ["Marzo","Abril","Mayo", "Junio"]
mes_3= ["Junio", "Julio", "Agosto", "Septiembre"]
mes_4= ["Septiembre", "Octubre", "Noviembre", "Diciembre"]

print("")

cond_cumplida= 0 #Esto hará que no se repitan las impresiones si se cumplen otras condiciones

#HEMISFERIO NORTE

if cond_cumplida==0:
    if hemisferio=="N":
        if mes in mes_1:
        
                if mes=="Diciembre":
                    if dia>=21:
                        print("Estás en invierno.")
                        cond_cumplida+=1
                    
                elif mes=="Marzo":
                    if dia<=20:
                        print("Estás en invierno.")
                        cond_cumplida+=1
                else:
                        print("Estás en invierno.")
                        cond_cumplida+=1        


if cond_cumplida==0:
    if hemisferio=="N":
        if mes in mes_1:
        
                if mes=="Marzo":
                    if dia>=21:
                        print("Estás en primavera.")
                        cond_cumplida+=1
                    
                elif mes=="Junio":
                    if dia<=20:
                        print("Estás en primavera.")
                        cond_cumplida+=1
                else:
                        print("Estás en primavera.")
                        cond_cumplida+=1       



if cond_cumplida==0:
    if hemisferio=="N":
        if mes in mes_1:
        
                if mes=="Junio":
                    if dia>=21:
                        print("Estás en otoño.")
                        cond_cumplida+=1
                    
                elif mes=="Septiembre":
                    if dia<=20:
                        print("Estás en otoño.")
                        cond_cumplida+=1
                else:
                        print("Estás en otoño.")
                        cond_cumplida+=1      


if cond_cumplida==0:
    if hemisferio=="N":
        if mes in mes_1:
        
                if mes=="Septiembre":
                    if dia>=21:
                        print("Estás en verano.")
                        cond_cumplida+=1
                    
                elif mes=="Diciembre":
                    if dia<=20:
                        print("Estás en verano.")
                        cond_cumplida+=1
                else:
                        print("Estás en verano.")
                        cond_cumplida+=1      




#HEMISFERIO SUR

if cond_cumplida==0:
    if hemisferio=="S":
        if mes in mes_1:
        
                if mes=="Diciembre":
                    if dia>=21:
                        print("Estás en verano.")
                        cond_cumplida+=1
                    
                elif mes=="Marzo":
                    if dia<=20:
                        print("Estás en verano.")
                        cond_cumplida+=1
                else:
                        print("Estás en verano.")
                        cond_cumplida+=1 


if cond_cumplida==0:
    if hemisferio=="S":
        if mes in mes_1:
        
                if mes=="Marzo":
                    if dia>=21:
                        print("Estás en otoño.")
                        cond_cumplida+=1
                    
                elif mes=="Junio":
                    if dia<=20:
                        print("Estás en otoño.")
                        cond_cumplida+=1
                else:
                        print("Estás en otoño.")
                        cond_cumplida+=1      


if cond_cumplida==0:
    if hemisferio=="S":
        if mes in mes_1:
        
                if mes=="Junio":
                    if dia>=21:
                        print("Estás en invierno.")
                        cond_cumplida+=1
                    
                elif mes=="Septiembre":
                    if dia<=20:
                        print("Estás en invierno.")
                        cond_cumplida+=1
                else:
                        print("Estás en invierno.")
                        cond_cumplida+=1     


if cond_cumplida==0:
    if hemisferio=="S":
        if mes in mes_1:
        
                if mes=="Septiembre":
                    if dia>=21:
                        print("Estás en primavera.")
                        cond_cumplida+=1
                    
                elif mes=="Diciembre":
                    if dia<=20:
                        print("Estás en primavera.")
                        cond_cumplida+=1
                else:
                        print("Estás en primavera.")
                        cond_cumplida+=1
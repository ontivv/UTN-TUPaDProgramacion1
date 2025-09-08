print("Ingrese la fecha: ")

fecha= input("Ingrese la fecha del día separada por comas en formato dia, DD/MM):")

dia, f_num= fecha.split(",")

n_dia, n_mes = f_num.split( "/" )



n_dia= n_dia.zfill(2)

n_mes= n_mes.zfill(2)

n_dia= int(n_dia)
n_mes= int(n_mes)

if n_dia<1 or n_dia>31 or n_mes<1 or n_mes>12: 
    
    fecha= input("FECHA INVÁLIDA, INGRESE NUEVAMENTE (día, DD/MM): ")
    
    dia, f_num= fecha.split(",")

    n_dia, n_mes = f_num.split( "/" )

    n_dia= n_dia.zfill(2)

    n_mes= n_mes.zfill(2)


print("")
print(f"Fecha ingresada correctamente! Hoy es {dia}, {n_dia}/{n_mes}")
print("")


import random

if dia== "Lunes" or dia== "lunes" :
    exam= random.randint(0, 1)
    print("NIVEL INICIAL: ")
    if exam==0 :
        print("Aún no se toman los examenes.")
    else :
        print("Ya se tomaron los examenes.")
        print("")
        alumn_ap= int(input("Ingrese la cantidad de alumnos aprobados: "))
        alumn_desap= int(input("Ingrese la cantidad de alumnos desaprobados: "))

        cant_alumn= alumn_ap + alumn_desap

        porcent_aprobados= (alumn_ap/cant_alumn)*100
        print(f"El porcentaje de alumnos aprobado es {int(porcent_aprobados)}%.")



if dia== "Martes" or dia== "martes" :
    exam= random.randint(0, 1)
    print("NIVEL INTERMEDIO: ")
    if exam==0 :
        print("Aún no se toman los examenes.")
    else :
        print("Ya se tomaron los examenes.")
        print("")
        alumn_ap= int(input("Ingrese la cantidad de alumnos aprobados: "))
        alumn_desap= int(input("Ingrese la cantidad de alumnos desaprobados: "))

        cant_alumn= alumn_ap + alumn_desap

        porcent_aprobados= (alumn_ap/cant_alumn)*100
        print(f"El porcentaje de alumnos aprobado es {int(porcent_aprobados)}%.")



if dia== "Miercoles" or dia== "Miércoles" or dia== "miércoles" or dia== "miercoles" :
    exam= random.randint(0, 1)
    print("NIVEL AVANZADO: ")
    if exam==0 :
        print("Aún no se toman los examenes.")
    else :
        print("Ya se tomaron los examenes.")
        print("")
        alumn_ap= int(input("Ingrese la cantidad de alumnos aprobados: "))
        alumn_desap= int(input("Ingrese la cantidad de alumnos desaprobados: "))

        cant_alumn= alumn_ap + alumn_desap

        porcent_aprobados= (alumn_ap/cant_alumn)*100
        print(f"El porcentaje de alumnos aprobado es {int(porcent_aprobados)}%.")




if dia== "Jueves" or dia== "jueves" : 
    print("PRÁCTICAS HABLADAS")
    print("")

    porc_asistencia= input("Ingrese el porcentaje de asistencia de hoy: ")

    num_porc= int(porc_asistencia.replace("%",""))
    
    
    if num_porc>= 50 and num_porc<100 :
        print("Asistió la mayoría.")

    elif num_porc==100 :
        print("Asistieron todos.")

    else : 
        print("No asistió la mayoría.")




if dia== "Viernes" or dia== "viernes" :
    print("INGLÉS PARA VIAJEROS")
    print("")

    n_dia= int(n_dia)
    n_mes= int(n_mes)
        
    if (n_dia== 1 and n_mes==1) or (n_dia== 1 and n_mes== 7):
        print("Comienzo de nuevo ciclo")
        cant_alumn_nuevo_ciclo= int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel_p_alumn= int(input("Ingrese el arancel por alumno: $"))
        print("")

        ingr_total= arancel_p_alumn * cant_alumn_nuevo_ciclo

        print(f"Ingreso total: ${ingr_total}")
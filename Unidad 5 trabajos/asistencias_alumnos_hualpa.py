cant_alumnnos = int(input("Ingresar cuántos alumnos están inscritos: "))

n_alumnos = ["" for _ in range(cant_alumnnos)]
a_alumnos = [0 for _ in range(cant_alumnnos)]

continuar = 1

print("")
print("Creando listado de alumnos:")
print("")

for i in range(cant_alumnnos) : 
    n_alumnos[i] = input("Nombre del alumno: ")
    a_alumnos[i] = 0

while continuar == 1 :
    
    opcion = int(input(""" MENÚ
                    
                    
                    (1) Añadir alumno
                    (2) Ver listado de asistencias 
                    (3) Consultar asistencias de un alumno
                    (4) Imprimir alumnos con asistencias 0
                    (5) Aumentar asistencias por alumno
                    
                    
                    """))
    
    if opcion == 1 :
        
        adicion = 1
        
        while adicion == 1 :
            
            alumno_adicion = input("Nombre de alumno a ingresar: ")
            
            n_alumnos.append(alumno_adicion)
            
            cant_alumnnos = len(n_alumnos)
            
            for i in range(cant_alumnnos) :
                print(n_alumnos[i])
        
            adicion = int(input("""¿Desea agregar otro alumno?
                            
                            (1) SI
                            (0) NO
                            
                            """))
        print("")
        print("")
    
    elif opcion == 2 :
        
        import random
        
        print("")
        print("")
        
        for i in range(cant_alumnnos) : 
            
            a_alumnos[i] = random.randint(0,10)
            
            print(f". {n_alumnos[i].title()}: {a_alumnos[i].title()} asistencias")
            
        print("")
        print("")

    elif opcion == 3 :
    
        iterador = 1
        
        print("")
        print("")
        
        while iterador == 1 :
        
            for i in range(cant_alumnnos) :
                n_alumnos[i] = n_alumnos[i].lower
            
            
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            
            nombre_alumno = nombre_alumno.lower
            
            if nombre_alumno in n_alumnos :
                
                pos_alumno = n_alumnos.index(nombre_alumno)
                
                print(f"{nombre_alumno[pos_alumno].title()}: {a_alumnos[pos_alumno]} asistencias")
                
            iterador = int(input("""¿Desea ver las asistencias de otro alumno?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))    
        print("")
        print("")
    
    
    
    
    elif opcion == 4 :
        
        for i in range(cant_alumnnos) :
            
            if a_alumnos[i] == 0 :
                print(f"{n_alumnos[i].title()} tiene 0 asistencias")
            
        print("")
        print("")
        
        
    elif opcion == 5 :
        
        condicion = 1
        
        while condicion == 1 : 
            
            cant_alumnos_aumento = int(input("¿A cuantos alumnos se les aumentarán las asistencias? : "))
            
            pos_alumno_aum = 0
            
            for i in range(cant_alumnnos) :
                
                n_alumnos[i] = n_alumnos[i].lower
                
            
            for i in range(cant_alumnos_aumento) :
                
                nombre_alumno_aumento = input("Nombre alumno: ")
                nombre_alumno_aumento = nombre_alumno_aumento.lower
                
                
                if nombre_alumno_aumento in n_alumnos :
                    
                    pos_alumno_aum = n_alumnos.index(nombre_alumno_aumento)
                    
                    a_alumnos[pos_alumno_aum] = a_alumnos[pos_alumno_aum] + 1
                    
                
                print(f"{nombre_alumno_aumento[pos_alumno_aum].title()}: {a_alumnos[pos_alumno_aum]} aistencias")
                
                print("")
                print("")
                
                
                
    continuar = int(input("""¿Desea repetir algún proceso?
                                
                            (1) SI
                            (0) NO
                                 
                            """))
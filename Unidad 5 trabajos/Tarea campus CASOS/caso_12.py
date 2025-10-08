continuar = 1

excursiones = ["City Tour", "Trekking Montaña", "Avistaje Ballenas"]
cupos = [15, 0, 8]

while continuar == 1:
    
    menu = int(input("""
                        
                        (1) Crear nueva lista de excursiones y cupos
                        (2) Mostrar oferta/cupos
                        (3) Consultar cupo por nombre
                        (4) Agregar excursión
                        (5) Ver excursiones sin cupo
                        (6) Actualizar cupos
                        (7) Salir
                        
                        """))

    match menu:
        
        case 1:
            
            print()
            
            cant_excursiones = int(input("Cantidad de excursiones: "))
            excursiones = ["" for _ in range(cant_excursiones)]
            cupos = [0 for _ in range(cant_excursiones)]
            
            for i in range(cant_excursiones):
                excursiones[i] = input("Nombre excursion: ")
                cupos[i] = int(input("Cantidad cupos: "))
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 2:
            
            cant_excursiones = len(excursiones)
            
            print()
            print("EXCURSIONES: ")
            print()
            
            for i in range(cant_excursiones):
                print(f"{excursiones[i]} - {cupos[i]} cupos disponibles")
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 3:
            
            cant_excursiones = len(excursiones)
            
            for i in range(cant_excursiones):
                excursiones[i] = excursiones[i].lower()
            
            exc_buscada = input("Ingrese excursión deseada: ").lower()
            
            if exc_buscada in excursiones:
                
                p_excursion = excursiones.index(exc_buscada)
                
                for i in range(cant_excursiones):
                    excursiones[i] = excursiones[i].capitalize()
                
                print()
                print(f"{excursiones[p_excursion]} - {cupos[p_excursion]} cupos disponibles")
            
            else: 
                print()
                print("EXCURSION NO REGISTRADA")
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 4:
            
            print()
            
            cant_excursiones = int(input("Cantidad de excursiones para añadir: "))
            
            
            
            while cant_excursiones < 0:
                
                cant_excursiones = int(input("Valor inválido, ingrese nuevamente: "))
            
            if cant_excursiones == 0:
                print()
                print("No hay excursiones que agregar")
            
            else: 
                
                print()
                for i in range(cant_excursiones):
                    excursiones.append(input("Nombre excursion: "))
                    cupos.append(int(input("Cantidad cupos: ")))
                    
                    while cupos[len(cupos)-1] < 0:
                        print()
                        cupos[len(cupos)-1] = int(input("Cantidad inválida, ingrese nuevamente: "))
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 5:
            
            cant_excursiones = len(excursiones)
            
            print()
            print("EXCURSIONES AGOTADAS:")
            print()
            
            contador = 0
            
            for i in range(cant_excursiones):
                
                if cupos[i] == 0:
                    print(f"{excursiones[i]}")
                    contador += 1
            
            if contador == 0:
                print("No hay excursiones agotadas.")
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 6:
            
            cant_excursiones = len(excursiones)
            
            for i in range(cant_excursiones):
                excursiones[i] = excursiones[i].lower()
            
            exc_buscada = input("Nombre de excursion: ").lower()
            print()
            
            if exc_buscada in excursiones:
                
                p_excursion = excursiones.index(exc_buscada)
                
                eleccion = int(input("""¿Qué desea hacer?
                                        
                                        (1) AÑADIR CUPOS
                                        (2) RESTAR CUPOS
                                        
                                        """))
                
                match eleccion:
                    
                    case 1:
                        
                        cant_suma = int(input("Cantidad a sumar: "))
                        print()
                        
                        while cant_suma < 0:
                            
                            cant_suma = int(input("Cantidad inválida, ingrese nuevamente: "))
                        
                        if cant_suma == 0:
                            
                            print("No hay nada para añadir.")
                            continue
                        
                        cupos[p_excursion] += cant_suma
                        
                        for i in range(cant_excursiones):
                            excursiones[i] = excursiones[i].capitalize()
                        
                        print()
                        print(f"{excursiones[p_excursion]} - {cupos[p_excursion]} cupos disponibles")
                    
                    case 2:
                        
                        if cupos[p_excursion] == 0:
                            print()
                            print("Excursion ya agotada.")
                            continue
                        
                        cant_resta = int(input("Cantidad a restar: "))
                        print()
                        
                        while cant_resta < 0:
                            
                            cant_resta = int(input("Cantidad inválida, ingrese nuevamente: "))
                        
                        if cant_resta == 0:
                            
                            print("No hay nada para restar.")
                            continue
                        
                        cupos[p_excursion] -= cant_resta
                        
                        for i in range(cant_excursiones):
                            excursiones[i] = excursiones[i].capitalize()
                        
                        print()
                        print(f"{excursiones[p_excursion]} - {cupos[p_excursion]} cupos disponibles")
            
            else:
                
                print("EXCURSION NO REGISTRADA")
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 7:
            
            print()
            print("FIN DEL PROGRAMA.")            
            continuar = 0
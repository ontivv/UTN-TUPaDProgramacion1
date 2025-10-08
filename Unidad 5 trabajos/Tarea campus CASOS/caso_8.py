instrumentos = ["Guitarra Acustica" , "Bajo Electrico" , "Bateria" , "Amplificador de Bajo" , "Violin" , "Trompeta"]
unidades = [ 3 , 4 , 2 , 3 , 7 , 0]

continuar = 1

while continuar == 1:
    
    print()
    
    opcion = int(input("""
                        
                        (1) Crear nuevo listado de instrumentos 
                        (2) Mostrar inventario completo
                        (3) Consultar unidades por instrumento
                        (4) Ver instrumentos faltantes
                        (5) Agregar instrumento
                        (6) Actualizar unidades
                        (7) Salir
                        
                        """))
    
    match opcion:
        
        case 1:
            
            print()
            
            cant_instrumentos = int(input("¿Cuántos instrumentos desea ingresar?: "))
            
            instrumentos = ["" for _ in range(cant_instrumentos)]
            unidades = [0 for _ in range(cant_instrumentos)]
            
            for i in range(cant_instrumentos):
                
                instrumentos[i] = input("Nombre del instrumento: ")
                unidades[i] = int(input("Unidades disponibles: "))
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (2) NO
                                    
                                    """))
        
        case 2:
            
            cant_instrumentos = len(instrumentos)
            
            print()
            print("LISTADO DE INSTRUMENTOS REGISTRADOS: ")
            print()
            
            for i in range(cant_instrumentos):
                
                print(f"{instrumentos[i]} - {unidades[i]} unidades disponibles")
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (2) NO
                                    
                                    """))
        
        case 3:
            
            print()
            
            cant_instrumentos = len(instrumentos)
            
            for i in range(cant_instrumentos):
                instrumentos[i] = instrumentos[i].lower()
            
            ins_buscado = input("Instrumento: ").lower()
            
            if ins_buscado in instrumentos:
                
                print()
                p_instrum = instrumentos.index(ins_buscado)
                
                print(f"{instrumentos[p_instrum].capitalize()} - {unidades[p_instrum]} unidades disponibles")
            
            else:
                
                print()
                print("INSTRUMENTO NO REGISTRADO")
            
            for i in range(cant_instrumentos):
                instrumentos[i] = instrumentos[i].capitalize()
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (2) NO
                                    
                                    """))
        
        case 4:
            
            cant_instrumentos = len(instrumentos)
            
            print()
            print("Instrumentos sin unidades:")
            print()
            
            contador = 0
            
            for i in range(cant_instrumentos):
                
                if unidades[i] == 0:
                    
                    print(f"{instrumentos[i]}")
                    
                    contador += 1
            
            if contador == 0:
                print("Hay unidades de todos los intrumentos.")
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (2) NO
                                    
                                    """))
        
        case 5:
            
            print()
            cant_instrumentos = int(input("¿Cuántos instrumentos desea agregar?: "))
            
            print()
            
            for i in range(cant_instrumentos):
                
                instrumentos.append(input("Nombre del instrumento: "))
                unidades.append(int(input("Unidades: ")))
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (2) NO
                                    
                                    """))
        
        case 6:
            
            print()
            cant_instrumentos = len(instrumentos)
            
            for i in range(cant_instrumentos):
                instrumentos[i] = instrumentos[i].lower()
            
            ins_buscado = input("Nombre del instrumento: ").lower()
            print()
            
            if ins_buscado in instrumentos:
                
                p_instrum = instrumentos.index(ins_buscado)
                
                op = int(input("""¿Qué desea hacer?:
                                
                                (1) AÑADIR UNIDADES
                                (2) RESTAR UNIDADES
                                
                                """))
                
                match op:
                    
                    case 1:
                        
                        cant_suma = int(input("Cantidad a añadir: "))
                        
                        while cant_suma <= 0:
                            
                            print()
                            cant_suma = int(input("Cantidad inválida, ingrese nuevamente: "))
                        
                        unidades[p_instrum] += cant_suma
                        
                        print()
                        print(f"{instrumentos[p_instrum].capitalize()} - {unidades[p_instrum]} unidades disponibles")
                    
                    case 2:
                        
                        cant_resta = int(input("Cantidad a restar: "))
                        
                        while cant_resta <= 0 or cant_resta > unidades[p_instrum]:
                            
                            print()
                            cant_resta = int(input("Cantidad inválida, ingrese nuevamente: "))
                        
                        unidades[p_instrum] -= cant_resta
                        
                        print()
                        print(f"{instrumentos[p_instrum].capitalize()} - {unidades[p_instrum]} unidades disponibles")
            
            else:
                print("INSTRUMENTO NO REGISTRADO")
            
            for i in range(cant_instrumentos):
                instrumentos[i] = instrumentos[i].capitalize()
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (2) NO
                                    
                                    """))
        
        
        case 7:
            
            print()
            print("FIN DEL PROGRAMA.")
            continuar = 2
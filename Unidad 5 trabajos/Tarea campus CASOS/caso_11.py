continuar = 1

ordenes = ["ORD-001", "ORD-002", "ORD-003"]
horas = [2.5, 0, 4.0]

while continuar == 1:
    
    menu = int(input("""
                        
                        (1) Nueva lista de ordenes
                        (2) Mostrar agenda completa
                        (3) Consultar horas por orden
                        (4) Listar órdenes con 0 horas 
                        (5) Agregar orden
                        (6) Actualizar horas
                        (7) Salir
                        
                        """))

    
    match menu:
        
        case 1:
            
            print()
            cant_ordenes = int(input("Cantidad de ordenes: "))
            
            while cant_ordenes < 0:
                
                cant_ordenes = int(input("Valor inválido, ingrese nuevamente: "))
            
            if cant_ordenes == 0:
                
                print("No hay ordenes que agregar.")
                continue
            
            ordenes = ["" for _ in range(cant_ordenes)]
            horas = [0 for _ in range(cant_ordenes)]
            
            print()
            for i in range(cant_ordenes):
                
                ordenes[i] = input("Código de orden: ")
                horas[i] = float(input("Horas estimadas: "))
                
                while horas[i] < 0:
                    
                    horas[i] = float(input("Número inválido, ingrese nuevamente: "))
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 2:
            
            print()
            cant_ordenes = len(ordenes)
            
            print("LISTADO DE ORDENES: ")
            print()
            
            for i in range(cant_ordenes):
                
                if horas[i] > 0:
                    
                    print(f"{ordenes[i]} - {horas[i]} horas estimadas")
                
                else:
                    
                    print(f"{ordenes[i]} - SIN HORAS ASIGNADAS")
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 3:
            
            print()
            cant_ordenes = len(ordenes)
            
            for i in range(cant_ordenes):
                
                ordenes[i] = ordenes[i].lower()
            
            orden_buscada = input("Ingrese orden: ").lower()
            
            if orden_buscada in ordenes:
                
                p_orden = ordenes.index(orden_buscada)
                
                for i in range(cant_ordenes):
                    ordenes[i] = ordenes[i].upper()
                
                if horas[p_orden] > 0:
                    
                    print(f"{ordenes[p_orden]} - {horas[p_orden]} horas estimadas")
                
                else:
                    
                    print(f"{ordenes[p_orden]} - SIN HORAS ASIGNADAS")
            
            else:
                
                print()
                print("ORDEN NO REGISTRADA.")
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 4:
            
            cant_ordenes = len(ordenes)
            
            print()
            print("LISTADO DE ORDENES SIN HORAS ASIGNADAS:")
            print()
            
            contador = 0
            
            for i in range(cant_ordenes):
                
                if horas[i] == 0:
                    
                    print(f"{ordenes[i]}")
                    contador += 1
            
            if contador == 0:
                
                print("TODAS LAS ORDENES TIENEN HORAS ASIGNADAS.")
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))

            
        case 5:
            
            cant_ordenes = int(input("Ordenes a agregar: "))
            
            while cant_ordenes < 0:
                
                print()
                cant_ordenes = int(input("Número inválido, ingrese nuevamente: "))

            if cant_ordenes == 0:
                
                print()
                print("NO HAY ORDENES PARA AGREGAR.")
                continue
            
            for i in range(cant_ordenes):
                
                ordenes.append(input("CÓDIGO DE ORDEN: "))
                horas.append(float(input("HORAS ESTIMADAS: ")))
                
                while horas[i] < 0:
                    
                    horas[len(horas)-1] = float(input("Número inválido, ingrese nuevamente: "))
            
            
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 6:
            
            cant_ordenes = len(ordenes)
            
            for i in range(cant_ordenes):
                ordenes[i] = ordenes[i].lower()
            
            orden_buscada = input("ORDEN A ACTUALIZAR: ").lower()
            
            if orden_buscada in ordenes:
                
                p_orden = ordenes.index(orden_buscada)
                
                print()
                
                for i in range(cant_ordenes):
                    ordenes[i] = ordenes[i].upper()
                
                op = int(input("""OPERACIÓN A REALIZAR:
                                
                                (1) ASIGNAR HORAS
                                (2) RESTAR HORAS
                                
                                """))

                match op:
                    
                    case 1:
                        
                        cant_horas_asignadas = float(input("Horas a asignar: "))
                        
                        while cant_horas_asignadas <= 0:
                            
                            cant_horas_asignadas = float(input("Número inválido, ingresar nuevamente: "))
                        
                        horas[p_orden] += cant_horas_asignadas
                        
                        print()
                        print(f"{ordenes[p_orden]} - {horas[p_orden]} horas estimadas")
                    
                    case 2:
                        
                        if horas[p_orden] == 0:
                            
                            print()
                            print("NO HAY HORAS ASIGNADAS PARA RESTAR.")
                            continue
                        
                        cant_horas_restadas = float(input("Horas a restar: "))
                        
                        while cant_horas_restadas <= 0:
                            
                            cant_horas_restadas = float(input("Número inválido, ingresar nuevamente: "))
                        
                        horas[p_orden] -= cant_horas_restadas
                        
                        print()
                        print(f"{ordenes[p_orden]} - {horas[p_orden]} horas estimadas")
                    
                
            else:
                
                print()
                print("ORDEN NO REGISTRADA.")
                continue
            
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        case 7:
            
            print("FIN DEL PROGRAMA.")
            continuar = 0
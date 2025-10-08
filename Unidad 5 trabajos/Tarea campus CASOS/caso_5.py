
platos = ["Fideos Blancos" , "Ñoquis Rellenos" , "Asado" , "Sushi"]
porciones = [ 1 , 5 , 2 , 0]

continuar = 1

while continuar == 1:
    
    opcion = int(input("""
                        
                        ¿Qué operación desea realizar?
                        
                        (1) Ingresar lista de platos
                        (2) Mostrar platos disponibles
                        (3) Consultar porciones de un plato
                        (4) Listar platos agotados
                        (5) Agregar un nuevo plato al menú
                        (6) Gestionar venta y devolución de porciones de platos
                        (7) Ver lista completa de platos
                        (8) Salir del programa
                        
                        """))
    
    match opcion:
        
        case 1:
            
            print()
            
            cant_platos = int(input("¿Cuántos platos desea ingresar?: "))
            print()
            
            platos = ["" for _ in range(cant_platos)]
            porciones = [0 for _ in range(cant_platos)]
            
            for i in range(cant_platos):
                
                platos[i] = input("Nombre del plato: ")
                porciones[i] = int(input("Cantidad de porciones del plato: "))
                
                while porciones[i] < 0:
                    
                    porciones[i] = int(input("Valor inválido, ingrese nuevamente: "))
            
            print()
            print()
            
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        case 2:
            
            cantidad_platos = len(platos)
            
            print()
            print("PLATOS DISPONIBLES:")
            print()
            
            for i in range(cantidad_platos):
                
                if porciones[i] > 0:
                    
                    print(f"{platos[i]} , {porciones[i]} porciones disponibles")
                    
                else:
                    pass
            
            print()
            print()
            
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
            
        case 3:
            
            print()
            
            cantidad_platos = len(platos)
            
            for i in range(cantidad_platos):
                
                platos[i] = platos[i].lower()
            
            plato_buscado = input("¿Qué plato desea buscar?: ").lower()
            
            if plato_buscado in platos:
                
                pos_plato = platos.index(plato_buscado)
                
                print("PLATO DISPONIBLE: ")
                print(f"{platos[pos_plato].capitalize()} , {porciones[pos_plato]} porciones disponibles")
            
            else: 
                
                print("PLATO NO DISPONIBLE.")
            
            print()
            print()
            
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 4: 
            
            cantidad_platos = len(platos)
            
            print()
            print("PLATOS AGOTADOS:")
            print()
            
            for i in range(cantidad_platos):
                
                if porciones[i] == 0:
                    
                    print(f"{platos[i]}")
                    
                else:
                    pass
            
            print()
            print()
            
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 5: 
            
            cantidad_adicion = int(input("¿Cuantos platos desea añadir?: "))
            
            for i in range(cantidad_adicion):
                
                platos.append(input("Nombre del plato: "))
                porciones.append(int(input("Cantidad de porciones del plato: ")))
            
            print()
            print()
            
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 6:
            
            decision = int(input("""¿Qué desea gestionar?
                                    
                                    (1) VENTA
                                    (2) DEVOLUCIÓN
                                    
                                    """))
            
            match decision:
                
                case 1:
                    
                    plato_vendido = input("Plato vendido: ").lower()
                    
                    cantidad_platos = len(platos)
                    
                    for i in range(cantidad_platos):
                        
                        platos[i] = platos[i].lower()
                    
                    

                    
                    if plato_vendido in platos:
                        
                        print()
                        
                        cantidad_platos = len(platos)
                        
                        pos_plato_vendido = platos.index(plato_vendido)
                        
                        cant_ventas = int(input("¿Cuántas porciones se vendieron?:  "))
                        
                        if cant_ventas >= porciones[pos_plato_vendido]:
                            
                            while cant_ventas >= porciones[pos_plato_vendido] or cant_ventas <= 0:
                            
                                print()
                            
                                if porciones[pos_plato_vendido] > 1:
                                    cant_ventas = int(input(f"""Valor inválido, debe ser menor que la cantidad disponible ({porciones[pos_plato_vendido]}).
                                                    
                                                        Ingrese nuevamente: """))
                            
                                elif porciones[pos_plato_vendido] == 1: 
                                    print("El plato seleccionado no se puede vender, cuenta con cantidades mínimas (1)")
                                    break
                                    continue
                            
                            porciones[pos_plato_vendido] = porciones[pos_plato_vendido] - cant_ventas
                            
                            print(f"""CANTIDADES ACTUALIZADAS:
                                    
                                    {platos[pos_plato_vendido].capitalize()} , {porciones[pos_plato_vendido]} porciones disponibles
                                    
                                    """)
                            
                        else:
                            
                            porciones[pos_plato_vendido] = porciones[pos_plato_vendido] - cant_ventas
                            
                            print()
                            print(f"{platos[pos_plato_vendido].capitalize()} , {porciones[pos_plato_vendido]} porciones disponibles")
                    
                    else:
                        
                        print()
                        print("Plato no encontrado.")
                    
                    print()
                    print()
            
                    continuar = int(input("""¿Desea realizar otra operación?
                                    
                                        (1) SI
                                        (0) NO
                                    
                                        """))
                
                case 2:
                    
                    print()
                    
                    cantidad_platos = len(platos)
                    
                    plato_devuelto = input("Plato devuelto:").lower()
                    
                    for i in range(cantidad_platos):
                        
                        platos[i] = platos[i].lower()
                    
                    
                    if plato_devuelto in platos:
                        
                        cant_devolucion = int(input("¿Cuántas porciones se devolvieron?:  "))
                        
                        while cant_devolucion >= 100 or cant_devolucion <= 0:
                            
                            print()
                            
                            cant_devolucion = int(input("""Valor irreal.
                                                    
                                                        Ingrese nuevamente: """))
                        
                        pos_plato_devuelto = platos.index(plato_devuelto)
                        
                        porciones[pos_plato_devuelto] = porciones[pos_plato_devuelto] + cant_devolucion
                        
                        print()
                        print(f"""{platos[pos_plato_devuelto].capitalize()} , {cant_devolucion} porciones devueltas. 
                                Ahora hay {porciones[pos_plato_devuelto]} porciones disponibles.""")
                        
                    else:
                        
                        print()
                        print("Plato no encontrado.")
                    
                    print()
                    print()
            
                    continuar = int(input("""¿Desea realizar otra operación?
                                    
                                        (1) SI
                                        (0) NO
                                    
                                        """))

        
        case 7:
            
            print()
            
            cantidad_platos = len(platos)
            
            for i in range(cantidad_platos):
                
                print(f"{platos[i]} , {porciones[i]} porciones disponibles")
            
            print()
            print()
            
            continuar = int(input("""¿Desea realizar otra operación?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 8:
            
            print()
            print("FIN DEL PROGRAMA")
            continuar = 0